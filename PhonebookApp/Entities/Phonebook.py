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
        record = Record();
        
        name = input('Enter your name: ');
        print('/n');
        phoneNumber = input('Enter your phone number: ');
        print('/n');
        email = input('Enter your email address: ');
        print('/n'); 
        address = input('Enter your street address: ');
        print('/n'); 
        city = input('Enter your city: ');
        print('/n'); 
        province = input('Enter your province: ');
        print('/n'); 
        postal_code = input('Enter your postal code: ');
        print('/n');
        date_of_birth = input('Enter your date of birth: ');
        print('/n'); 
        
        record.set_name(name);
        record.set_phone_number(phoneNumber);
        record.set_email(email);
        record.set_address(address);
        record.set_city(city);
        record.set_province(province);
        record.set_postal_code(postal_code);
        record.set_date_of_birth(date_of_birth);
               
        return 1
    
    # Define the method to list existing records in the phonebook
    def list_records(self):
        # Listing logic
        for x in self.__records:
            print(x);
        
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