# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:19 2024

@author: Sharek Khan
"""

class Record:
    # Define the init method/class constructor
    def __init__(self):
        self.__name
        self.__phone_number
        self.__email
        self.__address
        self.__city
        self.__province
        self.__postal_code
        self.__date_of_birth
        self.__age
        
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
        
    # Define the method to calculate the age
    def calculate_age(self):
        # Calculation logic
        return 1 