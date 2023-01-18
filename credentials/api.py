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
                'attrs': records['attrs']

            }
        )    

    return credentials_list

def get_credential_detail(referent):
    print('get_credential_detail') 

    response = requests.get('https://alice-api.educa.ch/credential/' + referent, 'GET')  

    print(response.text)     
    data = json.loads(response.text)

    return data

def delete_credential(referent):
    print('delete_credential') 

    response = requests.delete('https://alice-api.educa.ch/credential/' + referent)

    if response.status_code == 200:
        return True 
    else:
        return False

def check_revoked(referent):
    print('check_revoked')

    response = requests.get('https://alice-api.educa.ch/credential/revoked/' + referent, 'GET')
    data = json.loads(response.text)

    print(data)

    if data["revoked"]:
        return True
    else:
        return False



       

