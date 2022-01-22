# pymongo-logger
pymongo-logger

### Initialize
```
  connection_string = 'your_mongodb_connection_string'
  logger = MongoLogger(connection_string)
```

### Add Log
```
  req_json = {
      'users': {
          'first_name': 'Hitesh',
          'last_name': 'Mishra',
          'email': 'hiteshmishra708@gmail.com',
      }
  }
  resp = self.logger.add_log(req_json)
```

### Add Bulk Log
```
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
```

### Get Log
```
  req_json = {
      'users': {
          'first_name': 'Hitesh'
      }
  }
  resp = logger.get_log(req_json)
```

### Add All Logs
```
  req_json = {
      'collection': 'users'
  }
  resp = self.logger.get_all_logs(req_json)
```