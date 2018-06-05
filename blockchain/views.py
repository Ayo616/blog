from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    content = 'hello,world'
    from web3.auto import w3
    from web3.eth import Eth
    from web3 import Web3

    web = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

    # eth = Eth(w3)
    eth = Eth(web)
    content = str(dict(eth.getBlock('latest')))
    print(content)
    return  HttpResponse(content)

