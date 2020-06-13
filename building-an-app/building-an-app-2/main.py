#global param, config

bucketName = "real-bucket-dhl"
bucketTempName = "real-bucket-dhl-temp"
csvPath = "3.csv"
gStorage = 'gs://real-bucket-dhl/3.csv'
optimalCsvName = "optimalRoutes.csv"
optimalCsvPath = "files/february/" + optimalCsvName
gStorageOptimalCsv = "gs://real-bucket-dhl/files/february/" + optimalCsvName
url = 'http://35.213.166.175:3000' #vroomRoute

date = "20200204"
session = "a"
street = "Jalan Rumbia, Kampung Seberang Paya, 11900 Bayan Lepas, Pulau Pinang"

defaultZip = 99
defaultCapacity = 99999

mode = "noCloud"
morningStart = "08:45:00"
morningEnd = "13:59:59"

afternoonStart = "14:00:00"
afternoonEnd = "20:00:00"

useZip = False
customCapacity = True

import re
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

from datetime import date, timedelta

import json

import pprint

 
import os
# import pymysql
import pandas as pd

import logging
import os
from google.cloud import storage

# when use flask open back
# from flask import Flask
from io import StringIO
# from flask import jsonifyaf


# datastore_client = datastore.Client()


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



# real-bucket-dhl/files/february/day/x/session/fileType
def getResponseFileName(date : str, session : str )-> str:
#     from pathlib import Path

#     path = Path(__file__).parent / "../data/test.csv"
#     return "files/february/" + getDayFromInputDay(str(date)) + "/input.json"
    return "files/february/response/" + str(date) + "-" + session + "-response.json"

def getInputeForResponseFileName(date: str, sesison: str) -> str:
    return "files/february/input/" + str(date) + "-" + session  + "-input.json"

# def getResponseCsvFilePath(date: str, session : str) -> str:
#     return "files/february/response/day/" + getDayFromInputDay(str(date))
def getDayFromInputDay(date: str) -> str:
    return date[-2:]
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
    if(len(time_str.split(':')) ==3  ):
        h, m,s = time_str.split(':')
    else:
        print(len(time_str.split(':')))
        print(time_str)
        h, m = time_str.split(':')
        s= "00"
    
    return int(h) * 3600   + int(m) * 60 + int(s)

def getTimeWindow(start : float ,end : float) -> List:
    if(start != start ):
        start = "00:00:00"
#     if(end == "23:59"):
#         end = "20:00"
    if(end != end):
        end = "23:59:00"
    return [ getMiliSec(start), getMiliSec(end) ]

def getTime24hour(seconds : int):
    import datetime
    return str(datetime.timedelta(seconds=seconds))
    
def sendRequest(fileName : str):

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

def getDeliveryRoute(partialDataFrame : List, fullDataFrame : List, session : str):
#     print("DASDASDDASDSDSDASDS")
    deliveryList = []
    deliveryListRoute=[]
    
    arraySearched = []
#     print(len(partialDataFrame))
#     for x in range(0, len(partialDataFrame)):
    for index, x in partialDataFrame.iterrows():
        valid = False
        if(x["Act Ckpt Code"] ==  "DEPAR" or x["Act Ckpt Code"]==  "ARRVD"):
#             valid = True
            
            if(x["Act Ckpt Code"] == "DEPAR"):
            
                subFrame = partialDataFrame.loc[partialDataFrame["Courier id"] == x["Courier id"]]
                subFrame.reset_index(inplace=True)
                arraySearched.append(x["Courier id"])

                countArraySearched = arraySearched.count(x["Courier id"])
                departTime = None
                arrivalTime = None
                counterLoop = 0
                indexFirst = subFrame.index[0]
                for index2, k in subFrame.iterrows():
                    if(counterLoop < countArraySearched):
                        if(k["Act Ckpt Code"] == "DEPAR"):
                            if(index2 != indexFirst):
                                if(subFrame.iloc[index2-1]["Act Ckpt Code"] != "ARRVD"):
                                    arrivalTime = None
                                    departTime = getMiliSec(k["Act Tm"])
                            else:
                                departTime = getMiliSec(k["Act Tm"])

                        if(k["Act Ckpt Code"] == "ARRVD"):
                            arrivalTime = getMiliSec(k["Act Tm"])
                            counterLoop+=1
                    else:
                        break

                if(session == "m"):
                    if(arrivalTime != None):
                        if( (departTime > getMiliSec(morningStart))  | ( arrivalTime > getMiliSec(morningEnd) ) ):
                            valid = True
                    elif((departTime > getMiliSec(morningStart)) & (departTime < getMiliSec(afternoonStart) ) ):
                            valid = True
                    else:
                        valid = False
                        print("unknow prepare sitaution 5")
                elif(session =="a"):
                    if(arrivalTime != None):
                        if( (departTime > getMiliSec(afternoonStart))  | ( arrivalTime < getMiliSec(afternoonEnd) )):
                            valid = True
                    elif(departTime > getMiliSec(afternoonStart) ):
                        valid = True
                    else:
                        valid = False
                        print("unknow prepare sitaution 6")
                else:
                    print("session error")
            
            if(deliveryListRoute != []):
                deliveryList.append(deliveryListRoute)
                deliveryListRoute = []
            else:
                deliveryListRoute = []
        else:
#             if(valid):
            #logic for morning afternoon
            if( (session == "m") & (getMiliSec(x["Act Tm"]) > getMiliSec(morningStart) ) & (getMiliSec(x["Act Tm"]) < getMiliSec(morningEnd) ) ):
                valid = True
            elif( (session == "a") & (getMiliSec(x["Act Tm"]) > getMiliSec(afternoonStart) ) & (getMiliSec(x["Act Tm"]) < getMiliSec(afternoonEnd)  ) ) :
                valid = True
            else: #false for afternoon session first
                valid = False
            if(valid):
                if(x["lgtd"] != x["lgtd"] or x["lat"] != x["lat"]): # lat or long None
                    
                    if(mode == "noCloud"):
                        print("trigger no cloud geocode . . .")
                        lat = 2.7047421
                        lgtd = 101.9168708
                    else:
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

