# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:05:44 2024

@author: Sharek Khan
"""

# Import modules
from http import client
from Entities.User import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://Omer123:abcefgh@phonebookappcluster.2tgxc.mongodb.net/?retryWrites=true&w=majority&appName=PhonebookAppCluster"


class UserDAO:
    # Create a new client and connect to the server
    client = MongoClient(URI, server_api=ServerApi('1'))
        
    # Send a ping to confirm a successful connection
    try:
        # Get databases
        database = client.get_database("PhonebookAppDB")
            
        # Get collections
        collection = database.get_collection("Users")
        
    except Exception as e:
       print(e)
       
    # Define the init method/class constructor
    def __init__(self):
        self.__user = User()


    # Define the method to insert a new user entry to the database
    def insert_user(self, user):
         # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")
            
            # Insertion logic
            result = collection.insert_one(
            { "_id": user.get_userid,
              "username" : user.get_username,
              "password" : user.get_password
            })
            print(result.acknowledged)
        
        except Exception as e:
            print(e)

        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to find an existing user entry in the database
    def find_user(self, username):
        
        
         # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Users")

            # Querying logic
            query_filter = { "username":  username}
            result = collection.find_one(query_filter)
            print(result)

        except Exception as e:
            print(e)

        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to update an existing user entry in the database
    def update_user(self, user):
        # Updating logic
        
          # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            collection = database.get_collection("Users")

            query_filter = { "username": user.get_username }
            update_operation = { "$set": { "username": user.set_username }, 
                                 "$set": { "password": user.set_password } }
            
            result = collection.update_one(query_filter, update_operation)
            
            print(result.modified_count)
        
        except Exception as e:
            print(e)
        
        return 1
    
    # Define the method to delete an existing user entry from the database
    def delete_user(self, user):
        # Deleting logic
        
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            collection = database.get_collection("Users")

            query_filter = { "username": user.get_username }
            result = collection.delete_one(query_filter)
            print(result.deleted_count)
        
        except Exception as e:
            print(e)
        
        return 1
