# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:01:19 2024

@author: Sharek Khan
"""

class Phonebook:
    # Define the init method/class constructor
    def __init__(self, records):
        self.__records = records
    
    # Define the accessor for the records field
    def get_records(self):
        return self.__records
    
    # Define the mutator for the records field
    def set_records(self, new_records):
        self.__records = new_records
    
    # Define the method to add a new record to the phonebook
    def add_record(self, record):
        # Insertion logic
        return 1
    
    # Define the method to list existing records in the phonebook
    def list_records(self):
        # Listing logic
        print("Placehold text...")
        
    # Define the method to modify existing records in the phonebook
    def modify_record(self):
        # Modifying logic
        return 1
    
    # Define the method to search existing records in the phonebook
    def search_records(self):
        # Searching logic
        return 1
    
    # Define the method to delete an existing record from the phonebook
    def delete_record(self):
        # Deleting logic
        return 1