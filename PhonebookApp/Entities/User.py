# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:55 2024

@author: Sharek Khan
"""

# Import modules
import re

# Define constants
USER_ID_REGEX = r"^[A-Z]{3}[0-9]{4}$"
FIRST_NAME_REGEX = r"^[A-Za-z]+$"
LAST_NAME_REGEX = r"^(?:\s[A-Za-z]+)*$"
PHONE_NUMBER_REGEX = r"^[0-9]{10}$"
USERNAME_REGEX = r"^[A-Za-z0-9._-]{6,20}$"
PASSWORD_REGEX = r"^[A-Za-z0-9]{6,20}$"

class User:
    # Define the init method/class constructor
    def __init__(self):
        self.__user_id = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__phone_number = ""
        self.__username = ""
        self.__password = ""
    
    # Define the accessor to the user_id field
    def get_user_id(self):
        return self.__user_id

    # Define the accessor to the first_name field
    def get_first_name(self):
        return self.__first_name

    # Define the accessor to the last_name field
    def get_last_name(self):
        return self.__last_name
    
    # Define the accessor to the phone_number field
    def get_phone_number(self):
        return self.__phone_number

    # Define the accessor to the username field
    def get_username(self):
        return self.__username

    # Define the accessor to the password field
    def get_password(self):
        return self.__password
    
    # Define the generator for the user_id field
    def generate_user_id(self):
        l_name = self.get_last_name()
        p_number = self.get_phone_number()
        n = 0
        
        # Iterate through first 3 characters for last_name
        while(n < 3):
            # Append to user_id
            self.__user_id = self.__user_id + l_name[n].upper()
            # Increment the value of n
            n = n + 1
            
        # Reset n
        n = 4
        
        # Iterate through last 4 characters for phone_number
        while(n > 0):
            # Append to user_id
            self.__user_id = self.__user_id + p_number[len(p_number) - n]
            # Increment the value of n
            n = n - 1
        
    # Define the mutator to the user_id field
    def set_user_id(self, new_user_id):
        if re.match(USER_ID_REGEX, new_user_id):
            self.__user_id = new_user_id
        else:
            raise ValueError("Expected format: ABC1234, got invalid entry")
    
    # Define the mutator to the first_name field
    def set_first_name(self, new_first_name):
        if re.match(FIRST_NAME_REGEX, new_first_name):
            self.__first_name = new_first_name
        else:
            raise ValueError("Expected a name with alpha characters, got invalid entry")

    # Define the mutator to the last_name field
    def set_last_name(self, new_last_name):
        if re.match(LAST_NAME_REGEX, new_last_name):
            self.__last_name = new_last_name
        else:
            raise ValueError("Expected at least a name with alpha characters, got invalid entry")
    
    # Define the mutator to the phone_number field
    def set_phone_number(self, new_phone_number):
        if re.match(PHONE_NUMBER_REGEX, new_phone_number):
            self.__phone_number = new_phone_number
        else:
            raise ValueError("Expected a standard 10-digit phone number, got invalid entry")

    # Define the mutator to the username field
    def set_username(self, new_username):
        if re.match(USERNAME_REGEX, new_username):
            self.__username = new_username
        else:
            raise ValueError("Expected a username with 6 to 20 ASCII characters, got invalid entry")

    # Define the mutator to the password field
    def set_password(self, new_password):
        if re.match(PASSWORD_REGEX, new_password):
            self.__password = new_password
        else:
            raise ValueError("Expected a password with 6 to 20 alphanumerical characters, got invalid entry")