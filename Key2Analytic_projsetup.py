''' This module provides functions for creating a series of project folders.This creates a folders system per year for projects details. '''

#Imported Python libraries 
import time
import pathlib
import math
import os
#Imported Python Project
import Key_2_Analytics_utils as utils

#printing byline
print(f'Byline: {utils.byline}')

#define of functions
def create_folder(folder_name:str) -> None:
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    print(f"Creating folder path: {folder_name}")
    #Para folder name: name of folder to be created. type: str
    
def create_employee_from_list(folder_name: str, folder_list: list) -> None:
    folder_name = folder_name.lower()
    create_folder (folder_name)
    for employee in folder_list:
        employee_folder = pathlib.Path(folder_name).joinpath(employee)
        create_folder(str(employee_folder))
        print(f"Creating folder for employee: {employee_folder}")
        
    '''
    Creates folders from a list of employeess names ans stores them in a parent folder.
    param folder_name: name of folder to be created for parent folder (Employee)
    param folder_list: list of course names, example: ['Dave (Visualization)', 'Key (Manager)']
    Print f string allows to see any folder creation. 
    '''
    
def create_folder_from_range(folder_name: str, start_year: int,end_year: int):
        folder_name=(folder_name)
        create_folder (folder_name)
        for year in range(start_year,end_year +1):
         pathlib.Path(str(year)).mkdir(exist_ok=True)
         print(f"Creating folder for year: {year}") 
        """"Creates a folder based on given 
            Param: business start type: int year (2020)   
            Param:end year type: int  year(2024) 
            exist_ok = true (will only created folder, if a folder without same name does not exist already).
        """
    
def create_prefixed_folders(folder_name: str, project_list: list, prefix: str):
    folder_name = folder_name.lower()
    create_folder(folder_name)
     
    for project in project_list:
        project_folder= pathlib.Path(folder_name).joinpath(prefix + project.lower())
        create_folder(str(project_folder)) 
    """
    Creates folders based off folder  based off project and project number
    Param: folder name type: str  (see folder_name in main), 
    Param: project list  type: listing (see active_projects in main),
    Param: prefix type: str  (seee prefix in main)"
    """
    
    
def create_folders_periodically(duration_sec: int, folder_name: str, number_of_folders: int, starting_number: int) -> None:
     folder_name = folder_name.lower()
     create_folder(folder_name)
     account_number = starting_number
     while number_of_folders > 0:
        time.sleep(duration_sec)
        account_folder = pathlib.Path(folder_name).joinpath(str(account_number))
        create_folder(account_folder)
        number_of_folders -= 1
        account_number += 1
""" Creates folders peroodically based off the following
    Parma: duration in seconds  type: int
    Param: folder_name: name of folder to be created  type: str
    Param: number that folders will start creating from type: int
"""
        
  
# Define main function
def main():
    '''
    Main function
    Calls function to create folders from various variables.
    '''
    #Call function 2 to create folders given a list 
    employee_name = ['Dave (Visualization)', 'Key (Manager)', 'Shelby (Analyst 1)', 'Cho (Analyst 2']  # list of employees
    create_employee_from_list(folder_name= 'employee', folder_list= employee_name)
    
    #Call function 1 to create folders for a range (e.g. years)
    create_folder_from_range(folder_name= 'K2A_Proj', start_year= 2020, end_year= 2024)
    
    #Call function 3 to create folders using comprehension
    active_projects = ['AA4', 'BC3','CC2', 'DA78', 'HG4'] # projects that have been taken on
    create_prefixed_folders(folder_name='Project', project_list=active_projects, prefix="Proj-")
    
    # Call function 4 to create folders periodically using while
    create_folders_periodically(duration_sec= 5, folder_name= "Account Number", number_of_folders= 9, starting_number= 2000)
    
# All clear module
if __name__ == '__main__':
  main()
    
main()