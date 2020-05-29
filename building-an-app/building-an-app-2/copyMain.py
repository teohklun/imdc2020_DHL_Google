
# import import_ipynb
from job import Job
from vehicle import Vehicle
import importlib
import numpy as np
from typing import Dict, Tuple, Sequence, List, Any
import pandas as pd 
import datetime
import types
import requests

from typing import Dict, Tuple, Sequence, List, Any
# import polyline

import json

import pprint

 
import os
# import pymysql
import pandas as pd

import logging
import os
from google.cloud import storage

from flask import Flask
from io import StringIO
from flask import jsonify

# datastore_client = datastore.Client()

csvPath = "3.csv"



date = "20200204"
session = "m"
street = "Jalan Rumbia, Kampung Seberang Paya, 11900 Bayan Lepas, Pulau Pinang"


# import google.cloud.storage as gcs
# import webapp2

# from google.appengine.api import app_identity
#[END imports]

#[START retries]
# my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
#                                           max_delay=5.0,
#                                           backoff_factor=2,
#                                           max_retry_period=15)
# gcs.set_default_retry_params(my_default_retry_params)

# CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')
# # Create a Cloud Storage client.
# storage_client = gcs.Client()

# # Get the bucket that the file will be uploaded to.
# bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)

# def get(self):
#     # bucket_name = os.environ.get('BUCKET_NAME',
#     #                              app_identity.get_default_gcs_bucket_name())

#     # self.response.headers['Content-Type'] = 'text/plain'
#     # self.response.write('Demo GCS Application running from Version: '
#     #                     + os.environ['CURRENT_VERSION_ID'] + '\n')
#     # self.response.write('Using bucket name: ' + bucket_name + '\n\n')
# #[END get_default_bucket]

#     # bucket = '/' + bucket_name
#     filename = bucket + '/demo-testfile'
#     # self.tmp_filenames_to_clean_up = []

# def gcloudWriteFile(self, filename, content, optionWrite = "w"):
#     """Create a file.

#     The retry_params specified in the open call will override the default
#     retry params for this particular file handle.

#     Args:
#       filename: filename.
#     """
#     self.response.write('Creating file %s\n' % filename)

#     write_retry_params = gcs.RetryParams(backoff_factor=1.1)
#     gcs_file = gcs.open(filename,
#                         optionWrite,
#                         content_type='text/plain',
#                         options={'x-goog-meta-foo': 'foo',
#                                  'x-goog-meta-bar': 'bar'},
#                         retry_params=write_retry_params)
#     gcs_file.write(content)
#     gcs_file.close()
#     # self.tmp_filenames_to_clean_up.append(filename)

# def gcloudReadFile(self, filename):
#     self.response.write('Abbreviated file content (first line and last 1K):\n')

#     gcs_file = gcs.open(filename)
#     self.response.write(gcs_file.read())
#     contents = gcs_file.read()
#     gcs_file.close()

# def write_file(fileName : str, content : str):
#     text_file = open(fileName, "w")
#     n = text_file.write(content )
#     text_file.close()




def getResponseFileName(date : str, session : str ):
    from pathlib import Path

#     path = Path(__file__).parent / "../data/test.csv"
    return "files/february/" + date + "-" + session + "-response.json"

# def saveRecordToDataBase(date : str, session : str) -> str: 
#     host = os.getenv('MYSQL_HOST')
#     port = os.getenv('MYSQL_PORT')
#     user = os.getenv('MYSQL_USER')
#     password = os.getenv('MYSQL_PASSWORD')
#     database = os.getenv('MYSQL_DATABASE')

#     json_file_name = getResponseFileName(date, session)
#     # json_file_name = "response.json"

#     conn = pymysql.connect(
#         host=host,
#         port=int(3306),
#         user="root",
#         passwd=password,
#         db="dhl-project",)
#     #     charset='utf8mb4')
#     try:
#         connObject = conn.cursor()
#         command = "INSERT INTO optimal_summary (date, session, response_name) VALUES (%s,%s,%s)"

#         connObject.execute(command, (date,session,json_file_name,))
#         # print(df)
#         conn.commit()

#     except Exception as e:
#         print("Exeception occured:{}".format(e))

