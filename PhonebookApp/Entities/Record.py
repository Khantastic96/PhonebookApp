# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:19 2024

@author: Sharek Khan
"""

# Import modules
from datetime import date
import math
import re

# Define constants
RECORD_ID_REGEX = r"^[A-Z]{3}[0-9]{4}_[A-Z]{2}_[A-Z][0-9]+$"
PHONEBOOK_ID_REGEX = r"^[A-Z]{3}[0-9]{4}_[A-Z]{2}$"
NAME_REGEX = r"^[A-Za-z]+(?:\s[A-Za-z]+)*$"
PHONE_NUMBER_REGEX = r"^[0-9]{10}$"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
ADDRESS_REGEX = r"^[0-9]+[A-Za-z]?\s+[\w\s.-]+$"
CITY_REGEX = r"^[A-Za-z]+(?:\s[A-Za-z]+)*$"
PROVINCE_REGEX = r"^[A-Z]{2}$"
POSTAL_CODE_REGEX = r"^[A-Za_z][0-9][A-Za-z][ -]?[0-9][A-Za-z][0-9]$"
DATE_OF_BIRTH_REGEX = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
DAYS_IN_MONTH = 30.4375
DAYS_IN_YEAR = 365.25

class Record:
    # Define the init method/class constructor
    def __init__(self):
        self.__record_id = ""
        self.__phonebook_id = ""
        self.__name = ""
        self.__phone_number = ""
        self.__email = ""
        self.__address = ""
        self.__city = ""
        self.__province = ""
        self.__postal_code = ""
        self.__date_of_birth = ""
        self.__age = 0.0

    # Define the accessor to the record_id field
    def get_record_id(self):
        return self.__record_id

    # Define the accessor to the phonebook_id field
    def get_phonebook_id(self):
        return self.__phonebook_id

    # Define the accessor to the name field
    def get_name(self):
        return self.__name
    
    # Define the acessor to the phone_number field
    def get_phone_number(self):
        return self.__phone_number
    
    # Define the accessor to the email field
    def get_email(self):
        return self.__email
    
    # Define the accessor to the address field
    def get_address(self):
        return self.__address
    
    # Define the accessor to the city field
    def get_city(self):
        return self.__city
    
    # Define the accessor to the province field
    def get_province(self):
        return self.__province
    
    # Define the accessor to the postal_code field
    def get_postal_code(self):
        return self.__postal_code
    
    # Define the accessor to the date_of_birth field
    def get_date_of_birth(self):
        return self.__date_of_birth
    
    # Define the accessor to the age field
    def get_age(self):
        return self.__age
    
    # Define the generator for the record_id field
    def generate_record_id(self, phonebook_id, record_no):
        self.__record_id = phonebook_id + "_" + "R" + str(record_no)

    # Define the mutator to the record_id field
    def set_record_id(self, new_record_id):
        if re.match(RECORD_ID_REGEX, new_record_id):
            self.__record_id = new_record_id
        else:
            raise ValueError("Expected format: ABC1234_PB_R1, got invalid entry")

    # Define the mutator to the phonebook_id field
    def set_phonebook_id(self, new_phonebook_id):
        if re.match(PHONEBOOK_ID_REGEX, new_phonebook_id):
            self.__phonebook_id = new_phonebook_id
        else:
            raise ValueError("Expected format: ABC1234_PB, got invalid entry")

    # Define the mutator to the name field
    def set_name(self, new_name):
        if re.match(NAME_REGEX, new_name):
            self.__name = new_name
        else:
            raise ValueError("Expected at least a name with alpha characters, got invalid entry")
        
    # Define the mutator to the phone_number field
    def set_phone_number(self, new_phone_number):
        if re.match(PHONE_NUMBER_REGEX, new_phone_number):
            self.__phone_number = new_phone_number
        else:
            raise ValueError("Expected a standard 10-digit phone number, got invalid entry")
        
    # Define the mutator to the email field
    def set_email(self, new_email):
        if re.match(EMAIL_REGEX, new_email):
            self.__email = new_email
        else:
            raise ValueError("Expected format: username@domain.com, got invalid entry")
        
    # Define the mutator to the address field
    def set_address(self, new_address):
        if re.match(ADDRESS_REGEX, new_address):
            self.__address = new_address
        else:
            raise ValueError("Expected standard address with alphanumerical characters, got invalid entry")
        
    # Define the mutator to the city field
    def set_city(self, new_city):
        if re.match(CITY_REGEX, new_city):
            self.__city = new_city
        else:
            raise ValueError("Expected standard city with alpha characters, got invalid entry")
        
    # Define the mutator to the province field
    def set_province(self, new_province):
        if re.match(PROVINCE_REGEX, new_province):
            self.__province = str.upper(new_province)
        else:
            raise ValueError("Expected format: AB, got invalid entry")
        
    # Define the mutator to the postal_code
    def set_postal_code(self, new_postal_code):
        if re.match(POSTAL_CODE_REGEX, new_postal_code):
            self.__postal_code = new_postal_code
        else:
            raise ValueError("Expected format: A1B2C3, got invalid entry")
        
    # Define the mutator to the date_of_birth
    def set_date_of_birth(self, new_date_of_birth):
        if re.match(DATE_OF_BIRTH_REGEX, new_date_of_birth):
            self.__date_of_birth = new_date_of_birth
            self.__age = math.floor(self.calculate_age())
        else:
            raise ValueError("Expected format: DD/MM/YYYY, got invalid entry")
        
    # Define the method to calculate the age
    def calculate_age(self):
        # Get current date, delimit it by '/'
        today = date.today()
        today_delim = today.strftime("%d/%m/%Y").split('/')
        
        # Delimit date of birth by '/'
        dob_delim = self.__date_of_birth.split('/')
        
        # Substitute values as integers
        today_d = int(today_delim[0])
        today_m = int(today_delim[1])
        today_y = int(today_delim[2])
        dob_d = int(dob_delim[0])
        dob_m = int(dob_delim[1])
        dob_y = int(dob_delim[2])
        
        # Calculate the difference to find the age
        today_in_days = self.calculate_date_in_days(today_d, today_m, today_y)
        dob_in_days = self.calculate_date_in_days(dob_d, dob_m, dob_y)
        difference = today_in_days - dob_in_days
        
        # Calculate and return the age
        return difference / DAYS_IN_YEAR
        
    # Define the method to calculate a date in accumulated days
    def calculate_date_in_days(self, date, month, year):
        return date + (month-1)*(DAYS_IN_MONTH) + (year-1)*(DAYS_IN_YEAR)
    
    # Define the method to stringify an object when called through console output
    def __str__(self):
        record = (self.__name + ", " + str(math.floor(self.__age)) +
        "\n\t#: " + self.__phone_number +
        "\n\t@: " + self.__email + 
        "\n\t^: " + self.__address + ", " + self.__city + ", " + self.__province + " " + self.__postal_code +
        "\n\t!: " + self.__date_of_birth)
        return record