def getSessionWithTimeWindowMSec(start : int, end : int):
    timeWindowM = getTimeWindow(morningStart,  morningEnd )
    timeWindowA = getTimeWindow(afternoonStart,  afternoonEnd )
    if(start >= timeWindowM[0] and end <= timeWindowM[1]):
        session = "m"
    elif(start >= timeWindowA[0] and end <= timeWindowA[1]):
        session = "a"
    else:
        session = "asdas"
    return session

def getSessionWithTimeWindow(start: str, end: str) -> str:
    start, end = getTimeWindow(start, end)
    timeWindowM = getTimeWindow(morningStart,  morningEnd )
    timeWindowA = getTimeWindow(afternoonStart,  afternoonEnd )
    if(start >= timeWindowM[0] and end <= timeWindowM[1]):
        session = "m"
    elif(start >= timeWindowA[0] and end <= timeWindowA[1]):
        session = "a"
    else:
        session = "asdas"
    return session

    
def getTimeWindowWithSession(session : str) -> List:
    if(session == "m"):
#         timeWindow = getTimeWindow("09:00",  "18:45" )
#         timeWindow = getTimeWindow("09:00",  "13:45" )
        timeWindow = getTimeWindow(morningStart,  morningEnd )

    elif(session =="a"):
        timeWindow = getTimeWindow(afternoonStart,  afternoonEnd )
#         timeWindow = getTimeWindow("09:00",  "18:45" )

    else:
        print("undefined session")
        timeWindow = getTimeWindow("09:00:00",  "13:00:00" ) #default morning
        
    return timeWindow
    
def isNotNull(var):
    return var == var
def createJobsAndVehiclesList(deliveryList : List, timeWindow : List, zipSet :List):
    subangLocation = [101.9381 ,2.7297] #should be seremban
    jobList = []
    vehicleList = []
#     counter = 1
#     counter2 = 1
    deliveryOrPick = [1]
    duration = 300
#     print(deliveryList)
    for x in deliveryList:
        for y in x:
#             print(y["Act Ckpt Code"])
#             if(y["Act Ckpt Code"] == "ARRVD" or  y["Act Ckpt Code"] == "DEPAR"):
            if(y["Act Ckpt Code"]  == "DEPAR"): #just need to add one vehicle
                if(useZip):
                    vehicleList.append(Vehicle(y["id"],subangLocation, defaultCapacity, list(zipSet[y["Courier id"]]) + [defaultZip] , timeWindow, subangLocation, y["Courier id"]))
                else:
                    vehicleList.append(Vehicle(y["id"],subangLocation, defaultCapacity, [] , timeWindow, subangLocation, y["Courier id"]))

            #                 counter2+=1
            else:
                if(y["Act Ckpt Code"]  != "ARRVD"): 
    #                 print(y)
    #because the history actual time sometimes just does not fit in the range, so it will only be useful for new input
    # getTimeWindow(y["Open"], y["Closed"])
                    if(useZip):
                        jobList.append(Job(y["id"],deliveryOrPick,[y["lgtd"], y["lat"]] , [int(y["zip"])] if y["zip"] == y["zip"] else [defaultZip], [timeWindow], duration , y["Street"]  if y["Street"] == y["Street"] else "street is blank"        ))
                    else:
                        jobList.append(Job(y["id"],deliveryOrPick,[y["lgtd"], y["lat"]] , [], [timeWindow], duration , y["Street"]  if y["Street"] == y["Street"] else "street is blank"        ))
    #                 counter+=
    return jobList, vehicleList

def createDictionaryObjectJobsVehicles(jobsList : List,vehicleList : List) -> dict:
    dict_t = {}
    dict_t["jobs"] = []
    jobCounter = 0
    for x in jobsList:
        dict_t["jobs"].append(x.__dict__)
        jobCounter = jobCounter + 1

    dict_t["vehicles"] = []
    capacity = [  int (round(jobCounter/ len(vehicleList)) * 120 / 100 ) ]
    print("capacity : "  + str(capacity))
    for y in vehicleList:
        if(customCapacity):
#         y.capacity = [ round(jobCounter/ len(vehicleList)) + 1]
            y.capacity = capacity
#         y.capacity = [ round(jobCounter/ len(vehicleList))]

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

def addJob(dataFrame,date,session ,street, actBase = "P", openend = "00:00:00", closed = "23:59:00"):
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
    id = len(dataFrame) + 1
    awbBooking = session + "_" + str(id)
    closed = closed
    openend = openend
    
    
    if(session == "m"):
        actTm = "09:01:00"
    else:
        actTm = "15:00:00"
    
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
    zip = "11111"
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
                        'id' : [id],
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

    
def routeWithDateAndSession(date : str,  session: str, street: None):

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

def getRouteIndexWithID(readed : dict, jobID :id)-> dict:
    for indexRoute, routes in enumerate( readed["routes"] , start = 0): 
        for indexStep, step in enumerate( routes["steps"], start = 1):
                if(step["type"] == "job"):
                    if(step["job"] == jobID):
                        return indexStep, indexRoute
    
    return [],[]
#     return 1,2,indexRoute

def getLocationsAscendingFromRoute(routes : dict, index :int):
    locations = []
    for step in routes["steps"]:
        locations.append(step["location"])
    return locations

def getRouteDetailWithIDk(ID):
    readed = getResponseFileAsDict()    
    indexStep, indexRoute = getRouteIndexWithID(readed, ID)
    if(indexStep == [] or indexRoute == []) :
        return [],[],[]
    else:
        locations = getLocationsAscendingFromRoute(readed["routes"][indexRoute], indexStep)
        idLocation = locations[indexStep]
        vehicleID = getRouteVehicleID(readed["routes"], indexRoute)

        return readed["routes"][indexRoute], indexStep, vehicleID

def getRouteVehicleID(routes, index):
    return routes[index]["vehicle"]

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

def getResponseFileAsDict():
    import ndjson
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    blob = bucket.get_blob(getResponseFileName(date,session))s
    json_data_bytes = blob.download_as_string()
    dict_t = json.loads(json_data_bytes)
    return dict_t

