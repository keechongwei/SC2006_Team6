from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://tang0551:hUvvibJrWBYImwE0@cluster0.nl9y4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database('SC2006_api_db')
usersdb = db.Institution

# Get all data from the collection
all_users = list(usersdb.find({}))

# Print all users
for user in all_users:
    print(user)