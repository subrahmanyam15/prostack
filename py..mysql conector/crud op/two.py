import mysql.connector
dbcon=None 
cursor=None

try:
    dbcon= mysql.connector.connection(host='localhost',
                                      user='root',
                                      password='nancharamma',
                                      database='db15')
    cursor=dbcon.cursor();