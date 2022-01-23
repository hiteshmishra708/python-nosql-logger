from pynosql_logger.constant import DEFAULT_SUCCESS_MESSAGE
from pynosql_logger.helper import get_uuid
from datetime import datetime

class Meta:
    @staticmethod
    def add_meta(idx, item):
        if item:
            item['_log_id'] = get_uuid(idx)
            item['_updated_at'] = datetime.now().strftime("%d-%b-%Y %I:%M %p")
        return item

class Response:
    @staticmethod
    def get_response(resp, message=DEFAULT_SUCCESS_MESSAGE):
        resp['success'] = True
        resp['message'] = message
        return resp

    @staticmethod
    def get_error(err):
        return {
            'success': False,
            'message': str(err)
        }
