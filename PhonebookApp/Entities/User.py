# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:02:55 2024

@author: Sharek Khan
"""

class User:
    # Define the init method/class constructor
    def __init__(self):
        self.__userid = ""
        self.__fname = ""
        self.__lname = ""
        self.__phone_number = ""
        self.__username = ""
        self.__password = ""
    
    # Define the accessor to the userid field
    def get_userid(self):
        return self.__userid

    # Define the accessor to the username field
    def get_username(self):
        return self.__username

    # Define the accessor to the password field
    def get_password(self):
        return self.__password
    
     # Define the accessor to the fname field
    def get_fname(self):
        return self.__fname

    # Define the accessor to the lname field
    def get_lname(self):
        return self.__lname
    
    # Define the accessor to the lname field
    def get_phone_number(self):
        return self.__phone_number

    # Define the userid field
    def gen_userid(self):
        lname = self.get_lname()
        phone_num = self.get_phone_number()
        
        N = 3
        # iterate loop
        while(N > 0):
 
            # print character
            print(lname[-N], end='')
 
            # decrement the value of N
            N = N-1
        
        P = 4
        # iterate loop
        while(P > 0):
 
            # print character
            print(phone_num[-P], end='')
 
            # decrement the value of P
            P = P-1
        
        self.__userid = lname+phone_num
        print(self.__userid)

    # Define the mutator to the username field
    def set_username(self, new_username):
        self.__username = new_username

    # Define the mutator to the password field
    def set_password(self, new_password):
        self.__password = new_password
        
     # Define the accessor to the fname field
    def set_fname(self, new_fname):
        self.__fname = new_fname

    # Define the accessor to the lname field
    def set_lname(self, new_lname):
        self.__lname = new_lname
    
    # Define the accessor to the lname field
    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number