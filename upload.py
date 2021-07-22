from requests import post, get
import os

url = os.environ.get('URL')
key = os.environ.get('KEY')
def get_bom_xml(bom_xml: str = 'bom.xml') -> str:
    with open(bom_xml, 'r') as bom:
        return bom.read()


def submit_bom():

    headers = {'X-Api-Key': key}

    payload = {'bom': get_bom_xml(),
               'projectName': 'test',
               'projectVersion': '1',
               'autoCreate': False}

    response = post(f'{url}/api/v1/bom', headers=headers, files=payload)
    print (response.status_code, response.reason, response.text)


submit_bom()