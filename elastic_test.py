from pynosql_logger.loggers import ElasticLogger

elastic_url = 'http://127.0.0.1:9200'
logger = ElasticLogger(elastic_url)

# add log
req_json = {
    'users': {
        'first_name': 'Hitesh',
        'last_name': 'Mishra',
        'email': 'hiteshmishra708@gmail.com'
    }
}
resp = logger.add_log(req_json)
print('add_log', resp)

# add logs
req_json = {
    'users': [{
        'first_name': 'Test',
        'last_name': 'User 1',
        'email': 'testuser1@mailnesia.com'
    }, {
        'first_name': 'Test',
        'last_name': 'User 2',
        'email': 'testuser2@mailnesia.com'
    }]
}
resp = logger.add_log(req_json)
print('add_logs', resp)

# get log
es_query = {
    "users": {
        "query": {
            "multi_match": {
                "query": '@mailnesia',
                "type": "bool_prefix",
                "fields": ['email']
            }
        }
    }
}
resp = logger.get_log(es_query)
print('get_log', resp)

# get logs
req_json = {
    'collection': 'users'
}
resp = logger.get_all_logs(req_json)
print('get_all_logs', resp)