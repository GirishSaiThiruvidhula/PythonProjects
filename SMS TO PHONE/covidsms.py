import requests
import json
from bs4 import BeautifulSoup
import time



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


def getData(req_url):
    request_url = requests.get(req_url)
    return request_url.text

def sendDataforSMS(text_message):
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    # get response
    api_key = 'KMQ7RU20ARJBPYW2VHAR5H65JVRGJY3N'
    secret_key = 'BCHYLRE68W8MVGY5'
    use_type = 'stage'
    phone_number = 9581776039
    emailID = 'girish.sai1993@gmail.com'
    text_message = text_message
    response = sendPostRequest(URL, api_key, secret_key, use_type ,phone_number , emailID, text_message )
    """
      Note:-
        you must provide apikey, secretkey, usetype, mobile, senderid and message values
        and then requst to api
    """
    return response.text

def listOFList(datalist):
    newList = []
    start = 0
    end = 5
    while(end < len(datalist)):
       newList.append(datalist[start:end])
       start = end
       end = end + 5
    return newList

def getCoronaData():
    req_url ='https://www.mohfw.gov.in/'
    myDataStr = ""
    dataStr = ""
    # notifyMe("Girish", "This is the test to push notifications")
    myHtlmlData = getData(req_url)
    soup = BeautifulSoup(myHtlmlData, 'html.parser')
    # print(soup.prettify())
    for tr in soup.find_all('tbody')[-1].find_all('tr'):
        myDataStr += tr.get_text()
    
    myDataStr = myDataStr[1:]
    myDatList = myDataStr.split("\n")
    [myDatList.remove(ele) for ele in myDatList if ele == '']
    myDatList = myDatList[0:-7]
    myDatList = listOFList(myDatList)
    
    states = ['Andhra Pradesh','Telengana','Karnataka']
    for dataList in myDatList:
        if dataList[1] in states:
            nTitle = "Covid-19 Cases"
            nText = f"State : {dataList[1]}\nConfirmed : {dataList[2]}\nRecovered : {dataList[3]}\nDeaths : {dataList[4]}"
            dataStr += nText +'\n\n'
    return dataStr

if __name__ == "__main__":
    caronaData = getCoronaData()
    resultSMS = sendDataforSMS(caronaData)
    print(resultSMS)
