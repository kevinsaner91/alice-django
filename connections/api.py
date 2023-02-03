import requests
import json
import base64



def get_active_connections():
    print('get_active_connections')
    response = requests.get(
         'https://alice-api.educa.ch/connections', 'GET')
    data = json.loads(response.text)

    connection_list = list()

    for records in data["results"]:
        if records["state"] == "active":
            connection_list.append(
                {
                    "connection_id": records["connection_id"],
                    "their_label": records["their_label"],
                    "their_did": records["their_did"],
                    "last_updated": records["updated_at"]
                }
            )

    return connection_list


def get_connection_invitation():
    print('new_connection_invitation')

    url = 'https://alice-api.educa.ch/out-of-band/create-invitation'
    data = {
          "accept": [
               "didcomm/aip1",
                "didcomm/aip2;env=rfc19"
               ],
           "alias": "",
          "handshake_protocols": [
                "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"
               ],
           "metadata": {},
          "my_label": "Invitation to Faber",
            "protocol_version": "1.1",
            "use_public_did": "false"
          }
    headers = {"Content-Type": "application/json"}

    response = requests.post(
            url,
            json=data,
            headers=headers)

    print(response.json())

    data = json.loads(response.text)

    print(data)

    return data["invitation_url"]


def accept_connection(connection_info):
    print('accept_connection')
    connection_info = connection_info.replace(" ", "")

    if is_valid_connection_string(connection_info):

        url = 'https://alice-api.educa.ch/out-of-band/receive-invitation'
        data = decode(connection_info)
        headers = {"Content-Type": "application/json"}

        print(data)

        response = requests.post(
        url,
        data=data,
        headers=headers)

        print(response.status_code)    
        print(response.reason)

        if response.status_code == 200:
            print('successful')
            return True
        else:
            return False
    else:
        return False

def is_valid_connection_string(connection_info):
    print('is_valid_connection_strin')
    if "oob=" in connection_info:
        base64_info = connection_info.split('=', 1)
        try:
            decoded_connection_bytes = base64.b64decode(base64_info[1])
            decoded_connection_info = decoded_connection_bytes.decode()
       
            json.loads(decoded_connection_info)
            return True
        except (json.JSONDecodeError, base64.binascii.Error):
            print('Connection string format invalid')
            return False
    else:
        return False    
    
def decode(connection_info):
    print('decode')
    base64_info = connection_info.split('=', 1)
    
    decoded_connection_bytes = base64.b64decode(base64_info[1])
    decoded_connection_info = decoded_connection_bytes.decode()
    
    return decoded_connection_info
