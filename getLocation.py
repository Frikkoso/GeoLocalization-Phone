import requests
import json

def getIpLocarion(ip_Address, Token_Key):
    url = 'http://api.ipstack.com/{ip}?access_key={key}'.format(ip=Ip_Address, key=Token_Key)

    headers = {'Content-Type'.'application/json'}

    response = requests.get(url, headers)
    print('Request =',response)
    print('**************************')
    #print(response.text)
    parsed_json = (json.loads(response.text))
    print(json.dumbs(parsed_json, indent=4, sort_keys=True))
    