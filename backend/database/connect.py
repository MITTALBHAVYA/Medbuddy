from pymongo.mongo_client import MongoClient
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

Api_key = os.getenv('DB_URI')

app = FastAPI()

uri = Api_key


def database(database_name):
    client = MongoClient(uri)
    return client[database_name]

