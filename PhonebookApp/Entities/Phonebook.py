# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:01:19 2024

@author: Sharek Khan
"""

# Import modules
from Entities import User
from Entities import Record

class Phonebook:
    # Define the init method/class constructor
    def __init__(self, user, records):
        # Initialize User
        self.set_user(user)
        
        # Initialize Records
        self.set_records(records)
    
    # Define the accessor for the user field
    def get_user(self):
        return self.__user
    
    # Define the accessor for the records field
    def get_records(self):
        return self.__records
    
    # Define the mutator for the user field
    def set_user(self, new_user):
        self.__user.set_username(new_user.get_username())
        self.__user.set_password(new_user.get_password())
    
    # Define the mutator for the records field
    def set_records(self, new_records):
        for record in new_records:
            self.__records.append(record)
    
    # Define the method to add a new record to the phonebook
    def add_record(self, record):
        # Insertion logic
        if record != None:
            self.__records.append(record)
            return 1
        return 0
    
    # Define the method to list existing records in the phonebook
    def list_records(self):
        # Listing logic
        for x in self.__records:
            print(x);
        
    # Define the method to modify existing records in the phonebook
    def modify_record(self, record):
        # Modifying logic
        index = self.__records.index(record)
        self.__records[index].set_name(record.get_name())
        self.__records[index].set_phone_number(record.get_phone_number())
        self.__records[index].set_email(record.get_email())
        self.__records[index].set_address(record.get_address())
        self.__records[index].set_city(record.get_city())
        self.__records[index].set_province(record.get_province())
        self.__records[index].set_postal_code(record.get_postal_code())
        self.__records[index].set_date_of_birth(record.get_date_of_birth())
        return 1
    
    # Define the method to search existing records in the phonebook
    def search_records(self, name):
        # Searching logic
        for record in self.__records:
            if record.getName() == name:
                return record
        return None
    
    # Define the method to delete an existing record from the phonebook
    def delete_record(self, record):
        # Deleting logic
        self.__records.remove(record)
        return 1