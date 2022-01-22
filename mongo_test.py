from nosqllogger.loggers import MongoLogger

connection_string = 'mongodb+srv://hitesh:hitesh@cluster0.cfy1e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
logger = MongoLogger(connection_string)

# add log
req_json = {
    'users': {
        'first_name': 'Hitesh',
        'last_name': 'Mishra',
        'email': 'hiteshmishra708@gmail.com',
    }
}
resp = logger.add_log(req_json)

# add logs
req_json = {
    'users': [{
        'first_name': 'Test',
        'last_name': 'User 1',
        'email': 'testuser1@mailnesia.com',
    }, {
        'first_name': 'Test',
        'last_name': 'User 2',
        'email': 'testuser2@mailnesia.com',
    }]
}
resp = logger.add_log(req_json)

# get log
req_json = {
    'users': {
        'first_name': 'Hitesh'
    }
}
resp = logger.get_log(req_json)

# get logs
req_json = {
    'collection': 'users'
}
resp = logger.get_all_logs(req_json)