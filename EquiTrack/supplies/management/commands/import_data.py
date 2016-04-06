__author__ = 'Tarek'


import os
import json
import time
import requests
from bson.json_util import dumps
from bson.json_util import loads

import datetime


import argparse
from urlparse import urljoin
from ConfigParser import SafeConfigParser

from django.conf import settings
from pymongo import MongoClient
from django.template.defaultfilters import slugify

from requests.auth import HTTPBasicAuth
from django.core.management.base import BaseCommand



class Command(BaseCommand):

    can_import_settings = True

    def initiate_mongo_connection(self):
        connection = MongoClient(host='localhost', port=27017)
        db = connection.winter
        return db

    def handle(self, **options):

        raisScript = RaisAPIClass('mbazin@unicef.org', '?45x6UJa')
        raisScript.getlogininfo()

        data = requests.get(os.path.join(settings.COUCHBASE_URL,'_all_docs?include_docs=true'),auth=HTTPBasicAuth(settings.COUCHBASE_USER, settings.COUCHBASE_PASS)).json()

        rows = data['rows']



        connection = self.initiate_mongo_connection()
        lebanon = connection.data
        pcodes = connection.pcodes
        i=0
        for row in rows:
             doc = row['doc']
            ## CHANGE IDIOT PARTNERS
             if ('partner_name' in doc.keys()):
                 if doc['partner_name'] == 'user5':
                     doc['partner_name'] = 'sawa'
                 if doc['partner_name'] == 'unicef-leb':
                     doc['partner_name'] = 'lost'

            ## ADD ADMIN LEVEL DATA


             if 'location' in doc:
                 print doc['location']['p_code']
                 pcode = json.loads(dumps(pcodes.find_one({'_id': doc['location']['p_code']})))
                 if pcode != None:
                     print pcode["_id"]
                     doc["governorate"] = pcode["governorate"]
                     doc["district"] = pcode["district"]
                     doc["cadastral"] = pcode["cadastral"]
                     print doc["governorate"] +" "+doc["district"]+" "+doc["cadastral"]


            ## REMOVE ARRAYS
             if ('type' in doc.keys()) and (doc['type'] == 'assessment') and (doc['id_type'] == 'UNHCR'):

                CSCSurvey = {}
                WFPSurvey = {}

                if 'surveys' in doc.keys():
                   if  type(doc['surveys']) is list:
                        for survey in doc['surveys']:
                                if survey.keys()[0] == "CSC Survey":
                                    for question in survey['CSC Survey']:
                                        CSCSurvey.update(question)
                                elif survey.keys()[0] == "WFP Survey":
                                    for question in survey['WFP Survey']:
                                        WFPSurvey.update(question)


                doc['surveys']={"CSC Survey":CSCSurvey}
                doc['surveys'].update({"WFP Survey": WFPSurvey})


                old = json.loads(dumps(lebanon.find_one({'_id': doc['_id']})))

                #print(old['gender'])




                #if (old['gender'] == '' or old['gender'] == "N/A") and (old['first_name'] == '' or old['first_name'] == 'N/A') and  old['last_name'] == '' and old['middle_name'] == '':

                print doc['_id']

                if  old == None or 'rais_doc' not in old.keys() or old['_rev'] != doc['_rev']:
                #if i>=25608:
                    pa = raisScript.getpabycase(doc['official_id'])
                    #print(old)
                    #print old['_rev']
                    #print doc['_rev']
                    if pa != None and len(pa)>0:

                        pa = pa[0]
                        pa.pop('$id',None)
                        doc['first_name'] = pa['GivenName']
                        doc['middle_name'] = pa['FatherName']
                        doc['family_name'] = pa['FamilyName']
                        doc['marital_status'] = pa['MaritalStatusText']
                        doc['dob'] = pa['DOB']
                        doc['gender'] = pa['Sex']
                        doc['unhcr_phone'] = pa['CoAPhone']
                        doc['rais_doc'] = pa
                        doc.pop("last_name", None)
                    lebanon.update({'_id': doc['_id']}, doc, upsert=True)

                i+=1
                print i

             else:
                lebanon.update({'_id': doc['_id']}, doc, upsert=True)



class RaisAPIClass():

    def __init__(self,
                 username=None,
                 password=None,
                 base_url='https://www.unhcrmenadagdata.org/'):
        self.base_url = base_url
        self.headers = {}
        if username and password:
            self.loginData = {'grant_type': 'password','username': username,'password': password}


    def getlogininfo(self):
        response = requests.post(self.base_url+"RaisWebApiv2/Token",self.loginData)
        parsed_json_response = json.loads(response.text)
        auth = 'Bearer ' + parsed_json_response['access_token']
        self.headers = {'Authorization': auth}
        return self.headers

    def getpabycase(self,case_number):
        try:
             response = requests.get(self.base_url+"RaisWebApiv2/api/GetPAByCase/{}".format(case_number),
                                                                        headers=self.headers).json()
             return response
        except ValueError:
             return []





