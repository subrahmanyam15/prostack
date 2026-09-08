from fastapi import APIRouter
router=APIRouter(prefix='/products')
products=[
    {'pid':101,'pname':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'pname':'Lenovo Mouse','price':400,'category':'Electronics'},
    {'pid':103,'pname':'ThinkPad','price':108000,'category':'Electronics'},
    {'pid':104,'pname':'Water Bottle','price':10,'category':'Groceries'},
    {'pid':105,'pname':'Dell Inspiron','price':150000,'category':'Electronics'},
    {'pid':106,'pname':'Mac Book Pro','price':183000,'category':'Electronics'},
    {'pid':107,'pname':'Stappler','price':35,'category':'Stationary'},
    {'pid':108,'pname':'R Pen','price':10,'category':'Stationary'},
    {'pid':109,'pname':'Parker Pen','price':200,'category':'Stationary'},
    {'pid':110,'pname':'Meta Rayban','price':40000,'category':'Electronics'}
]
'''
Rest API -1
________________
Usage: Fetch All products
Rest API URL: http://127.0.0.1:8000/products/
Method Type:GET
Required Fields:None
Access Type:Public

'''

@router.get("/")
def get_products():
    return products



'''
Rest API -2
________________
Usage: Fetch product by Id
Rest API URL: http://127.0.0.1:8000/products/10
Method Type:GET
Required Fields:None
Access Type:Public
'''

@router.get("/{p_id}")
def get_product_by_id(p_id:int):
    new_products=list(filter(lambda product:product['pid']==p_id,products))

    if new_products:
        return new_products
    else:
        return {"message":"products not available"}


'''
Rest API -4
______
Usage: Fetch products by category
Rest API URL: http://127.0.0.1:8000/products/category/electronics
Method Type:GET
Required Fields:None
Access Type:Public
'''

@router.get("/category/{category}")
def get_products_by_category(category:str):
    new_products=list(filter(lambda product:product['category'].lower()==category.lower(),products))
    if new_products:
         return new_products
    else:
        return {'msg':"Product Not Available"}



'''

Rest API -3
________________
Usage: Fetch product by name
Rest API URL: http://127.0.0.1:8000/products/Marker Pen
Method Type:GET
Required Fields:None
Access Type:Public
'''    

@router.get("/name/{p_name}")
def get_products_by_category(p_name:str):
    new_products=list(filter(lambda product:product['pname'].lower()==p_name.lower(),products))
    if new_products:
         return new_products
    else:
        return {'msg':"Product Not Available"}