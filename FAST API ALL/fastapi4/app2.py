from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def home_page():
 return {'message':"app root req"}

@app.post("/")
def create_user():
 return {'message':"new user created"}

@app.put("/")
def update_user():
 return {'message':"user update "}