def checkGFileExists(fileName : str, bucketName = bucketName) -> bool:
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
#     name = 'files/february/optimalRoutes.csv'
#     name = "files/february/response/20200204-a-447-response.json"
    return storage.Blob(bucket=bucket, name=fileName).exists(client)

def handleOptimalRoute(dataFrame, columns):
    from datetime import datetime
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    gStorageOptimalCsv = 'gs://real-bucket-dhl/files/february/optimalRoutes.csv'
    csvFilePathName = 'files/february/optimalRoutes.csv'
    historyFilePath = 'files/february/removed/'

#     csv = 
#     string = fullDataFrame.to_csv(None, index=False)
    
    if (not checkGFileExists(csvFilePathName)):
        string = dataFrame.to_csv(None, index=False)
        blob = bucket.blob(csvFilePathName)
        blob.upload_from_string(string, "application/vnd.ms-excel")
        print("create new optimal route csv")
#     create new csv
    else:
        print("update optimal route csv")
        oldDataFrame = pd.read_csv(gStorageOptimalCsv)
        #check this partial inside this csv
        batchID = dataFrame.iloc[0]["batchID"]
        foundPartialDataFrame = oldDataFrame.loc[oldDataFrame["batchID"] == batchID]
        
        if(not foundPartialDataFrame.empty):
            string = foundPartialDataFrame.to_csv(None, index=False)
            #store this to change data to history
            date_time = datetime.now().strftime("%m_%d_%Y, %H:%M:%S")
            blob = bucket.blob(historyFilePath + date_time + "--" +str(batchID) +".csv" )
            blob.upload_from_string(string, "application/vnd.ms-excel")
        
        #update the csv
            oldDataFrame = oldDataFrame.drop(oldDataFrame.index[foundPartialDataFrame.index.to_list()])
#             oldDataFrame = oldDataFrame.drop(oldDataFrame.index[foundPartialDataFrame.index.to_list()])
        
        
        newDataFrame = pd.concat([oldDataFrame,dataFrame])
        newDataFrame.reset_index()
        string = newDataFrame.to_csv(None, index=False, columns = columns)
        blob = bucket.blob(csvFilePathName)
        blob.upload_from_string(string, "application/vnd.ms-excel")

def getSingleRouteFromRoutes(routes : dict) -> dict:
    singleRoute = routes.copy()
    singleRoute["routes"] = [routes["routes"][0]]
    singleRoute["summary"]["distance"] = routes["routes"][0]["distance"]
    singleRoute["summary"]["duration"] = routes["routes"][0]["duration"]
    singleRoute["summary"]["service"] = routes["routes"][0]["service"]
    singleRoute["summary"]["cost"] = routes["routes"][0]["cost"]
    singleRoute["summary"]["delivery"] = [routes["routes"][0]["delivery"]]
    singleRoute["summary"]["amount"] = [routes["routes"][0]["amount"]]
    return singleRoute
        
def processRoutedResponse(fullDataFrame, dict_t, session):
    
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    for routes in dict_t["routes"]:
        df = pd.DataFrame()
        vehicleInformation = fullDataFrame.loc[fullDataFrame['id'] == routes["vehicle"]].iloc[0]
#         vehicleInformation = fullDataFrame.loc[fullDataFrame['id'] == routes["vehicle"]]
        actCkptCode = vehicleInformation["Act Ckpt Code"]
#         actCkptCode = vehicleInformation["Act Ckpt Code"].values[0]
        vehicleInformation['id'] = vehicleInformation['id'].astype("int")
        vehicleInformation['id'] = vehicleInformation['id'].astype("str")
        vehicleID = vehicleInformation['id']

        date = int(vehicleInformation["Act Dt"])
        name = vehicleInformation["Courier id"]
        routes["steps"][0]["name"] = vehicleInformation["Courier id"]
        singleRoute = getSingleRouteFromRoutes(dict_t)

        content = json.dumps(singleRoute, cls=NpEncoder) 
        blob = bucket.blob("files/february/response/"+ str(date) +  "-" + session  + "-" + vehicleID + "-response.json")
        blob.upload_from_string(content, "application/json")
        print("created json file")
        
        for indexStep, step in enumerate( routes["steps"], start = 1):
            if(step["type"] == "start" or step["type"] == "end"):
                startingInformation = vehicleInformation.copy()
                startingInformation["Act Tm"] = getTime24hour(step["arrival"])
                startingInformation["batchID"] = str(date) +  "-" + session  + "-" + str(vehicleID)
                startingInformation["id"] = str(startingInformation["id"])

                if(step["type"] == "end"):
    #                 startingInformation.at[startingInformation.index[0], "id"] = str(startingInformation["id"].values[0]) + "arrvd"
