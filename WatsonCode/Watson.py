import subprocess
import json
import requests
#from ibm_watson import IAMTokenManager


privateinfo = open("Private.txt","r")
APIkey = privateinfo.readline()
WatsonURL = privateinfo.readline()

def make_Post_request(url, line):
    headers = {"Authorization": "TOKEN " + APIkey}
    Data= {"text": line, "features":{"setiment":{}}}
    resp = requests.post(url, headers=headers, data= Data)
    return resp




file = open("lines.txt","r")
lines = file.readlines()
for x in lines:
    print(make_Post_request(WatsonURL,x))
    print(APIkey)
    print(WatsonURL)
