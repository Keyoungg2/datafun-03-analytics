""" This is for Project 3 to show learned skills using git and fectching different data types.
    The main objective being to create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats."""
    
#Standard Library imports
import csv
import json
from pathlib import Path
from pip import pandas as pd


#imports from virtual environment
from pip import requests
from AppData.Local.Programs.Python.Python312.Lib.test.test_shutil import write_test_file

#import pervious modules
import Key2Analytic_projsetup
import Key_2_Analytics_utils

#Defined variable
yourname_attr_my_name_string: str = "Name: Kareem Young"
projectname: str = "CSIS 44608 Module 3 Project"

#Defined Functions
# Function created to call and write text file creating data.txt file
def write_txt_file(folder_name, filename, data): 
    # Create path
    file_path = Path(folder_name).joinpath(filename)

    with file_path.open('w', encoding='utf-8') as file: 
        file.write(data)

#Text file
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
      Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
      file_path = Path(folder_name).joinpath(filename) # uses pathlib to join paths
      with file_path.open('w') as file:
            file.write(response.text.lower())
            print(f"Text data has been saved as {filename}")
   
    """Fetch text data from a URL and writes it to a file.
    Failed to fetch text will prompt for any issues with fetch.
    param folder_name: Name of the folder to save the data to
    param filename: Name of the file to save the data to
    param url: URL to fetch the data from
    """
#Excel file
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Excel data saved to {file_path}")
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")
def main():
    ''' Main function to demonstrate module capabilities. '''

print(f"Name: {yourname_attr_my_name_string}")
print (f"{projectname}")
