# extract 
import requests
import mysql.connector
rest_api_url='https://jsonplaceholder.typicode.com/users'
user_resp=requests.get(rest_api_url)
users=user_resp.json()

#Tranform users data according mysql users table
users_data=[]

for user in users:
    users_data.append(())




dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='nancharamma',
                                  database='db15') 
    cursor=dbcon.cursor()
    sql_st='''
            create table employees(
            eid int,
            ename varchar(32),
            esal float,
            gender varchar(32),
            primary key(eid)
            );
           '''
    cursor.execute(sql_st)
    print("New Table created successfully")
except Exception as err:
    print(err)



finally:
    if cursor is not None:
        cursor.close()
    if dbcon is not None:
        dbcon.close()
