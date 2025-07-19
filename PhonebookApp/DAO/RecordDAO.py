# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 02:05:37 2024

@author: Sharek Khan
"""

# Import modules
from Entities.Record import Record
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI = "mongodb+srv://Omer123:abcefgh@phonebookappcluster.2tgxc.mongodb.net/?retryWrites=true&w=majority&appName=PhonebookAppCluster"
URI = "mongodb+srv://Sharek123:pointd3xt3r@phonebookappcluster.2tgxc.mongodb.net/?retryWrites=true&w=majority&appName=PhonebookAppCluster"

class RecordDAO:
    # Define the init method/class constructor
    def __init__(self):
        self.__record = Record()
        
    # Define the method to insert a new record entry to the database
    def insert_record(self, record):
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Insertion logic
            result = collection.insert_one(
                {"_id": record.get_record_id(),
                 "phonebook_id": record.get_phonebook_id(),
                 "name": record.get_name(),
                 "phone_number": record.get_phone_number(),
                 "email": record.get_email(),
                 "address": record.get_address(),
                 "city": record.get_city(),
                 "province": record.get_province(),
                 "postal_code": record.get_postal_code(),
                 "date_of_birth": record.get_date_of_birth(),
                 "age": record.get_age()})
            print(result.acknowledged)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to insert new record entries to the database
    def insert_records(self, records):
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Establish a sucessful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Records")
            
            # Insertion logic
            for record in records:
                # Define query
                query_filter = { "record_id": record.get_record_id() }
                
                # Search logic
                result = collection.find_one(query_filter)
                
                # Check for existing records
                if not result:
                    # Insert record
                    result = collection.insert_one(
                        {"_id": record.get_record_id(),
                         "phonebook_id": record.get_phonebook_id(),
                         "name": record.get_name(),
                         "phone_number": record.get_phone_number(),
                         "email": record.get_email(),
                         "address": record.get_address(),
                         "city": record.get_city(),
                         "province": record.get_province(),
                         "postal_code": record.get_postal_code(),
                         "date_of_birth": record.get_date_of_birth(),
                         "age": record.get_age()})
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1         
    
    # Define the method to find an existing record entry in the database
    def find_records(self, phonebook_id):
        # Create a return object of the query
        results = []
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Define query
            query_filter = { "phonebook_id": phonebook_id }

            # Search logic
            results = list(collection.find(query_filter))
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return results
    
    # Define the method to determine if a phonebook's record(s) exists in the database
    def has_records(self, phonebook_id):
        # Create a verification flag
        has_records = False
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Records")
            
            # Define query
            query_filter = { "phonebook_id": phonebook_id }
            
            # Verification logic
            result = collection.find_one(query_filter)
            if result:
                has_records = True
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return has_records        
        
    # Define the method to update an existing record entry in the database
    def update_record(self, record):
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Define query
            query_filter = {"_id": record.get_record_id() }
            update_operation = {"$set": { "name": record.get_name() },
                                "$set": { "phone_number": record.get_phone_number() },
                                "$set": { "email": record.get_email() },
                                "$set": { "address": record.get_address() },
                                "$set": { "city": record.get_city() },
                                "$set": { "province": record.get_province() },
                                "$set": { "postal_code": record.get_postal_code() },
                                "$set": { "date_of_birth": record.get_date_of_birth() }}

            # Modification logic
            result = collection.update_one(query_filter, update_operation)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to delete an existing record entry from the database
    def delete_record(self, record):
        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")
            
            # Get collections
            collection = database.get_collection("Records")

            # Define query
            query_filter = { "_id": record.get_record_id() }
            
            # Deletion logic
            result = collection.delete_one(query_filter)
            print(result.deleted_count)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