#     finally:
#         conn.close()
#         return json_file_name
    
# def deleteRecordToDataBase(date : str, session : str): 
#     host = os.getenv('MYSQL_HOST')
#     port = os.getenv('MYSQL_PORT')
#     user = os.getenv('MYSQL_USER')
#     password = os.getenv('MYSQL_PASSWORD')
#     database = os.getenv('MYSQL_DATABASE')
#     # json_file_name = "response.json"

#     conn = pymysql.connect(
#         host=host,
#         port=int(3306),
#         user="root",
#         passwd=password,
#         db="dhl-project",)
#     #     charset='utf8mb4')
#     try:
#         connObject = conn.cursor()
#         command = "delete from optimal_summary where date = %s and session = %s"
#         connObject.execute(command, (date,session))
#         # print(df)
#         conn.commit()

#     except Exception as e:
#         print("Exeception occured:{}".format(e))

#     finally:
#         conn.close()

def write_file(fileName : str, content : str):

    text_file = open(fileName, "w")
    n = text_file.write(content )
    text_file.close()
    
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
    
# def getTimeWindow(start, end):
    
def getMiliSec(time_str: float) -> int:
    """Get Seconds from time."""
#     if(type(time_str) == "float"):
#     if(type(time_str) is types.Float):
#             elif isinstance(obj, np.floating):

    time_str = str(time_str)
    
    h, m = time_str.split(':')
    return int(h) * 3600   + int(m) * 60

def getTimeWindow(start : float ,end : float) -> List:
    if(start != start ):
        start = "00:00"
    if(end == "23:59"):
        end = "20:00"
    if(end != end):
        end = "23:59"
    return [ getMiliSec(start), getMiliSec(end) ]
    
def sendRequest(fileName : str):

    url = 'http://35.213.166.175:3000'
    #payload = open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=open(fileName, 'rb'), headers=headers) 

#function declaration
def getActualQueryAdress(companyName: str, street : str)-> str:
    string = companyName + "+" + street
    return string

def parseStringToHtml(string :str) -> str:
    string  =string.replace(" ","+")
    return string

def getLocationWithStreetNameOrCustomerName(companyName: str, street : str) -> List:
    stringRquestStreet = getActualQueryAdress(parseStringToHtml(companyName), parseStringToHtml(street))
    api_key = "AIzaSyA2H1uflVbzM7wtGeMlbwpLKnMkFIJdWVc"
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + stringRquestStreet + ',+CA&key='+api_key+''
    # url = "https://maps.googleapis.com/maps/api/js?key="+api_key+"&libraries=places"
    # url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+stringRquestStreet+"&inputtype=textquery&fields=formatted_address,name,plus_code,geometry&key="+api_key+""
    # url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=BJ Court&inputtype=textquery&fields=formatted_address,name,plus_code,geometry&key="+api_key+""

    payload = {'key1': 'value1', 'key2': 'value2'}

    # POST with JSON 
    r = requests.post(url, data=json.dumps(payload))

    # Response, status etc
    r.text
    parsed = json.loads(r.text)

    return parsed["results"][0]["geometry"]["location"]

url = 'http://35.213.166.175:3000'

def getDeliveryRoute(partialDataFrame : List, fullDataFrame : List, session : str):
#     print("DASDASDDASDSDSDASDS")
    deliveryList = []
    deliveryListRoute=[]
#     print(len(partialDataFrame))
#     for x in range(0, len(partialDataFrame)):
    for index, x in partialDataFrame.iterrows():
        valid = False
        if(x["Act Ckpt Code"] ==  "DEPAR" or x["Act Ckpt Code"]==  "ARRVD"):
            valid = True
#csv not two departure / arrival per session
#                             if( (session == "m") & 
#                                (getMiliSec(x["Act Tm"]) > getMiliSec("08:45") ) & 
#                                (getMiliSec(x["Act Tm"]) < getMiliSec("13:59") ) ):
#                     #                 print("here before")
#                                 valid = True
#                             elif( (session == "a") & 
#                                  (getMiliSec(x["Act Tm"]) > getMiliSec("14:00") )& 
#                                  (getMiliSec(x["Act Tm"]) < getMiliSec("23:59") ) ):
#                                 valid = True
#                             else:
#                     #                 print(x)
#                                 print("undefined session 222")
#                                 valid=False
            if(deliveryListRoute != []):
                deliveryList.append(deliveryListRoute)
                deliveryListRoute = []
            else:
                deliveryListRoute = []
        else:
