from flask import Flask,request
from pprint import pprint
from getairport import getairportname

app=Flask(__name__)

@app.route('/')
def hello():
  return "This is my webhook page"

@app.route('/', methods=['POST'])
def webhook():
  req= request.get_json(force=True)
  cityname=req['sessionInfo']['parameters']['destination_city']
  print("City name is :", cityname)
  airportname=getairportname(cityname)
  
  response={
          "fulfillmentResponse": {
              "messages": [
                  {
                      "text": {
                          "text": [
                              f"the airport name for your city {cityname} is {airportname}"] 
                      }
                  }
              ]
          }
      }
  # pprint(req)
  return response

if __name__=="__main__":
  app.run(debug=True, port=5600)