#                     startingInformation.at[startingInformation.index[0], "Act Ckpt Code"] = "ARRVD"
                    startingInformation["Act Ckpt Code"] = "ARRVD"
                elif(step["type"] == "start"):
                     startingInformation["Act Ckpt Code"] = "DEPAR"
                else:
                    print("unprepare situation 3")
                    print("actCkptCode : " + actCkptCode)
                df = df.append(startingInformation)
            elif(step["type"] == "job"):
                jobInformation = fullDataFrame.loc[fullDataFrame['id'] == int(step["job"])]
                if(jobInformation["Street"].values[0] == jobInformation["Street"].values[0]):
                    string = jobInformation["Street"].values[0]
                    description = re.sub('\s+', ' ', string)
                    step["description"] = description

                else:
                    step["description"] = "Street is blank"
                new = pd.DataFrame({'PUD Svc Area': [vehicleInformation["PUD Svc Area"]], 
                         'PUD Fac': [vehicleInformation["PUD Fac"]],
                         'PUD Rte': [vehicleInformation["PUD Rte"]],          
                         'PUD Cycle': [vehicleInformation["PUD Cycle"]],
                          'Courier id':[vehicleInformation["Courier id"]],
                          'Courier Type':  [vehicleInformation["Courier Type"]],
                          'Customer Name': [jobInformation["Customer Name"].values[0]],
                          'Street': [jobInformation["Street"].values[0]],
                          'zip': [jobInformation["zip"].values[0]],
                          'City': [jobInformation["City"].values[0]],
                          'Act Dt': [jobInformation["Act Dt"].values[0]],
                          'Act Base': [jobInformation["Act Base"].values[0]],
                          'Delivery Type': [jobInformation["Delivery Type"].values[0]],
                          'Pickup Type': [jobInformation["Pickup Type"].values[0]],
                          'Prod Grp': [jobInformation["Prod Grp"].values[0]],
                          'Prod Code': [jobInformation["Prod Code"].values[0]],
                          'ShpCnt': [jobInformation["ShpCnt"].values[0]],
                          'Pallets Pcs': [jobInformation["Pallets Pcs"].values[0]],
                          'Parcel Pcs': [jobInformation["Parcel Pcs"].values[0]],
                          'Total Pcs': [jobInformation["Total Pcs"].values[0]],
                          'Weight': [jobInformation["Weight"].values[0]],
                          'AR dtm': [jobInformation["AR dtm"].values[0]],
                          'Act Tm': [getTime24hour(step["arrival"])],
                          'Open': [jobInformation["Open"].values[0]],
                          'Closed': [jobInformation["Closed"].values[0]],
                          'lat':  [step["location"][1]],
                          'lgtd':  [step["location"][0]],
                          'awb_booking': [jobInformation["awb_booking"].values[0]],
                          'Act Ckpt Code': [jobInformation["Act Ckpt Code"].values[0]],
                          'PuD Type': [jobInformation["PuD Type"].values[0]],
                          'Stop Code':  [jobInformation["Stop Code"].values[0]],
                         'MarkerColor':  [jobInformation["MarkerColor"].values[0]], 
                         'id' : [str(step["job"])],
                         'batchID' : [str(date) +  "-" + session  + "-" + str(vehicleID)],
                                   })
#                 print(new)
                columns =["PUD Svc Area","PUD Fac","PUD Rte","PUD Cycle","Courier id","Courier Type","Customer Name","Street","zip","City","Act Dt","Act Base","Delivery Type","Pickup Type","Prod Grp","Prod Code","ShpCnt","Pallets Pcs","Parcel Pcs","Total Pcs","Weight","AR dtm","Act Tm","Open","Closed","lat","lgtd","awb_booking","Act Ckpt Code","PuD Type","Stop Code","MarkerColor","id","batchID"]
#                 df = df[]]
                df = df.append(new)
            else:
                print("unprepare situation 1")
         #last record = end
        timeIntervalMorning = getTimeWindowWithSession("m")
        timeIntervalAfternoon = getTimeWindowWithSession("a")
    #     session = "aaa"
    #     getMiliSec(x["Act Tm"]) > getMiliSec("14:00:00") ) & (getMiliSec(x["Act Tm"]) < getMiliSec("23:59:00")  
    #     print(getMiliSec(df.iloc[-1]["Act Tm"]))
    #     print(getMiliSec(timeIntervalMorning[0]))
    #     print(type(getMiliSec(timeIntervalMorning[0])))

    #     if(getMiliSec(df.iloc[-1]["Act Tm"]) > timeIntervalMorning[0] and getMiliSec(df.iloc[-1]["Act Tm"]) <= timeIntervalMorning[1]):
    #         session = "m"
    #         print("afternoon")
    #     elif(getMiliSec(df.iloc[-1]["Act Tm"]) > timeIntervalAfternoon[0] and getMiliSec(df.iloc[-1]["Act Tm"]) <= timeIntervalAfternoon[1]):
    #         session = "a"
    #         print("morning")
    #     else:
    #         print("unprepare situation 2")

        
        
        string = df.to_csv(None, index=False, columns = columns)
        blob = bucket.blob("files/february/response/"+ str(date) +  "-" + session  + "-" + vehicleID + ".csv")
#         print("files/february/response/"+ str(date) +  "-" + session  + "-" + str(vehicleInformation['id']) + ".csv" )
#         print(str(vehicleInformation['id'].astype("int")) + ".csv" )

        blob.upload_from_string(string, "application/vnd.ms-excel")

#         df.to_csv("routes/"+ str(date) + "/" +session  + "/" + str(name) + ".csv", index=False)
        print("created csv file . . ..")
#         print(df)
        handleOptimalRoute(df, columns)

    blob = bucket.blob(getInputeForResponseFileName(date,session))
    content = json.dumps(dict_t, cls=NpEncoder) #the processed routes
    blob.upload_from_string(content, "application/json")
    print("created updated response json file")

def tryGotUnassignedInResponse2(date : str,  session: str, street: None, unassignedJob =None ):
    
    client = storage.Client()
    bucket = client.get_bucket(bucketName)

    fullDataFrame = pd.read_csv(gStorage)
    tempLen = len(fullDataFrame)
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    tempLen2 = len(fullDataFrame)
    if(tempLen> tempLen2):
        fullDataFrame.reset_index()
    #initial id column
    if 'id' not in fullDataFrame .columns:
        fullDataFrame["id"] = fullDataFrame.index+1
    
    # fullDataFrame = pd.read_csv(csvPath)
    
#     if(street == street):
#         fullDataFrame, newAwbBooking = addJob(fullDataFrame, date, session, street)

    courierAndZip = fullDataFrame[["Courier id", "zip"]]
    courierAndZip = courierAndZip[fullDataFrame['zip'].notna()]
    courierAndZip = courierAndZip[courierAndZip["zip"].astype(str).str.isdigit()] 
    zipSet = courierAndZip.groupby(["Courier id"])["zip"].aggregate(lambda x: set(map(int, x)))
    partialDataFrame = fullDataFrame
    partialDataFrame = partialDataFrame.loc[partialDataFrame['Act Dt'] == int(date)]
    deliveryListRoute, fullDataFrame = getDeliveryRoute(partialDataFrame, fullDataFrame, session)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session), zipSet)
    
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList)
    print(len(deliveryListRoute))
