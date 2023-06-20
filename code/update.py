from pymongo import MongoClient
import os
# Retrieve the host and port from environment variables
db_host = docdb-2023-06-20-07-52-242.cgognpdsxe7j.us-east-1.docdb.amazonaws.com
db_port = 27017

# Connect to the DocumentDB cluster
client = MongoClient(db_host, db_port)

# Authenticate with the provided credentials
db = client.my_database
db.authenticate('abhishek', 'Temp1234')

# Update a document in a collection
collection = db.my_collection
query = {'_id': '12345'}
update = {'$set': {'name': 'Abhishek'}}
collection.update_one(query, update)
