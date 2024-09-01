# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:39:02 2024

@author: Sharek Khan
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "<INSERT CONNECTION STRING HERE>"

# Define the main function
def main():
    # Create a new client and connect to the server
    client = MongoClient(URI, server_api=ServerApi('1'))

    try:
        # Get databases
        database = client.get_database("<DATABASE NAME>")
        database = client["<DATABASE_NAME>"] # Alt way
        # Get collections
        collection = database.get_collection("<COLLECTION_NAME>")
        collection = database["<COLLECTION_NAME>"] # Alt way
        
        # Create a collection
        database.create_collection("<COLLECTION_NAME>")
        
        # Get a list of collections
        collections = database.list_collections()
        for c in collections:
            print(c)
        
        # Get a list of collection names
        collection_names = database.list_collection_names()
        for c in collection_names:
            print(c)
        
        # Delete a collection
        test = database["<COLLECTION_NAME>"]
        test.drop()
        
        # Insert one
        result = collection.insert_one(
            { "<FIELD_NAME>": "<VALUE>" }
        )
        print(result.acknowledged)
        
        # Insert many
        document_list = [
            { "<FIELD_NAME>": "<VALUE>" },
            { "<FIELD_NAME>": "<VALUE>" },
            { "<FIELD_NAME>": "<VALUE>" }
        ]
        result = collection.insert_many(document_list)
        print(result.acknowledged)
                
        # Find one
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        result = collection.find_one(query_filter)
        print(result)
        
        # Find many
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        results = collection.find_many(query_filter)
        for document in results:
            print(document)
        
        # Update one
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        update_operation = { "$set": { "<FIELD_NAME>": "<VALUE>" } }
        result = collection.update_one(query_filter, update_operation)
        print(result.modified_count)
        
        # Update many
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        update_operation = { "$set": { "<FIELD_NAME>": "<VALUE>" } }
        result = collection.update_many(query_filter, update_operation)
        print(result.modified_count)
        
        # Replace one
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        replace_document = { "<FIELD_NAME>": "<VALUE>" }
        result = collection.replace_one(query_filter, replace_document)
        print(result.modified_count)
        
        # Delete one
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        result = collection.delete_one(query_filter)
        print(result.deleted_count)
        
        # Delete many
        query_filter = { "<FIELD_NAME>": "<VALUE>" }
        result = collection.delete_many(query_filter)
        print(result.deleted_count)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
    finally:
        # Close the client
        client.close()
        
main()
