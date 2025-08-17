# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 02:09:48 2025

@author: khasharek
"""

import os
from dotenv import load_dotenv

# Load vairables from .env into environment
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("Missing MongoDB connection string. Check your .env file.")