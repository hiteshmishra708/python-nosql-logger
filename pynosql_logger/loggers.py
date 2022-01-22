from pynosql_logger.constant import DEFAULT_DB_NAME
from pynosql_logger.helper import get_json, ConnectionType
from pynosql_logger.response import Response

class MongoLogger:
    def __init__(self, mongodb_connection_string, c_type=ConnectionType.SYNC, db_name=DEFAULT_DB_NAME):
        self.__connection_string = mongodb_connection_string
        self.__db_name = db_name
        self.__db = self.__connect_db()
        self.__c_type = c_type

    def __connect_db(self):
        """Connect to MongoDB database with the given connection string."""
        from pymongo import MongoClient
        client = MongoClient(self.__connection_string)
        db = client[self.__db_name]
        return db

    def add_log(self, req_json):
        """Update the logs into the collection if collection exists
           else create collection and add logs.
        """
        try:
            count, keys = 0, req_json.keys()
            for key in keys:
                if type(req_json[key]) == list:
                    for record in req_json[key]:
                        self.__db[key].insert_one(record)
                        count += 1
                else:
                    self.__db[key].insert_one(req_json[key])
                    count += 1
            message = 'Added {} record successfully in {} collection'.format(count, ', '.join(keys))
            return {
                'success': True,
                'message': message
            }
        except Exception as ex:
            return Response.get_error(ex)

    def get_log(self, req_json):
        """Return the logs that matches the query."""
        try:
            count, keys, resp = 0, req_json.keys(), {}
            for key in keys:
                resp[key] = list(self.__db[key].find(req_json[key]))
                count += len(resp[key])
            message = 'Found {} record successfully in {} collection'.format(count, ', '.join(resp.keys()))
            res = get_json(resp)
            res['success'] = True
            res['message'] = message
            return Response.get_response(res, message)
        except Exception as ex:
            return Response.get_error(ex)
    
    def get_all_logs(self, req_json):
        """Returns all logs of collection."""
        try:
            count, keys, resp = 0, req_json.keys(), {}
            for key in keys:
                if type(req_json[key]) == list:
                    for collection in req_json[key]:
                        resp[collection] = get_json(list(self.__db[collection].find()))
                        count += 1
                else:
                    resp[req_json[key]] = get_json(list(self.__db[req_json[key]].find()))
                    count += 1
            message = 'Found {} record successfully in {} collection'.format(count, ', '.join(resp.keys()))
            res = get_json(resp)
            res['success'] = True
            res['message'] = message
            return Response.get_response(res, message)
        except Exception as ex:
            return Response.get_error(ex)

class ElasticLogger:
    def __init__(self, elastic_url, c_type=ConnectionType.SYNC):
        self.__elastic_url = elastic_url
        self.__c_type = c_type

    def __insert(self, idx, arr):
        import json, requests
        url = '{}/{}/'.format(self.__elastic_url, idx)
        resp = requests.get(url)
        if resp.json().get("error"):
            resp = requests.put(url, json={})
        njson = []
        for item in arr:
            njson.append(
                json.dumps({"update": {"_id": item["id"], "_index": idx}}))
            njson.append(json.dumps({"doc": item, "doc_as_upsert": True}))

        if njson:
            url = '{}/_bulk'.format(self.__elastic_url)
            resp = requests.post(url, data="{0}{1}".format(u"\n".join(map(str, njson)), "\n"),
                                                headers={"Content-Type": "application/x-ndjson"})

            if resp.json().get("errors"):
                print("Not updated")

    def __find(self, idx, req_query):
        import requests
        fields = list(req_query.keys())
        es_query = {
            # "from": 0,
            # "size": 10,
            "query": {
                "multi_match": {
                "query": req_query[fields[0]],
                "type": "bool_prefix",
                "fields": fields
                }
            }
        }
        url = "{}/{}/_search".format(self.__elastic_url, idx)
        resp = requests.get(url, json=es_query)
        rs = resp.json()
        eresults = rs.get("hits", {}).get("hits", [])
        return [pr["_source"] for pr in eresults]

    def __find_all(self, idx):
        import requests
        es_query = {
            "query": {
                "match_all": {}
            }
        }
        url = "{}/{}/_search".format(self.__elastic_url, idx)
        resp = requests.get(url, json=es_query)
        rs = resp.json()
        eresults = rs.get("hits", {}).get("hits", [])
        return [pr["_source"] for pr in eresults]

    def add_log(self, req_json):
        """Update the logs into the index if index exists
           else create index and add logs.
        """
        try:
            count, keys = 0, req_json.keys()
            for key in keys:
                if type(req_json[key]) == list:
                    self.__insert(key, req_json[key])
                    count += len(req_json[key])
                else:
                    self.__insert(key, [req_json[key]])
                    count += 1
            message = 'Added {} record successfully in {} collection'.format(count, ', '.join(keys))
            return {
                'success': True,
                'message': message
            }
        except Exception as ex:
            return Response.get_error(ex)

    def get_log(self, req_json):
        """Return the logs that matches the query."""
        try:
            count, keys, resp = 0, req_json.keys(), {}
            for key in keys:
                resp[key] = list(self.__find(key, req_json[key]))
                count += len(resp[key])
            message = 'Found {} record successfully in {} collection'.format(count, ', '.join(resp.keys()))
            res = get_json(resp)
            res['success'] = True
            res['message'] = message
            return Response.get_response(res, message)
        except Exception as ex:
            return Response.get_error(ex)

    def get_all_logs(self, req_json):
        """Returns all logs of collection."""
        try:
            count, keys, resp = 0, req_json.keys(), {}
            for key in keys:
                if type(req_json[key]) == list:
                    for collection in req_json[key]:
                        resp[collection] = get_json(list(self.__find_all(collection)))
                        count += 1
                else:
                    resp[req_json[key]] = get_json(list(self.__find_all(req_json[key])))
                    count += 1
            message = 'Found {} record successfully in {} collection'.format(count, ', '.join(resp.keys()))
            res = get_json(resp)
            res['success'] = True
            res['message'] = message
            return Response.get_response(res, message)
        except Exception as ex:
            return Response.get_error(ex)