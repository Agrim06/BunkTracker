from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["BunkTracker"]

users_collection = db["users"]
subjects_collection = db["subjects"]
attendance_collection = db["attendance"]
