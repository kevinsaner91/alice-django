from django.shortcuts import render
from django.http import HttpResponseRedirect
from collections import OrderedDict
import json
from . import api

def get_credentials(request):
    print('Credentials')

    credentials = api.get_credentials()

    return render(request,'credentials/credentials.html', {'credentials': credentials})

def get_credential_detail(request, referent):
    print('get_credential_detail')

    credential = api.get_credential_detail(referent)


    return render(request, 'credentials/credential-detail.html', {'credential': credential, 'show': False })

def delete_credential(request, referent):
    print('delete credential')

    delete = False

    if api.delete_credential(referent):
        delete = True
        credentials = api.get_credentials()
        return render(request,'credentials/credentials.html', {'credentials': credentials, 'delete': delete})
    else:
        credential = api.get_credential_detail(referent)
        return render(request, 'credentials/credential-detail.html', {'credential': credential, 'delete': delete, 'show': False})

def check_revoked(request, referent):
    print('check_revoked')

    revoked = False

    if api.check_revoked(referent):
        revoked = True
        credential = api.get_credential_detail(referent)
        return render(request, 'credentials/credential-detail.html', {'credential': credential,'revoked': revoked, 'show': True})
    else:
        credential = api.get_credential_detail(referent)
        return render(request, 'credentials/credential-detail.html', {'credential': credential,'revoked': revoked, 'show': True})    

        


