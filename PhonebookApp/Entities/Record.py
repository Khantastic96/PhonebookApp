# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:19 2024

@author: Sharek Khan
"""

# Import modules
from datetime import date

# Define constants
DAYS_IN_MONTH = 30.4375
DAYS_IN_YEAR = 365.25

class Record:
    # Define the init method/class constructor
    def __init__(self):
        self.__name = ""
        self.__phone_number = ""
        self.__email = ""
        self.__address = ""
        self.__city = ""
        self.__province = ""
        self.__postal_code = ""
        self.__date_of_birth = ""
        self.__age = 0.0
        
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
    
    # Define the mutator to the name field
    def set_name(self, new_name):
        self.__name = new_name
        
    # Define the mutator to the phone_number field
    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number
        
    # Define the mutator to the email field
    def set_email(self, new_email):
        self.__email = new_email
        
    # Define the mutator to the address field
    def set_address(self, new_address):
        self.__address = new_address
        
    # Define the mutator to the city field
    def set_city(self, new_city):
        self.__city = new_city
        
    # Define the mutator to the province field
    def set_province(self, new_province):
        self.__province = new_province
        
    # Define the mutator to the postal_code
    def set_postal_code(self, new_postal_code):
        self.__postal_code = new_postal_code
        
    # Define the mutator to the date_of_birth
    def set_date_of_birth(self, new_date_of_birth):
        self.__date_of_birth = new_date_of_birth
        self.__age = self.calculate_age()
        
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
    
    # Define to method to stringify an object when called through console ouput
    def __str__(self):
        record = (self.__name + ", " + self.__age +
        "\n\t#: " + self.__phone_number +
        "\n\t@: " + self.__email + 
        "\n\t^: " + self.__address + ", " + self.__city + ", " + self.__province + " " + self.__postal_code +
        "\n\t!: " + self.__date_of_birth)
        return record