#             if(valid):
            #logic for morning afternoon
            if( (session == "m") & (getMiliSec(x["Act Tm"]) > getMiliSec("08:45") ) & (getMiliSec(x["Act Tm"]) < getMiliSec("13:59") ) ):
                valid = True
            elif( (session == "a") & (getMiliSec(x["Act Tm"]) > getMiliSec("14:00") ) & (getMiliSec(x["Act Tm"]) < getMiliSec("23:59")  ) ) :
                valid = True
            else: #false for afternoon session first
                valid = False
            if(valid):
                if(x["lgtd"] != x["lgtd"] or x["lat"] != x["lat"]): # lat or long None
                    location = getLocationWithStreetNameOrCustomerName(x["Customer Name"], x["Street"])

                    lat = location["lat"]
                    lgtd = location["lng"]
    #                     print(lat)
                    #update the file
                    fullDataFrame.at[index, 'lat'] = lat
                    fullDataFrame.at[index, 'lgtd'] = lgtd

                    #update today
                    x["lat"] = lat
                    x["lgtd"] = lgtd
        if(valid):
            deliveryListRoute.append(x)
#     print(deliveryList[0])
    return deliveryList, fullDataFrame
        
def getTimeWindowWithSession(session : str) -> List:
    if(session == "m"):
#         timeWindow = getTimeWindow("09:00",  "18:45" )
#         timeWindow = getTimeWindow("09:00",  "13:45" )
        timeWindow = getTimeWindow("08:45",  "13:59" )

    elif(session =="a"):
        timeWindow = getTimeWindow("14:00",  "18:45" )
#         timeWindow = getTimeWindow("09:00",  "18:45" )

    else:
        print("undefined session")
        timeWindow = getTimeWindow("09:00",  "13:00" ) #default morning
        
    return timeWindow

def createJobsAndVehiclesList(deliveryList : List, timeWindow : List):
    subangLocation = [101.9381 ,2.7297] #should be seremban
    jobList = []
    vehicleList = []
    counter = 1
    counter2 = 1
    deliveryOrPick = [1]
    capacity = [99999]
    duration = 300
#     print(deliveryList)
    for x in deliveryList:
        for y in x:
#             print(y["Act Ckpt Code"])
#             if(y["Act Ckpt Code"] == "ARRVD" or  y["Act Ckpt Code"] == "DEPAR"):
            if(y["Act Ckpt Code"]  == "DEPAR"): #just need to add one vehicle
                vehicleList.append(Vehicle(counter2,subangLocation,capacity, [] , timeWindow, subangLocation, y["Courier id"]))
                counter2+=1
            else:
#                 print(y)
#because the history actual time sometimes just does not fit in the range, so it will only be useful for new input
# getTimeWindow(y["Open"], y["Closed"])
                jobList.append(Job(counter,deliveryOrPick,[y["lgtd"], y["lat"]] , [], [timeWindow], duration , y["Street"]  if y["Street"] == y["Street"] else "street is blank"        ))
                counter+=1
    return jobList, vehicleList

def createDictionaryObjectJobsVehicles(jobsList : List,vehicleList : List ) -> dict:
    dict_t = {}
    dict_t["jobs"] = []
    for x in jobsList:
        dict_t["jobs"].append(x.__dict__)

    dict_t["vehicles"] = []
    for y in vehicleList:
        #test.append(json.dumps(x.__dict__))
        dict_t["vehicles"].append(y.__dict__)
    return dict_t

# Function to insert row in the dataframe 
def addRowToDataFrame(row_number, df, row_value): 
    # Slice the upper half of the dataframe 
    df1 = df[0:row_number] 
   
    # Store the result of lower half of the dataframe 
    df2 = df[row_number:] 
   
    # Inser the row in the upper half dataframe 
    df1.loc[row_number]=row_value 
   
    # Concat the two dataframes 
    df_result = pd.concat([df1, df2]) 
   
    # Reassign the index labels 
    df_result.index = [*range(df_result.shape[0])] 
   
    # Return the updated dataframe 
    return df_result 

