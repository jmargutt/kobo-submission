import requests
import json

URL = f'https://kobo.ifrc.org/api/v2/assets/{ASSET_ID}/data/bulk/'
TOKEN = 'your_secret_token'
PARAMS = {
    'fomat': 'json'
}
HEADERS = {
    'Authorization': f'Token {TOKEN}'
}

payload = {
    'submission_ids': ['1111', '1112'],
    'data': {'group_name/question_name': 'new_value'}
}

res = requests.patch(
    url=URL,
    data={'payload': json.dumps(payload)},
    params=PARAMS,
    headers=HEADERS
)
