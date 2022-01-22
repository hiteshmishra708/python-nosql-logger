import json
from functools import wraps

class ConnectionType:
    SYNC = 1
    ASYNC = 2

def get_json(data):
    return json.loads(json.dumps(data, default=str))

def auth_decorator():
    def _auth_decorator(f):
        @wraps(f)
        def __auth_decorator(*args, **kwargs):
            # just do here everything what you need
            app = request.args.get('app')
            key = request.args.get('key')
            if app not in ALLOWED_REQUESTS or ALLOWED_REQUESTS[app] != key:
                return {
                    'success': False,
                    'message': 'No Access'
                }
            result = f(*args, **kwargs)
            return result
        return __auth_decorator
    return _auth_decorator