def addJob(dataFrame,date,session ,street, actBase = "P", openend = "00:00", closed = "23:59"):
    from numpy import nan as Nan

    actDt = int(date)
    street = street
    
#     if(openend == None):
#         openend = "00:00"
#     if(closed == None):
#         closed = "00:00"
        
    dateArrival = date
    pickUpType = "REGULAR"
    deliveryType = "NORMAL"
    
    name = "name"
    
    pudSvcArea = "KUL"
    pudType = "pudType"
    actCkpyCode = "OK"
    awbBooking = "new ID " + str(( len(dataFrame) + 1 ))
    closed = closed
    openend = openend
    
    if(session == "m"):
        actTm = "09:01"
    else:
        actTm = "15:00"
    
    dateArrival = dateArrival
    weight = 0
    tPcs = 0
    parcelPcs = 0
    shpCnt = 0
    palletPcs = 0
    parcelP = 0
    proCode = "test"
    prodGrp = "testG"
    pickUpType = pickUpType
    actBase = actBase
    city = "123"
    zip = "zip"
    street = street
    customerName = name
    if(dataFrame.all != dataFrame.all):
        print("dataFrame is blank array")
    courierID = dataFrame.iloc[0]["Courier id"]
    pudCycle = "B"
    pudEac = "EAC"
#     actDt = None

    new = pd.DataFrame({'PUD Svc Area': [pudSvcArea], 
                     'PUD Fac': [pudEac],
                     'PUD Cycle': [pudCycle],
                      'Courier id':courierID,
                      'Courier Type':  np.nan,
                      'Customer Name': [customerName],
                      'Street': [street],
                      'zip': [zip],
                      'City': [city],
                      'Act Dt': actDt,
                      'Act Base': [actBase],
                      'Delivery Type': [deliveryType],
                      'Pickup Type': [pickUpType],
                      'Prod Grp': [prodGrp],
                      'Prod Code': [proCode],
                      'ShpCnt': [shpCnt],
                      'Pallets Pcs': [palletPcs],
                      'Parcel Pcs': [parcelP],
                      'Total Pcs': [tPcs],
                      'Weight': [weight],
                      'AR dtm': [dateArrival],
                      'Act Tm': [actTm],
                      'Open': [openend],
                      'Closed': [closed],
                      'lat':  pd.Series([np.nan]),
                      'lgtd':  pd.Series([np.nan]),
                      'awb_booking': [awbBooking],
                      'Act Ckpt Code': [actCkpyCode],
                      'PuD Type': [pudType],
                      'Stop Code':  pd.Series([np.nan]),
                    'MarkerColor':  pd.Series([np.nan]), })
    
#     print(new.iloc[0]["Act Dt"])
    
    partialDataFrame = dataFrame.loc[(dataFrame['Courier id'] == courierID) & (dataFrame["Act Dt"] == int(date)) & (dataFrame["Act Ckpt Code"] == "DEPAR")]
    
#     print(partialDataFrame.index)
#     print(type(new.iloc[0]["Open"]))
    dataFrame = addRowToDataFrame(partialDataFrame.index[0] + 1, dataFrame, new.iloc[0])
#     dataFrame = dataFrame.append(new, ignore_index=True)
    
    return dataFrame,awbBooking

def gotUnssigned(dict_t : dict) -> str:
    if(dict_t != None and (dict_t["code"] != 0) ):
        return(dict_t["error"])
    else:
        return dict_t["unassigned"]

    
def routeWithDateAndSession(date : str,  session: str, street: None ):

    # fullDataFrame = pd.read_csv("3.csv")
    fullDataFrame = pd.read_csv(csvPath)

    
    if(~(street != street)):
        fullDataFrame, newAwbBooking = addJob(fullDataFrame, date, session ,street)
    
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    partialDataFrame = fullDataFrame

    partialDataFrame = partialDataFrame.loc[partialDataFrame['Act Dt'] == int(date)]
