import requests
import json



def get_credentials():
    print('get_credentials')
    response = requests.get(
         'https://alice-api.educa.ch/credentials', 'GET')
    data = json.loads(response.text)

    credentials_list = list()

    for records in data["results"]:

        credentials_list.append(
            {
                'referent': records['referent'],
                'schema_id': records['schema_id'],
                'cred_def_id': records['cred_def_id'],
                'rev_reg_id': records['rev_reg_id'],
                'cred_rev_id': records['cred_rev_id'],
                'attrs': records['attrs']

            }
        )    

    return credentials_list