#     print(deliveryListRoute)
#     print( dict_t)
#     print(vehicleList[0].time_window)

    content = json.dumps(dict_t, cls=NpEncoder) 
    
    blob = bucket.blob(getInputeForResponseFileName(date,session))

    blob.upload_from_string(content, "application/json")

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=content, headers=headers)    
    
    if (r.status_code != 200) :
        print ("Error request code : ")
        print(r.status_code)
        print(r.content)
#         print(dict_t)
    
    else:
#         blob = bucket.blob(getResponseFileName(date, session))

#         blob.upload_from_string(r.content, "application/json")
        dict_t = json.loads(r.content)
        processRoutedResponse(fullDataFrame, dict_t, session)
        
    #     #update the added job to csv
#         newJobDataFrame = fullDataFrame.loc[(fullDataFrame["awb_booking"] == newAwbBooking)]
# 
    #     #temp fix
#         fullDataFrame.at[newJobDataFrame.index[0], "Courier Type"] = "NON_GCA5"

        string = fullDataFrame.to_csv(None, index=False)

        blob = bucket.blob(csvPath)

        blob.upload_from_string(string, "application/vnd.ms-excel")

        dict_t = json.loads(r.content)
#         dict_t["extra"] = {}

#         dict_t["extra"]["awb_booking"] = newAwbBooking

        responseDict = gotUnssigned(dict_t)

#     print(dict_t)
    # print(responseDict == [])#
#     print(content)
    return dict_t

def uploadFile(fileName, content, bucketName = bucketName):
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    
    blob = bucket.blob(fileName)
    name, extensionName = fileName.split(".")
    if(extensionName == "csv"):
        print("csv upload")
#         string = fullDataFrame.to_csv(None, index=False)
        blob.upload_from_string(content, "application/vnd.ms-excel")
    elif(extensionName == "json"):
        blob.upload_from_string(content, "application/json")
    else: 
        print("file not support by this function yet")
    
#api part for chen wei
def getRoutedGeocode(rowID : int) -> list:
    df = pd.read_csv(gStorageOptimalCsv)
    job = df.loc[df["id"].astype('int') == rowID]
    if(job.empty):
        return "rowID not find"
    else:
        jobs = df.loc[df["batchID"] == job["batchID"].values[0] ]
        if(jobs.empty):
            return "contact admin"
        else:
            return jobs["lat"].to_list(), jobs["lgtd"].to_list()

def getETAByID(rowID : int) -> str:
    df = pd.read_csv(gStorageOptimalCsv)
    job = df.loc[df["id"].astype('int') == rowID]
    if(job.empty):
        return "rowID not find"
    else:
        return job["Act Tm"].values[0]

def makeTempDataFrameRow(df):
    df["Courier Type"] = "NON_GCA5"
    return df
    
def changeTime(rowID : int, start: str, end : str ) -> list:
    df = pd.read_csv(gStorageOptimalCsv)
    dfJob=df.loc[df["id"].astype('int') == rowID]
#     print(len(dfJob))
    fullDataFrame = pd.read_csv(gStorage)
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    if(dfJob.empty):
        return "rowID not find"
    session = getSessionWithTimeWindow(start, end)
    print(session)
    if(session not in ["m", "a"]):
        return "time interval error"

    courierAndZip = fullDataFrame[["Courier id", "zip"]]
    courierAndZip = courierAndZip[fullDataFrame['zip'].notna()]
    courierAndZip = courierAndZip[courierAndZip["zip"].astype(str).str.isdigit()] 
    zipSet = courierAndZip.groupby(["Courier id"])["zip"].aggregate(lambda x: set(map(int, x)))
    partialDataFrame = df
    partialDataFrame = partialDataFrame.loc[partialDataFrame['batchID'] == dfJob["batchID"].values[0]]
    deliveryListRoute, df = getDeliveryRoute(partialDataFrame, df, session)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session), zipSet)
    for job in jobsList:
        if(job.id == rowID):
            job.time_windows = [getTimeWindow(start, end)]
            break
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList)
    content = json.dumps(dict_t, cls=NpEncoder) 
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=content, headers=headers)    
    
    if (r.status_code != 200) :
        print ("Error request code : ")
        print(r.status_code)
        print(r.content)
        return "routing server error"
    
    else:
        dict_t = json.loads(r.content)
        if(dict_t["summary"]["unassigned"] > 0):
            return "could not fit the time range"
        else:
            print("here")
            temp = dfJob.copy()
            temp["Open"] = start
            temp["Closed"] = end
            temp["Courier Type"] = "NON_GCA5"
            df = addRowToDataFrame(dfJob.index[0] + 1, df, temp.iloc[0])
            uploadFile(optimalCsvPath ,df.to_csv(None, index=False))
#             uploadFile(dfJob["batchID"].values[0] + "-temp"+ str(job["id"].values[0]) +"-response.json", r.content, bucketTempName)
            return "possible, update with id " + str(rowID)