#     partialDataFrame = partialDataFrame.sort_values('Courier id')
    #     fullDataFrame
    deliveryListRoute, fullDataFrame = getDeliveryRoute(partialDataFrame, fullDataFrame)
#     print(deliveryListRoute)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session))
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList )

#     pprint.pprint(dict_t)
    content = json.dumps(dict_t, cls=NpEncoder) 
#     write_file("content.json", content)

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=open("content.json", 'rb'), headers=headers)    
    
    #record the response to file
    # json_file_name = saveRecordToDataBase(date, session)
    # deleteRecordToDataBase(date, session)
#     write_file(json_file_name, r.content)


    text_file = open(json_file_name, "wb")
    n = text_file.write(r.content )
    text_file.close()
    
#     #update the added job to csv
    fullDataFrame.to_csv(csvPath, index=False)
    
#     print(len(fullDataFrame))
#     print(partialDataFrame)
    return r

# r =routeWithDateAndSession(date, session, "Jalan Rumbia, Kampung Seberang Paya, 11900 Bayan Lepas, Pulau Pinang")
            
def getDictFromResponse(responseFileName : str) -> dict:
    with open(responseFileName) as f:
        if(os.stat(responseFileName).st_size == 0):
            dict_t = None
        else: 
            dict_t = json.load(f)
    return dict_t

def tryGotUnassignedInResponse(date : str,  session: str, street: None, unassignedJob =None ):

    fullDataFrame = pd.read_csv(csvPath)
    if(~(street != street)):
        fullDataFrame, newAwbBooking = addJob(fullDataFrame, date, session, street)
    
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    partialDataFrame = fullDataFrame
    partialDataFrame = partialDataFrame.loc[partialDataFrame['Act Dt'] == int(date)]

    deliveryListRoute, fullDataFrame = getDeliveryRoute(partialDataFrame, fullDataFrame, session)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session))
    
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList )
    print(len(deliveryListRoute))
    content = json.dumps(dict_t, cls=NpEncoder) 
    # write_file("tmp/content.json", content)

    gcloudWriteFile("content.json", content, "w")

    data = gcloudReadFile(filename)

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    # r = requests.post(url, data=open("tmp/content.json", 'rb'), headers=headers)    
    r = requests.post(url, data=open(data, 'rb'), headers=headers)    
    
    # text_file = open(getResponseFileName(date, session), "wb")
    # n = text_file.write(r.content )
    # text_file.close()
    gcloudWriteFile(getResponseFileName(date, session), r.content, "wb")
    
def tryGotUnassignedInResponse2(date : str,  session: str, street: None, unassignedJob =None ):
    
    client = storage.Client()
    bucket = client.get_bucket('real-bucket-dhl')

    fullDataFrame = pd.read_csv('gs://real-bucket-dhl/3.csv')

    # fullDataFrame = pd.read_csv(csvPath)
    if(~(street != street)):
        fullDataFrame, newAwbBooking = addJob(fullDataFrame, date, session, street)
    
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    partialDataFrame = fullDataFrame
    partialDataFrame = partialDataFrame.loc[partialDataFrame['Act Dt'] == int(date)]

    deliveryListRoute, fullDataFrame = getDeliveryRoute(partialDataFrame, fullDataFrame, session)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session))
    
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList )
    print(len(deliveryListRoute))
    content = json.dumps(dict_t, cls=NpEncoder) 
    # write_file("tmp/content.json", content)

    # gcloudWriteFile("content.json", content, "w")

    # data = gcloudReadFile(filename)

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    # r = requests.post(url, data=open("tmp/content.json", 'rb'), headers=headers)    
    r = requests.post(url, data=content, headers=headers)    
    
    # text_file = open(getResponseFileName(date, session), "wb")
    # n = text_file.write(r.content )
    # text_file.close()
    # gcloudWriteFile(getResponseFileName(date, session), r.content, "wb")
    
    
#     #update the added job to csv
    newJobDataFrame = fullDataFrame.loc[(fullDataFrame["awb_booking"] == newAwbBooking)]

