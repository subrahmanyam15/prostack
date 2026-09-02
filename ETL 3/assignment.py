#Extract data from Rest API's

import requests,json,pymongo
rest_api_ulr='https://jsonplaceholder.typicode.com/users'
users=requests.get(rest_api_ulr).json()

#Tranform - for JSON file
users_json=[]

for user in users:
    users_json.append({
        "uid":user['id'],
        "uname":user['name'],
        "email":user['email'],
        "city":user['address']['city']
    })



#Load into new json file
with open('users.json','w') as fp1:
    json.dump(users_json,fp1)
print("New JSON File created successfully")


try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['toxic']
    users_col=db['users']
    users_col.insert_many(users_json)
    print("Data Inserted into MongoDB User collections successfully")
except:
    pass
finally:
    pass


