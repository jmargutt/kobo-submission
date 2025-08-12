import requests
import uuid

headers = {
    'Authorization': f'Token <my-token>',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

submission = {
    'meta': {
        'instanceID': f'uuid:{uuid.uuid4()}'
    },
    'question1': 'answer1',
    'group1': {
        'question2': 'answer2'
    }
}

data_request = requests.post(
    f'https://kc.ifrc.org/api/v1/submissions',
    json={
        "id": "<my-asset>",
        "submission": submission
    },
    headers=headers
)

