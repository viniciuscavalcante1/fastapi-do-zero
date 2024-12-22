from fastapi import FastAPI  # import object FastAPI from fastapi lib

app = FastAPI()  # starts FastAPI application

@app.get("/")  # defines an endpoint with address /, accessible by HTTP method GET
def read_root():  # function that will be executed when a client access /
    return {'message': 'Hello, world!'}  # returned data