def confirmChangeTime(rowID : str):
    from time import strftime
    from time import gmtime    
    df = pd.read_csv(gStorageOptimalCsv)
    dfJob = df.loc[df["id"].astype('int') == rowID]
    if(dfJob.empty):
        return "id not found"
    tempJob = df.loc[(df["id"].astype('int') == rowID) & (df["Courier Type"] == "NON_GCA5" )]
    
    tempJob["Courier Type"] =  dfJob["Courier Type"]
    df = df.drop(dfJob.index[0])
    start = tempJob["Open"].values[0]
    end = tempJob["Closed"].values[0]
    session = getSessionWithTimeWindow(start,end)
    

    
    fullDataFrame = pd.read_csv(gStorage)
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    if(session not in ["m", "a"]):
        return "time interval error"
    
    courierAndZip = fullDataFrame[["Courier id", "zip"]]
    courierAndZip = courierAndZip[fullDataFrame['zip'].notna()]
    courierAndZip = courierAndZip[courierAndZip["zip"].astype(str).str.isdigit()] 
    zipSet = courierAndZip.groupby(["Courier id"])["zip"].aggregate(lambda x: set(map(int, x)))
    partialDataFrame = df
    partialDataFrame = partialDataFrame.loc[partialDataFrame['batchID'] == dfJob["batchID"].values[0]]
    deliveryListRoute, df = getDeliveryRoute(partialDataFrame, df, session)
    jobsList, vehicleList = createJobsAndVehiclesList(deliveryListRoute, getTimeWindowWithSession(session), zipSet)
    for job in jobsList:
        if(job.id == rowID):
            job.time_windows = [getTimeWindow(start, end)]
            break
    dict_t = createDictionaryObjectJobsVehicles(jobsList,vehicleList)
    content = json.dumps(dict_t, cls=NpEncoder) 
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=content, headers=headers)    
    
    if (r.status_code != 200) :
        print ("Error request code : ")
        print(r.status_code)
        print(r.content)
    
    else:
        dict_t = json.loads(r.content)
        if(dict_t["summary"]["unassigned"] > 0):
            return "could not fit the time range"
        else:
            uploadFile(optimalCsvPath ,df.to_csv(None, index=False))
            uploadFile(dfJob["batchID"].values[0] + "-temp"+ str(dfJob["id"].values[0]) +"-response.json", r.content, bucketTempName)
    
    responseFile = "gs://real-bucket-dhl/files/february/response/" + str(dfJob["batchID"].values[0]) + "-temp-response.json"
    
    client = storage.Client()
    
    if (not checkGFileExists(str(dfJob["batchID"].values[0]) + "-temp"+ str(dfJob["id"].values[0]) +"-response.json", bucketTempName)):
        return "temp file not exist"
    bucket = client.get_bucket(bucketTempName)
    blob = bucket.get_blob(str(dfJob["batchID"].values[0]) + "-temp"+ str(dfJob["id"].values[0]) +"-response.json")
    json_data = blob.download_as_string()
    blob.delete()
    
    if (not checkGFileExists("files/february/response/" + str(dfJob["batchID"].values[0]) + "-response.json")):
        print("old file not exist")
    else:
        bucket = client.get_bucket(bucketName)
        blobOld = bucket.get_blob("files/february/response/" + str(dfJob["batchID"].values[0]) + "-response.json")
        blobOld.delete()
    
    dict_t = json.loads(json_data)
    
#     df.at[job.index[0], ["Open"]]  = strftime("%H:%M:%S", gmtime(start))
#     df.at[job.index[0], ["Closed"]]  = strftime("%H:%M:%S", gmtime(end))
    processRoutedResponse(df, dict_t,session)
    return "success. . ."

def getTimeWindowFromResponsedict(dict_t : dict, idToFind)->list:
    for route in dict_t["routes"]:
        for step in route["steps"]:
            if(step["type"] == "job"):
                if(step["job"] == idToFind):
                    start = step["arrival"]
                    end = step["arrival"] + step["duration"]
                    break
    return start,end

def changeJob(data):
    from numpy import nan as Nan
    if(not is_json(data)):
        return "not json"
    else:
        dict_t = json.loads(data)
        fullDF = pd.read_csv(gStorage)
        if(fullDF.empty):
            return "file empty"
        fullDF = fullDF.loc[(fullDF['Courier Type'] != "NON_GCA5") ]
        dict_t["PUD Svc Area"] = "KUL"
        dict_t["PUD Fac"] = "EAC"
        dict_t["PUD Rte"] = "ACA1"
        dict_t["PUD Cycle"] = "B"
        dict_t["Courier id"] = "rafinord"
        dict_t["Courier Type"] = "NON_GCA5"
        dict_t["Delivery Type"] = "NORMAL"
        dict_t["Pickup Type"] = "REGULAR"
        dict_t["ShpCnt"] = 0
        dict_t["Pallets Pcs"] = 0
        dict_t["Parcel Pcs"] = 0
        dict_t["AR dtm"] = pd.Series([np.nan])
        dict_t["Act Tm"] = dict_t["Open"]
#         dict_t["Open"] = "B"
#         dict_t["Closed"] = "B"
        dict_t["lat"] = pd.Series([np.nan])
        dict_t["lgtd"] = pd.Series([np.nan])
        dict_t["awb_booking"] = "awb_booking" + str(len(fullDF) + 1)
        dict_t["Act Ckpt Code"] = "PU"
        dict_t["PuD Type"] = "PU"
        dict_t["Stop Code"] = 111
        dict_t["MarkerColor"] = pd.Series([np.nan])
        dict_t["id"] = str(len(fullDF) + 1)
        
        df = pd.DataFrame.from_dict(dict_t)
#         df = pd.DataFrame.from_records(dict_t, index = [0], columns = fullDF.columns)
#         print(df.columns)
#         print(df["PUD Svc Area"])
    
        partialDataFrame = fullDF.loc[(fullDF['Courier id'] == "rafinord") & (fullDF["Act Dt"] == int(df["Act Dt"])) & (fullDF["Act Ckpt Code"] == "DEPAR")]
        fullDF = addRowToDataFrame(partialDataFrame.index[0] + 1, fullDF, df.iloc[0])
        uploadFile(csvPath, fullDF.to_csv(None, index=False))
        return "confirm with id " + str(df["id"].values[0])
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def confirmAddJob(rowID : int):
        fullDF = pd.read_csv(gStorage)
        if(fullDF.empty):
            return "file empty"
        selectedDF = fullDF.loc[(fullDF["id"].astype(int) == rowID) & (fullDF["Courier Type"] == "NON_GCA5")]
        if(selectedDF.empty):
            return "id not found"
        fullDF.at[selectedDF.index, "Courier Type"] = "DHL Courier" 
        uploadFile(csvPath, fullDF.to_csv(None, index=False))
        return True

client = storage.Client()
bucket = client.get_bucket(bucketName)
fullDataFrame = pd.read_csv(gStorageOptimalCsv)

client = storage.Client()
bucket = client.get_bucket(bucketName)
fullDataFrame = pd.read_csv(gStorageOptimalCsv)
from numpy import nan as Nan
fullDataFrame
fullDataFrame['Act Tm'] = pd.to_datetime(fullDataFrame['Act Tm'])
fullDataFrame['Act Tm'] = [time.time() for time in fullDataFrame['Act Tm']]
time = datetime.datetime.strptime(morningStart, '%H:%M:%S').time()
time2 = datetime.datetime.strptime(morningEnd, '%H:%M:%S').time()
maskVehicle = (fullDataFrame["Act Ckpt Code"] == "DEPAR") | (fullDataFrame["Act Ckpt Code"] == "ARRVD")
tasks = fullDataFrame.loc[~ (maskVehicle)]
# print(tasks)

