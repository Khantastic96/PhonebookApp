# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:52:02 2024

@author: Sharek Khan
"""

# Import modules
from Entities.Phonebook import Phonebook
from pymongo.mongo_client import MongoClient
from .config import MONGO_URI
from pymongo.server_api import ServerApi

class PhonebookDAO:
    # Define the init method/class constructor
    def __init__(self):
        self.__phonebook = Phonebook()
        
    # Define the method to insert a new phonebook entry to the database
    def insert_phonebook(self, user, phonebook):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Phonebooks")
            
            # Insertion logic
            collection.insert_one({
                "_id": phonebook.get_phonebook_id(),
                "user_id": user.get_user_id() })
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()                
        return 1
    
    # Define the method to find an existing user's phonebook entry in the database
    def find_phonebook(self, user_id):
        # Create a return object of the query
        result = {}
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Phonebooks")
            
            # Define query
            query_filter = { "user_id": user_id }
            
            # Search logic
            result = collection.find_one(query_filter)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return result
    
    # Define the method to determine if a user's phonebook exists in the database
    def has_phonebook(self, user_id):
        # Create a verification flag
        has_phonebook = False
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Phonebooks")
            
            # Define query
            query_filter = { "user_id": user_id }
            
            # Verification logic
            result = collection.find_one(query_filter)
            if result:
                has_phonebook = True
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return has_phonebook
    
    # Define the method to update an existing phonebook entry in the database
    def update_phonebook(self, phonebook_id):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Phonebooks")
            
            # Define query
            query_filter = { "_id": phonebook_id }
            update_operation = { "$set": { "_id": phonebook_id } }
            
            # Modification logic
            collection.update_one(query_filter, update_operation)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to delete an existing phonebook entry from the database
    def delete_phonebook(self, phonebook_id):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Phonebooks")
            
            # Define query
            query_filter = { "_id": phonebook_id }
            
            # Deletion logic
            collection.delete_one(query_filter)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
