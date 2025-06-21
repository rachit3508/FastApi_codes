from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/intro")
def read_intro():
    return "This is a simple FastAPI application."

@app.get("/view")
def read_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

    
