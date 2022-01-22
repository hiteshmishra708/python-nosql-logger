from pynosql_logger.constant import DEFAULT_SUCCESS_MESSAGE

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
