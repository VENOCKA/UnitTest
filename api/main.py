from typing import Optional
import pymongo
import certifi
from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
from model.Figurine import PyObjectId

from model.Figurine import Figurine

app = FastAPI()
client = pymongo.MongoClient("mongodb+srv://VENOCKA:Tifoznf027@cluster0.dvj0i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.Amazon
DB_Figu = db.Figurine

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/Figurine/{id}", response_model=Figurine)
async def read_one(id:PyObjectId):
    figu = DB_Figu.find_one({"_id": id})
    print(figu)
    return figu

@app.get("/GetAll")
async def read_item():
    return [Figurine(**figurine) for figurine in DB_Figu.find()]

@app.post("/Figurine", response_model=Figurine)
async def create_item(figurine: Figurine = Body(...)):
    New = DB_Figu.insert_one(figurine.dict(by_alias=True))
    return DB_Figu.find_one({"_id": New.inserted_id})

@app.put("/Figurine/{id}")
async def modify_item(id: PyObjectId, figurine: Figurine = Body(...)):
    DB_Figu.update_one({'_id': id}, {"$set": figurine.dict(by_alias=True)})
    return { "status": "succes"}

@app.delete("/Figurine/{id}")
async def delete_item(id: PyObjectId):
    DB_Figu.delete_one({'_id': id})
    return { "status": "deleted"}