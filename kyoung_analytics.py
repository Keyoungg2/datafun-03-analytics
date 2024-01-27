""" This is for Project 3 to show learned skills using git and fectching different data types.
    The main objective being to create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats."""
    
#Standard Library imports
import csv
import json
from pathlib import Path

#imports from virtual environment
import requests
import pandas as pd
import numpy as np
import xlrd

#import pervious modules
import Key2Analytic_projsetup
import Key_2_Analytics_utils

#Defined variable
yourname_attr_my_name_string: str = "Name: Kareem Young"








def main():
    ''' Main function to demonstrate module capabilities. '''

print(f"Name: {yourname_attr_my_name_string}")