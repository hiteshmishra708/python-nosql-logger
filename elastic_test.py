from pynosql_logger.loggers import ElasticLogger

elastic_url = 'http://127.0.0.1:9200'
logger = ElasticLogger(elastic_url)

# add log
req_json = {
    'users': {
        'first_name': 'Hitesh',
        'last_name': 'Mishra',
        'email': 'hiteshmishra708@gmail.com',
        'id': 1
    }
}
resp = logger.add_log(req_json)

# add logs
req_json = {
    'users': [{
        'first_name': 'Test',
        'last_name': 'User 1',
        'email': 'testuser1@mailnesia.com',
        'id': 2
    }, {
        'first_name': 'Test',
        'last_name': 'User 2',
        'email': 'testuser2@mailnesia.com',
        'id': 3
    }]
}
resp = logger.add_log(req_json)

# get log
req_json = {
    'users': {
        'email': '@mailnesia'
    }
}
resp = logger.get_log(req_json)

# get logs
req_json = {
    'collection': 'users'
}
resp = logger.get_all_logs(req_json)