# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:01:19 2024

@author: Sharek Khan
"""

# Import modules
from .User import User
from .Record import Record
import re

# Define constants
PHONEBOOK_ID_REGEX = r"^[A-Z]{3}[0-9]{4}_[A-Z]{2}$"

class Phonebook:
    # Define the init method/class constructor
    def __init__(self):
        self.__phonebook_id = ""
        self.__user = User()
        self.__records = []
    
    # Define the accessor for the phonebook_id field
    def get_phonebook_id(self):
        return self.__phonebook_id
    
    # Define the accessor for the user field
    def get_user(self):
        return self.__user
    
    # Define the accessor for the records field
    def get_records(self):
        return self.__records
    
    # Define the generator for the phonebook_id field
    def generate_phonebook_id(self):
        self.__phonebook_id = self.__user.get_user_id() + "_" + "PB"
        
    # Define the mutator for the phonebook_id field
    def set_phonebook_id(self, new_phonebook_id):
        if re.match(PHONEBOOK_ID_REGEX, new_phonebook_id):
            self.__phonebook_id = new_phonebook_id
        else:
            raise ValueError("Expected format: ABC1234_PB, got invalid entry")
    
    # Define the mutator for the user field
    def set_user(self, new_user):
        # Check for NoneType parameter
        if new_user is not None:
            self.__user.set_user_id(new_user.get_user_id())
            self.__user.set_username(new_user.get_username())
            self.__user.set_password(new_user.get_password())
        else:
            raise TypeError("Expected User object, got NoneType entry")
    
    # Define the mutator for the records field
    def set_records(self, new_records):
        # Check for NoneType parameter
        if new_records is not None:
            for record in new_records:
                self.__records.append(record)
        else:
            raise ValueError("Expected collection of Records, got NoneType entry")

    # Define the method to add a new record to the phonebook
    def add_record(self, record):
        # Check for NoneType parameter
        if record is not None:
            # Insertion logic
            self.__records.append(record)
            return 1
        else:
            raise ValueError("Expected Record object, got NoneType entry")
        return 0
    
    # Define the method to list existing records in the phonebook
    def list_records(self):
        # Listing logic
        for x in self.__records:
            print(x);
        
    # Define the method to modify existing records in the phonebook
    def modify_record(self, record):
        # Check for NoneType parameter
        if record is not None:
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
        else:
            raise ValueError("Expected Record object, got NoneType entry")
        return 0
    
    # Define the method to search existing records in the phonebook
    def search_records_by_name(self, name):
        # Searching logic
        records = []
        # Check with partial name
        if len(str.split(name, " ")) <= 1:
            for record in self.__records:
                f_name, l_name = str.split(record.get_name(), " ")
                partial_match = True
                # Check for all possible partial match conditions
                if len(name) > len(f_name) and len(name) > len(l_name):
                    partial_match = False
                elif len(name) <= len(f_name) and len(name) > len(l_name):
                    for i in range(0, len(name)):
                        if name[i] != f_name[i]:
                            partial_match = False
                            break
                elif len(name) > len(f_name) and len(name) <= len(l_name):
                    for i in range(0, len(name)):
                        if name[i] != l_name[i]:
                            partial_match = False
                            break
                else:
                    for i in range(0, len(name)):
                        if name[i] != f_name[i] and name[i] != l_name[i]:
                            partial_match = False
                            break
                if partial_match:
                    records.append(record)
        # Check with partial full name
        else:
            for record in self.__records:
                r_f_name, r_l_name = str.split(record.get_name(), " ")
                f_name, l_name = str.split(name, " ")
                partial_match = True
                # Check for all possible partial match conditions
                if f_name == r_f_name and len(l_name) <= len(r_l_name):
                    for i in range(0, len(l_name)):
                        if l_name[i] != r_l_name[i]:
                            partial_match = False
                            break
                else:
                    partial_match = False
                if partial_match:
                    records.append(record)
        return records

    def search_record_by_phone_number(self, phone_number):
        # Check for NoneType parameter
        if phone_number is not None:
            # Searching logic
            for record in self.__records:
                if phone_number == record.get_phone_number():
                    return record
        else:
            raise ValueError("Expected standard 10-digit phone number, got NoneType entry")
        return None

    def search_record_by_email(self, email):
        # Check for NoneType parameter
        if email is not None:
            # Searching logic
            for record in self.__records:
                if email == record.get_email():
                    return record
        else:
            raise ValueError("Expected standard email, got NoneType entry")
        return None

    # Define the method to delete an existing record from the phonebook
    def delete_record(self, record):
        # Check for NoneType parameter
        if record is not None:
            # Deleting logic
            self.__records.remove(record)
            return 1
        else:
            raise ValueError("Expected Record object, got NoneType entry")
        return 0
    
    # Define the method to check for duplicate records with the same values
    def is_duplicate(self, record):
        # Check for empty phonebook
        if len(self.__records) < 1:
            return False
        # Check for NoneType parameter
        if record is not None:
            # Check for duplicate entries (1:1)
            for r in self.__records:
                if record.get_name() != r.get_name():
                    return False
                if record.get_phone_number() != r.get_phone_number():
                    return False
                if record.get_email() != r.get_email():
                    return False
                if record.get_address() != r.get_address():
                    return False
                if record.get_city() != r.get_city():
                    return False
                if record.get_province() != r.get_province():
                    return False
                if record.get_postal_code() != r.get_postal_code():
                    return False
                if record.get_date_of_birth() != r.get_date_of_birth():
                    return False
        else:
            raise ValueError("Expected Record object, got NoneType entry")
            return False
        return True
