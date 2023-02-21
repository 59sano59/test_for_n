from faker import Faker
import json
from random import randint
import random
import os
# from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import time
import firebase_admin
from firebase_admin import db

# load_dotenv() 

key_path = os.path.join(os.path.dirname(__file__), ".vscode", "cool-ocean-292410-firebase-adminsdk-6q9ek-cae1a092eb.json")

databaseURL = 'https://cool-ocean-292410-default-rtdb.europe-west1.firebasedatabase.app/'

fake = Faker()
module_type = ['RU','BB', 'SM', 'SM+BB']

cred_obj = firebase_admin.credentials.Certificate(key_path)
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL' :databaseURL})
ref = db.reference("/")

while True:

    testline_data = {
        'radio1': {
        
        'testlineId': 
          randint(1, 100),
            
        'resultId': 
          randint(0, 100),
            
        'timestamp': 
          datetime.now().isoformat(','),
            
        'moduleName': 
          fake.ssn(),
            
        'serialNumber': 
          fake.ssn(),
            
        'featureId': 
            randint(1, 100),
            
        'btsConfigBlockId' : 
          randint(1, 100),
            
        'platformName' : 
          fake.ssn(),
            
        'bracketSlot' : 
          fake.ssn(),
            
        'moduleType' : 
          random.choice(module_type),
            
        'infoModelObjectId' : 
          randint(1, 100),
        
        'memory' : 
          randint(50, 100),

        'cpu' : 
          randint(200, 1000),
            
        'temperature' : 
          randint(-50, 200),
            
        'power' : 
          randint(0, 500),
        },

        'radio2' : {
        'testlineId': 
          randint(1, 100),
            
        'resultId': 
          randint(0, 100),
            
        'timestamp': 
          datetime.now().isoformat(','),
            
        'moduleName': 
          fake.ssn(),
            
        'serialNumber': 
          fake.ssn(),
            
        'featureId': 
            randint(1, 100),
            
        'btsConfigBlockId' : 
          randint(1, 100),
            
        'platformName' : 
          fake.ssn(),
            
        'bracketSlot' : 
          fake.ssn(),
            
        'moduleType' : 
          random.choice(module_type),
            
        'infoModelObjectId' : 
          randint(1, 100),
        
        'memory' : 
          randint(50, 100),

        'cpu' : 
          randint(200, 1000),
            
        'temperature' : 
          randint(-50, 200),
            
        'power' : 
          randint(0, 500),
    }}

    time.sleep(1)
    print('Creating data...')
    with open('dummy.json', 'w') as fp:
        json.dump(testline_data, fp, indent=4)

    # df = pd.DataFrame(testline_data, index=testline_data)
    # print(df.isnull().sum()) #uncomment to see null value

    for value in list(testline_data):
        if value is None:
            del value[testline_data]
            print('None value deleted')
        elif isinstance(testline_data, dict):
            print('no null values')

    for test in testline_data:
        print('Getting data...')
        s = json.dumps(testline_data) # Convert the reading into a JSON string.

    ref.set(testline_data)
    print("Sending data...")
    # Close the producer.


    if testline_data == 0:
        print('List empty!!!!')
        break