#     #temp fix
    fullDataFrame.at[newJobDataFrame.index[0], "Courier Type"] = "NON_GCA5"


    string = fullDataFrame.to_csv(None, index=False)

    blob = bucket.blob("3.csv")

    blob.upload_from_string(string, "application/vnd.ms-excel")

    # fullDataFrame.to_csv(csvPath, index=False)
    
    #true mean no unassigned, false mean got error or the location can not fit.

    # dict_t = gcloudReadFile(getResponseFileName(date, session))

    # dict_t = getDictFromResponse(getResponseFileName(date, session))
    # dict_t = json.load(r.content)

    dict_t = json.loads(r.content)

    responseDict = gotUnssigned(dict_t)

#     print(dict_t)
    print(responseDict == [])#
#     print(content)
    return dict_t

# # print(tryGotUnassignedInResponse(date,session,street))
# # morningData = tryGotUnassignedInResponse(date,session,street)
# # print(morningData)    
# #     #update the added job to csv
#     newJobDataFrame = fullDataFrame.loc[(fullDataFrame["awb_booking"] == newAwbBooking)]

# #     #temp fix
#     fullDataFrame.at[newJobDataFrame.index[0], "Courier Type"] = "NON_GCA5"
#     fullDataFrame.to_csv(csvPath, index=False)
    
#     #true mean no unassigned, false mean got error or the location can not fit.

#     dict_t = gcloudReadFile(getResponseFileName(date, session))

#     # dict_t = getDictFromResponse(getResponseFileName(date, session))
#     responseDict = gotUnssigned(dict_t)

# #     print(dict_t)
#     print(responseDict == [])#
# #     print(content)
#     return dict_t

# print(tryGotUnassignedInResponse(date,session,street))
# morningData = tryGotUnassignedInResponse(date,session,street)
# print(morningData)


import datetime

from flask import Flask, render_template

# [START gae_python37_datastore_store_and_fetch_times]


# [END gae_python37_datastore_store_and_fetch_times]
app = Flask(__name__)

# morningData = tryGotUnassignedInResponse2(date,session,street)


# [START gae_python37_datastore_render_times]
@app.route('/')
def start():
    # morningData = tryGotUnassignedInResponse(date,session,street)
    print("start")
    return "Hello"
# def root():

@app.route('/try')
def tryReturn():
    # date = "20200204"
    # session = "m"
    # street = "Jalan Rumbia, Kampung Seberang Paya, 11900 Bayan Lepas, Pulau Pinang"
# example
# http://127.0.0.1:8080/try?date=20200204&session=m&street=Bj%20Court%20Condominium,%20Kampung%20Seberang%20Paya,%2011900%20Bayan%20Lepas,%20Pulau%20Pinang
    from flask import request
    date  = request.args.get('date')
    session = request.args.get('session')
    street = request.args.get('street')

    # street = "Bj Court Condominium, Kampung Seberang Paya, 11900 Bayan Lepas, Pulau Pinang"
    morningData = tryGotUnassignedInResponse2(date,session,street)
    return morningData
    # print(type(date))
    # return street

# [END gae_python37_datastore_render_times]


@app.route('/openFile')
def openFile():
    from flask import Flask
    from io import StringIO
    from flask import jsonify
    client = storage.Client()
    bucket = client.get_bucket('real-bucket-dhl')
    
    blob = bucket.get_blob('3.csv')
    your_file_contents = blob.download_as_string()

    # df = pd.read_csv(StringIO(your_file_contents))
    df = pd.read_csv('gs://real-bucket-dhl/3.csv')

    # fullDataFrame = pd.read_csv(blob)
    # return your_file_contents
    # print(df.iloc[0]["Courier id"])

    return jsonify(df.iloc[0]["Courier id"])

@app.route('/uploadfile')
def upload_blob():
    client = storage.Client()
    bucket = client.get_bucket("real-bucket-dhl")
    
    # fullDataFrame = pd.read_csv(csvPath)
    df = pd.read_csv('gs://real-bucket-dhl/3.csv')
    string = df.to_csv(None, index=False)

    blob = bucket.blob("3.csv")

    blob.upload_from_string(string, "application/vnd.ms-excel")

@app.route('/test')
def another_function():

    from flask import request
    a  = request.args.get('first')
    b = request.args.get('second')
    return a + b


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