dfVehicle = fullDataFrame.loc[maskVehicle]
dateList = [20200201]
dfXDayVehicle = dfVehicle.loc[dfVehicle["Act Dt"].astype(int).isin(dateList)]

# dateDF = pd.to_datetime(fullDataFrame["Act Dt"], format='%Y%m%d')
fullDataFrame["Act Dt"] = pd.to_datetime(fullDataFrame["Act Dt"], format='%Y%m%d')
dateDF = fullDataFrame.groupby(fullDataFrame['Act Dt'].dt.weekday_name)["id"].nunique()
dayDF = fullDataFrame.groupby(fullDataFrame['Act Dt'].dt.day)["id"].nunique()

sessionMMask = ((tasks['Act Tm'] >= time) & (tasks['Act Tm'] <= time2)) 
sessionMMask.value_counts()

morning = tasks.loc[sessionMMask]
afternoon = tasks.loc[~sessionMMask]

type(dayDF.astype(int))
dayDF.astype(int)[1]

client = storage.Client()
bucket = client.get_bucket(bucketName)
dfReturn = pd.read_csv(gStorageOptimalCsv)

morningSSec = datetime.datetime.strptime(morningStart, '%H:%M:%S').time()
morningESec = datetime.datetime.strptime(morningEnd, '%H:%M:%S').time()
afternoonSSec = datetime.datetime.strptime(afternoonStart, '%H:%M:%S').time()
afternoonESec = datetime.datetime.strptime(afternoonEnd, '%H:%M:%S').time()

#vehicle
def getVehicleInMonth(month = 2):
    maskVehicle = (dfReturn["Act Ckpt Code"] == "DEPAR") | (fullDataFrame["Act Ckpt Code"] == "ARRVD")
    dfVehicle = dfReturn.loc[maskVehicle]
    return len(dfVehicle)

def getVehicleDateInMonth(date,month =2):
    maskVehicle = (dfReturn["Act Ckpt Code"] == "DEPAR") | (fullDataFrame["Act Ckpt Code"] == "ARRVD")
    dfVehicle = dfReturn.loc[(maskVehicle) & (dfReturn["Act Dt"].astype(int) == int(date)) ]
    return len(dfVehicle)

def getVehicleDateSessionInMonth(date,session,month = 2):
    dfLocal = dfReturn.copy()
    maskVehicle = (dfLocal["Act Ckpt Code"] == "DEPAR") | (dfLocal["Act Ckpt Code"] == "ARRVD")
    dfLocal['Act Tm'] = pd.to_datetime(dfLocal['Act Tm'])
    dfLocal['Act Tm'] = [time.time() for time in dfLocal['Act Tm']]
    dfLocal = dfLocal.loc[(maskVehicle) & (dfLocal["Act Dt"].astype(int).isin(date))]
    if(session=="m"):
        dfVehicle = dfVehicle.loc[(dfVehicle["Act Tm"] >= morningSSec) & (dfVehicle["Act Tm"] <= morningESec)]
    elif(session=="a"):
        dfVehicle = dfVehicle.loc[(dfVehicle["Act Tm"] >= afternoonSSec) &(dfVehicle["Act Tm"] <= afternoonESec)]
    else:
        return "not prepared session"
                                  
    return len(dfVehicle)

#get routeIDS
def getBatchID():
    dfLocal = dfReturn.copy()
    dfLocal = dfLocal["batchID"].unique()
#     print(type(list(dfLocal)))
    dict_t = {}
    for item in list(dfLocal):
        dict_t[item] = item
    return json.dumps(dict_t)
#     print(dfLocal)
    return dfLocal.to_json()

def getRoute(batchID):
    dfLocal = dfReturn.copy()
    dfLocal = dfLocal.loc[dfLocal["batchID"].isin(batchID)]
#     dfLocal = dfLocal.loc[dfLocal["duration"]]



def getVehicle(courierID = None, date=None, action=None, s=None,weekDay=None, perDay=None):
    dfLocal = dfReturn.copy()
    dfLocal["Act Dt"] = pd.to_datetime(dfReturn["Act Dt"], format='%Y%m%d')
    maskVehicle = (dfLocal["Act Ckpt Code"] == "DEPAR") | (dfLocal["Act Ckpt Code"] == "ARRVD")
    dfLocal = dfLocal.loc[maskVehicle]
    if(courierID):
        dfLocal.loc[dfLocal["Courier id"].isin(courierID)]
    if(action):
        dfLocal.loc[dfLocal["Act Base"] == action]
    if(date):
        dfLocal.loc[dfLocal["Act Dt"].isin(date)]
    if(s):
        dfLocal['Act Tm'] = pd.to_datetime(dfLocal['Act Tm'])
        dfLocal['Act Tm'] = [time.time() for time in dfLocal['Act Tm']]
        if(s=="m"):
            dfLocal = dfLocal.loc[(dfLocal["Act Tm"] >= morningSSec) & (dfLocal["Act Tm"] <= morningESec)]
        elif(s=="a"):
            dfLocal = dfLocal.loc[(dfLocal["Act Tm"] >= afternoonSSec) &(dfLocal["Act Tm"] <= afternoonESec)]
        else:
            return "not prepared session"
    if(weekDay):
        dfLocal = dfLocal.groupby(dfLocal['Act Dt'].dt.weekday_name)["id"].nunique()
        return dfLocal.to_json()
    if(perDay):
        dfLocal = dfLocal.groupby(dfLocal['Act Dt'].dt.day)["id"].nunique()
        return dfLocal.to_json()
    return len(dfLocal)

