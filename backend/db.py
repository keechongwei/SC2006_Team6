# for Ying Jie, this is chatted,
# need to actually see how to connect to MongoDB

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['sc2006_db']  # Replace with actual database name
users_collection = db['users']
institutions_collection = db['institutions']