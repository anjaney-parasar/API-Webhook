import http.client
import json

conn = http.client.HTTPSConnection("vgtechdemo.com")


def getairportname(city):

    payload = f'{{\"search\": "{city}"}}'

    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/flight/airports", payload, headers)

    res = conn.getresponse()
    data = res.read()
    response=json.loads(data.decode("utf-8"))
    airportname=response['data'][0]["airports"][0]['label']
    return airportname