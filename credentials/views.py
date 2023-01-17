from django.shortcuts import render
from django.http import HttpResponseRedirect
from collections import OrderedDict
import json
from . import api

def get_credentials(request):
    print('Credentials')

    credentials = api.get_credentials()

    print(credentials)

    return render(request,'credentials/credentials.html', {'credentials': credentials})
