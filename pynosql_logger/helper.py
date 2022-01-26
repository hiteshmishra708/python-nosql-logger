import json, uuid

def get_json(data):
    return json.loads(json.dumps(data, default=str))

def get_uuid(idx):
    return '{}-{}'.format(idx, str(uuid.uuid4()))