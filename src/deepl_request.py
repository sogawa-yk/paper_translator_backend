import yaml
import httpx as requests
from requests.exceptions import Timeout


def translate(text):
    with open('/app/paper_translator_backend/data/config.yaml') as file:
        key = yaml.safe_load(file.read())['api_key']


    params = {
        'auth_key': key,
        'text': text,
        'source_lang': 'EN',
        'target_lang': 'JA'
    }

    try:
        request = requests.post('https://api-free.deepl.com/v2/translate', data=params, timeout=(5.0, 15.0))
        result = request.json()
    except Timeout:
        return 'Timeout!!'
    
    return result['translations'][0]['text']
