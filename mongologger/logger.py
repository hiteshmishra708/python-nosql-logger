from pymongo import MongoClient
# import mongologger.constant, mongologger.helper
from mongologger.constant import DEFAULT_DB_NAME
from mongologger.helper import get_json
from mongologger.response import Response

class MongoLogger:
    def __init__(self, mongodb_connection_string, db_name=DEFAULT_DB_NAME):
        self.__connection_string = mongodb_connection_string
        self.__db_name = db_name
        self.__db = self.__connect_db()

    def __connect_db(self):
        client = MongoClient(self.__connection_string)
        db = client[self.__db_name]
        return db

    def add_log(self, req_json):
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