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
            
            # Fetch queried record
            queried_record = collection.find_one(query_filter)
            fields_to_update = {}
            
            # Check for unchanged or null entries
            if record.get_name() != queried_record.get("name") and record.get_name() != None:
                fields_to_update["name"] = record.get_name()
            if record.get_phone_number() != queried_record.get("phone_number") and record.get_phone_number() != None:
                fields_to_update["phone_number"] = record.get_phone_number()
            if record.get_email() != queried_record.get("email") and record.get_email() != None:
                fields_to_update["email"] = record.get_email()
            if record.get_address() != queried_record.get("address") and record.get_address() != None:
                fields_to_update["address"] = record.get_address()
            if record.get_city() != queried_record.get("city") and record.get_city() != None:
                fields_to_update["city"] = record.get_city()
            if record.get_province() != queried_record.get("province") and record.get_province() != None:
                fields_to_update["province"] = record.get_province()
            if record.get_postal_code() != queried_record.get("postal_code") and record.get_postal_code() != None:
                fields_to_update["postal_code"] = record.get_postal_code()
            if record.get_date_of_birth() != queried_record.get("date_of_birth") and record.get_date_of_birth() != None:
                fields_to_update["date_of_birth"] = record.get_date_of_birth()
            if record.get_age() != queried_record.get("age") and record.get_age() != None:
                fields_to_update["age"] = record.get_age()
            
            # Modification logic (if necessary)
            if fields_to_update:
                update_operation = { "$set": fields_to_update }
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
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
