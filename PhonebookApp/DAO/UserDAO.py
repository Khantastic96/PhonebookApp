# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:05:44 2024

@author: Sharek Khan
"""

# Import modules
from Entities.User import User
from pymongo.mongo_client import MongoClient
from .config import MONGO_URI
from pymongo.server_api import ServerApi

class UserDAO:    
    # Define the init method/class constructor
    def __init__(self):
        self.__user = User()

    # Define the method to insert a new user entry to the database
    def insert_user(self, user):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")
            
            # Insertion logic
            collection.insert_one({
              "_id": user.get_user_id(),
              "username" : user.get_username(),
              "password" : user.get_password() })
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to find an existing user entry in the database
    def find_user(self, username):
        # Create a return object of the query
        result = {}
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")

            # Define query
            query_filter = { "username":  username }
            
            # Search logic
            result = collection.find_one(query_filter)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return result
    
    # Define the method to authenticate an existing user entry in the database
    def authenticate_user(self, username, password):
        # Create a authenication flag
        is_authenticated = False
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")

            # Define query
            query_filter = { "username":  username}
            
            # Authentication logic
            result = collection.find_one(query_filter)
            if result is not None:
                if result["username"] == username and result["password"] == password:
                    is_authenticated = True
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return is_authenticated
    
    # Define the method to update an existing user entry in the database
    def update_user(self, user):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")
            
            # Define query
            query_filter = { "_id": user.get_user_id() }
            update_operation = {
                "$set": {
                    "username": user.get_username(), 
                    "password": user.get_password()
                    }}
            
            # Modification logic
            collection.update_one(query_filter, update_operation)
        except Exception as e:
            print(e)
        return 1
    
    # Define the method to delete an existing user entry from the database
    def delete_user(self, user):
        # Create a new client and connect to the server
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")

            # Define query
            query_filter = { "_id": user.get_user_id() }
            
            # Deletion logic
            collection.delete_one(query_filter)
        except Exception as e:
            print(e)
        return 1