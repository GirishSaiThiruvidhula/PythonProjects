import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
api_key = 'KMQ7RU20ARJBPYW2VHAR5H65JVRGJY3N'
secret_key = 'BCHYLRE68W8MVGY5'
use_type = 'stage'
phone_number = 9581776039
emailID = 'girish.sai1993@gmail.com'
text_message = 'Hi, This is Girish and I am texting the SMS to phone thorugh Python'
response = sendPostRequest(URL, api_key, secret_key, use_type ,phone_number , emailID, text_message )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)