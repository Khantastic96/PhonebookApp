# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 02:05:37 2024

@author: Sharek Khan
"""

# Import modules
from Entities.Record import Record

class RecordDAO:
    # Define the init method/class constructor
    def __init__(self):
        self.__record = Record()
        
    # Define the method to insert a new record entry to the database
    def insert_record(self, record):
        # Insertion logic
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Insertion logic
            result = collection.insert_one(
                {"name": record.get_name,
                 "phone_number": record.get_phone_number,
                 "email": record.get_email,
                 "address": record.get_address,
                 "city": record.get_city,
                 "province": record.get_province,
                 "postal_code": record.get_postal_code,
                 "date_of_birth": record.get_date_of_birth})
            print(result.acknowledged)

        except Exception as e:
            print(e)

        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to find an existing record entry in the database
    def find_record(self, name):
        # Querying logic
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Establish a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Define query
            query_filter = {"name": name}

            # Search logic
            result = collection.find_one(query_filter)
        except Exception as e:
            print(e)
        finally:
            # Close the client
            client.close()
        return 1
    
    # Define the method to update an existing record entry in the database
    def update_record(self, record):
        # Updating logic
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            # Get collections
            collection = database.get_collection("Records")

            # Define query
            query_filter = {"name": name}
            update_operation = {"$set": {"name": record.set_name},
                                "$set": {"phone_number": record.set_phone_number},
                                "$set": {"email": record.set_email},
                                "$set": {"address": record.set_address},
                                "$set": {"city": record.set_city},
                                "$set": {"province": record.set_province},
                                "$set": {"postal_code": record.set_postal_code},
                                "$set": {"date_of_birth": record.set_date_of_birth}}

            # Modification logic
            result = collection.update_one(query_filter, update_operation)
        except Exception as e:
            print(e)
        return 1
    
    # Define the method to delete an existing record entry from the database
    def delete_record(self, record):
        # Deleting logic

        # Create a new client and connect to the server
        client = MongoClient(URI, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            # Get databases
            database = client.get_database("PhonebookAppDB")

            collection = database.get_collection("Records")

            query_filter = { "name": record.get_name }
            result = collection.delete_one(query_filter)
            print(result.deleted_count)

        except Exception as e:
            print(e)

        return 1
