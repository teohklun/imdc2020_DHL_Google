#global param, config

bucketName = "real-bucket-dhl"
csvPath = "3.csv"
gStorage = 'gs://real-bucket-dhl/3.csv'

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
            
#             if(arrivalTime == arrivalTime):
#                 if( (session == "m") & (getMiliSec(departTime) > getMiliSec("08:45:00") ) & ( getMiliSec(arrivalTime) < getMiliSec("13:59:00") ) ):
#                     valid = True
#                 elif((session == "a")& (getMiliSec(departTime) > getMiliSec("14:00:00") ) & (getMiliSec(arrivalTime) < getMiliSec("23:59:00")  ) ):
#                     valid = True
#                 else:
#                     print("condition not meet")
#                     valid = False
#             elif( session == "m" & (getMilliSec(departTime) > getMiliSec("08:45:00") & getMilliSec(departTime) > getMiliSec("14:00:00") ):
#                  valid = True
#             elif( session == "a" & (getMilliSec(departTime) > getMiliSec("08:45:00") & getMilliSec(departTime) > getMiliSec("14:00:00") ) 
#                 valid = True
#             else:
#                 valid =False
#                  print("unknown situation 4")

                
            
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

def getRouteDetailWithID(ID):
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
    blob = bucket.get_blob(getResponseFileName(date,session))
    json_data_bytes = blob.download_as_string()
    dict_t = json.loads(json_data_bytes)
    return dict_t

def checkGFileExists(fileName : str) -> bool:
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
#     name = 'files/february/optimalRoutes.csv'
#     name = "files/february/response/20200204-a-447-response.json"
    return storage.Blob(bucket=bucket, name=fileName).exists(client)

def handleOptimalRoute(dataFrame):
    from datetime import datetime
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    pathForRead = 'gs://real-bucket-dhl/files/february/optimalRoutes.csv'
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
        oldDataFrame = pd.read_csv(pathForRead)
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
        string = newDataFrame.to_csv(None, index=False)
        blob = bucket.blob(csvFilePathName)
        blob.upload_from_string(string, "application/vnd.ms-excel")

def processRoutedResponse(fullDataFrame):
    
    client = storage.Client()
    bucket = client.get_bucket(bucketName)
    
    for routes in test_dict_t["routes"]:
        df = pd.DataFrame()
        vehicleInformation = fullDataFrame.loc[fullDataFrame['id'] == routes["vehicle"]]
        actCkptCode = vehicleInformation["Act Ckpt Code"].values[0]
        vehicleInformation['id'] = vehicleInformation['id'].astype("int")
        vehicleInformation['id'] = vehicleInformation['id'].astype("str")
        vehicleID = vehicleInformation['id'].values[0]

        date = vehicleInformation["Act Dt"].values[0]
        name = vehicleInformation["Courier id"].values[0]
        routes["steps"][0]["name"] = vehicleInformation["Courier id"].values[0]
        
        tempSingleRoute = test_dict_t.copy()
