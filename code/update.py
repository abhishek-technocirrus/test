from pymongo import MongoClient
import os
# Retrieve the host and port from environment variables
db_host = os.environ.get('DB_HOST')
db_port = int(os.environ.get('DB_PORT'))

# Connect to the DocumentDB cluster
client = MongoClient(db_host, db_port)

# Authenticate with the provided credentials
db = client.my_database
db.authenticate('admin', 'password')

# Update a document in a collection
collection = db.my_collection
query = {'_id': '12345'}
update = {'$set': {'name': 'Abhishek'}}
collection.update_one(query, update)