def getJob(date=None, action=None, s=None, mode="weekDay"):
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    dfReturn = pd.read_csv(gStorageOptimalCsv)
    # date = pd.to_datetime(date)
    dfLocal = dfReturn.copy()
    # dfLocal["Act Dt"] = pd.to_datetime(dfReturn["Act Dt"], format='%Y%m%d')
    maskVehicle = (dfLocal["Act Ckpt Code"] == "DEPAR") | (dfLocal["Act Ckpt Code"] == "ARRVD")
    dfLocal = dfLocal.loc[~maskVehicle]
    if(action):
        dfLocal = dfLocal.loc[dfLocal["Act Base"] == action]
    if(date):
        dfLocal = dfLocal.loc[dfLocal["Act Dt"].isin(date)]
    if(s):
        dfLocal['Act Tm'] = pd.to_datetime(dfLocal['Act Tm'])
        dfLocal['Act Tm'] = [time.time() for time in dfLocal['Act Tm']]
        if(s=="m"):
            dfLocal = dfLocal.loc[(dfLocal["Act Tm"] >= morningSSec) & (dfLocal["Act Tm"] <= morningESec)]
        elif(s=="a"):
            dfLocal = dfLocal.loc[(dfLocal["Act Tm"] >= afternoonSSec) &(dfLocal["Act Tm"] <= afternoonESec)]
        else:
            return "not prepared session"
    dfLocal["Act Dt"] = pd.to_datetime(dfReturn["Act Dt"], format='%Y%m%d')
    if(mode == "weekday"):
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
        if (dfLocal.empty):
            print("HASDASDASDASDASDS")
        dfLocal = dfLocal.groupby(dfLocal['Act Dt'].dt.weekday_name)["id"].nunique().reindex(days)

        return dfLocal.to_json()
    if(mode == "day"):
        dfLocal = dfLocal.groupby(dfLocal['Act Dt'].dt.day)["id"].nunique()
        return dfLocal.to_json()
    return len(dfLocal)
#action
def getJobInAction():
    return []

from flask import Flask, render_template
from flask import jsonify
from flask import request
app = Flask(__name__)

# [START gae_python37_datastore_store_and_fetch_times]'
@app.route('/')
def test12312():
    return "hello"

@app.route('/getGeo')
def fun1():
    rowID = int(request.args.get('rowID'))
    a,b = getRoutedGeocode(rowID)
    c = {}
    c["lat"] = a
    c["lgtd"] = b
    j = json.dumps(c)
    return j

# http://127.0.0.1:8080/getEta?rowID=680
@app.route('/getEta')
def fun2():
    rowID = int(request.args.get('rowID'))
    return json.dumps(getETAByID(rowID))

# http://127.0.0.1:8080/changeTime?rowID=680&start=15:30:00&end=16:30:00
@app.route('/changeTime')
def fun3():
    rowID = int(request.args.get('rowID'))
    start = request.args.get('start')
    end = request.args.get('end')
    return jsonify(changeTime(rowID, start, end))

# http://127.0.0.1:8080/confirmChangeTime?rowID=680
@app.route('/confirmChangeTime')
def fun4():
    rowID = int(request.args.get('rowID'))
    return jsonify(confirmChangeTime(rowID))

# http://127.0.0.1:8080/addJob?rowID=680

# example json 
# {"Customer Name": "FG FAMILY GOLD", "Street": "NO.113, JLN KESUMA 4B \\/ 1\\nBDR TASIK KESUMA 40 SELANGOR\\nBERANANG", "zip": "43700", "City": "BERANANG", "Act Dt": 20200201, "Act Base": "P", "Open": "9:00", "Closed": "12:00", "Prod Grp": "WPX", "Prod Code": "P", "Total Pcs": 2.0, "Weight": 1.78}

# data = {"Customer Name":"FG FAMILY GOLD","Street":"NO.113, JLN KESUMA 4B \\/ 1\\nBDR TASIK KESUMA 40 SELANGOR\\nBERANANG","zip":"43700","City":"BERANANG","Act Dt":20200201,"Act Base":"P","Open":"9:00","Closed":"12:00","Prod Grp":"WPX","Prod Code":"P","Total Pcs":2.0,"Weight":1.78}
# r = requests.post("http://127.0.0.1:8080/addJob?rowID=680",json=json.dumps(data), headers=headers)
@app.route('/addJob', methods=['GET', 'POST'])
def fun5():
    data = request.json
    # return data
    return jsonify(changeJob(data))


# http://127.0.0.1:8080/confirmAddJob?rowID=680
@app.route('/confirmAddJob')
def fun6():
    rowID = int(request.args.get('rowID'))
    return jsonify(confirmAddJob(rowID))

@app.route('/test', methods=["POST"])
def test():
    json = request.json
    print(json["date-multi"])
    if("date" in json):
        date = json["date"]
        print(date)    
    if("session" in json):
        session = json["session"]


    return "Asds"

@app.route('/job', methods=["POST"])
def test2():
    json = request.json
    print(json)
    if("date-range-type" in json):
        if(json["date-range-type"] == "range"):
            date = json["date-range"]
            start, end = date.split(" - ")

            start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
            end = datetime.datetime.strptime(end, '%Y-%m-%d').date()

            delta = end - start       # as timedelta
            dates = []

            for i in range(delta.days + 1):
                day = start + timedelta(days=i)
                day = day.strftime('%Y%m%d')
                dates.append(day)
 
            # build list date from this variable
        elif(json["date-range-type"] == "multi"):
            print("multi")

            date = json["date-multi"]
            arr = date.split(", ")
            if(len(arr) == 1):
                dates = json["date-multi"]
                # dates = datetime.datetime.strptime(dates, '%Y-%m-%d').date()
                dates = [dates.replace("-", "")]
            else:
                dates = [day.replace('-','') for day in arr]
                # dates = [datetime.datetime.strptime(day, '%Y-%m-%d').date() for day in arr]
            # print(dates)
    if("session" in json):
        session = json["session"]
    if("action" in json):
        action = json["action"]
    if("mode" in json):
        mode = json["mode"]
    # print(getJob(dates, action, session, mode))
    toReturn = getJob(dates, action, session, mode)
    return toReturn
    # return "adas"
# [END gae_python37_datastore_store_and_fetch_times]

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8007, debug=True)