#         del tempSingleRoute["routes"]
        tempSingleRoute["routes"] = [test_dict_t["routes"][0]]
        
        content = json.dumps(tempSingleRoute, cls=NpEncoder) 
        blob = bucket.blob("files/february/response/"+ str(date) +  "-" + session  + "-" + vehicleID + "-response.json")
        blob.upload_from_string(content, "application/json")
        print("created json file")
        
        for indexStep, step in enumerate( routes["steps"], start = 1):
            if(step["type"] == "start" or step["type"] == "end"):
                startingInformation = vehicleInformation.copy()
                startingInformation.at[startingInformation.index[0], "Act Tm"] = getTime24hour(step["arrival"])
                startingInformation["batchID"] = str(date) +  "-" + session  + "-" + str(vehicleID)

                if(step["type"] == "end"):
    #                 startingInformation.at[startingInformation.index[0], "id"] = str(startingInformation["id"].values[0]) + "arrvd"
                    startingInformation.at[startingInformation.index[0], "Act Ckpt Code"] = "ARRVD"
                if(actCkptCode == "DEPAR"):
                    startingInformation.at[startingInformation.index[0], "id"] = str(startingInformation["id"].values[0]) + "arrvd"
                elif(actCkptCode == "ARRVD"):
                    startingInformation.at[startingInformation.index[0], "id"] = str(startingInformation["id"].values[0]) + "depart"
                else:
                    print("unprepare sitaution 3")
                    print("actCkptCode : " + actCkptCode)
                df = df.append(startingInformation)
            elif(step["type"] == "job"):
                jobInformation = fullDataFrame.loc[fullDataFrame['id'] == step["job"]]
                if(jobInformation["Street"].values[0] == jobInformation["Street"].values[0]):
                    string = jobInformation["Street"].values[0]
                    description = re.sub('\s+', ' ', string)
                    step["description"] = description

                else:
                    step["description"] = "Street is blank"

                new = pd.DataFrame({'PUD Svc Area': [vehicleInformation["PUD Svc Area"].values[0]], 
                         'PUD Fac': [vehicleInformation["PUD Fac"].values[0]],
                         'PUD Rte': [vehicleInformation["PUD Rte"].values[0]],          
                         'PUD Cycle': [vehicleInformation["PUD Cycle"].values[0]],
                          'Courier id':[vehicleInformation["Courier id"].values[0]],
                          'Courier Type':  [vehicleInformation["Courier Type"].values[0]],
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

        
        
        string = df.to_csv(None, index=False)
        blob = bucket.blob("files/february/response/"+ str(date) +  "-" + session  + "-" + vehicleID + ".csv")
#         print("files/february/response/"+ str(date) +  "-" + session  + "-" + str(vehicleInformation['id']) + ".csv" )
#         print(str(vehicleInformation['id'].astype("int")) + ".csv" )

        blob.upload_from_string(string, "application/vnd.ms-excel")

        df.to_csv("routes/"+ str(date) + "/" +session  + "/" + str(name) + ".csv", index=False)
        print("created csv file . . ..")
        handleOptimalRoute(df)

    blob = bucket.blob(getInputeForResponseFileName(date,session))
    content = json.dumps(test_dict_t, cls=NpEncoder) #the processed routes
    blob.upload_from_string(content, "application/json")
    print("created updated response json file")

def tryGotUnassignedInResponse2(date : str,  session: str, street: None, unassignedJob =None ):
    
    client = storage.Client()
    bucket = client.get_bucket(bucketName)

    fullDataFrame = pd.read_csv(gStorage)
    fullDataFrame = fullDataFrame.loc[(fullDataFrame['Courier Type'] != "NON_GCA5") ]
    #initial id column
    if 'id' not in fullDataFrame .columns:
        fullDataFrame["id"] = fullDataFrame.index+1
    
    # fullDataFrame = pd.read_csv(csvPath)
    if(~(street != street)):
        fullDataFrame, newAwbBooking = addJob(fullDataFrame, date, session, street)

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

        processRoutedResponse(fullDataFrame)
        
    #     #update the added job to csv
        newJobDataFrame = fullDataFrame.loc[(fullDataFrame["awb_booking"] == newAwbBooking)]

    #     #temp fix
        fullDataFrame.at[newJobDataFrame.index[0], "Courier Type"] = "NON_GCA5"

        string = fullDataFrame.to_csv(None, index=False)

        blob = bucket.blob("3.csv")

        blob.upload_from_string(string, "application/vnd.ms-excel")

        dict_t = json.loads(r.content)
        dict_t["extra"] = {}

        dict_t["extra"]["awb_booking"] = newAwbBooking

        responseDict = gotUnssigned(dict_t)

#     print(dict_t)
    # print(responseDict == [])#
#     print(content)
    return dict_t

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
