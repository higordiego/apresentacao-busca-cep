import requests

payload={}
headers = {}

# https://cdn.apicep.com/file/apicep/06233-030.json

def endereco_url(cep, provider= None):
    if provider is None or provider == 'viacep':
        provider = 'viacep'
        return "https://viacep.com.br/ws/"+ cep + "/json"
    return "https://cdn.apicep.com/file/apicep/"+cep+".json"


def get_cep(cep):
    url = endereco_url(cep)
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
