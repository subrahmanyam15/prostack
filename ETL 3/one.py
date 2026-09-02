import requests
import mysql.connector
rest_api_url='https://dummyjson.com/products'
products_resp=requests.get(rest_api_url)
products_data=products_resp.json()
products=products_data["products"]
print(type(products))


#Transform 

beauty_products= []
for product in products:
    if product['category']=="beauty":
        beauty_products.append((
        product["id"],
        product["title"],
        product["price"],
        product["category"],
        product["discount"]
    ))

#load the data
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host="localhost",
                                  user="uroot",
                                  password="nancharamma",
                                  database="db17")
    cursor=dbcon.cursor()
    sql_st='''
            insert into users
            values
            (%s,%s,%s,%s);
           '''
    cursor.executemany(sql_st,beauty_products) 
    dbcon.commit()
    print(cursor.row_count,"beauty products created")


except mysql.connector.Error as err:
    print(err)
except Exception as err:
    print(err)

finally:
    if cursor is not None:
        cursor.close()
    if dbcon is not None and dbcon.is_connected():
        dbcon.close()