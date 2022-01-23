import threading
from pynosql_logger.loggers import MongoLogger, ElasticLogger

class AsyncMongoLogger(MongoLogger):

    def add_log(self, req_json):
        t1 = threading.Thread(target = MongoLogger.add_log, args = (self, req_json,))
        t1.start()

class AsyncElasticLogger(ElasticLogger):
    
    def add_log(self, req_json):
        t1 = threading.Thread(target = ElasticLogger.add_log, args = (self, req_json,))
        t1.start()