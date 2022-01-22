from unittest import TestCase
from pynosql_logger.loggers import MongoLogger

class PyLoggerTests(TestCase):
    def setUp(self):
        # connection_string = 'mongodb://tester:tester@localhost:27017/test'
        connection_string = 'mongodb+srv://hitesh:hitesh@cluster0.cfy1e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        self.logger = MongoLogger(connection_string)

    def test_add_log(self):
        req_json = {
            'users': {
                'first_name': 'Hitesh',
                'last_name': 'Mishra',
                'email': 'hiteshmishra708@gmail.com',
            }
        }
        resp = self.logger.add_log(req_json)
        self.assertTrue(resp['success'], msg='Failed to add log')

    def test_bulk_log(self):
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
        resp = self.logger.add_log(req_json)
        self.assertTrue(resp['success'], msg='Failed to add logs')

    def test_get_json(self):
        req_json = {
            'users': {
                'first_name': 'Hitesh'
            }
        }
        resp = self.logger.get_log(req_json)
        self.assertTrue(resp['success'], msg='Failed to get log')

    def test_get_all_logs(self):
        req_json = {
            'collection': 'users'
        }
        resp = self.logger.get_all_logs(req_json)
        self.assertTrue(resp['success'], msg='Failed to get log')
