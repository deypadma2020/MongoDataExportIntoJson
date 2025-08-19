import os
from dotenv import load_dotenv 
from pymongo import MongoClient

load_dotenv(".env")

mongo_url = os.getenv("mongo_url")
print(mongo_url)
client = MongoClient(mongo_url)
print("Python-MongoDB connection created succesfully -\n", client)
