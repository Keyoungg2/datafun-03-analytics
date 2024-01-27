""" This is for Project 3 to show learned skills using git and fectching different data types.
    The main objective being to create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats."""
    
#Standard Library imports
import csv
import json
from pathlib import Path
import requests
from io import StringIO
import pandas as pd


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
    try:
        response: requests.get(url)
        response.raise_for_status() 
        
        if response.status_code == 200:
            Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
            file_path = Path(folder_name).joinpath(filename) # uses pathlib to join paths
            with file_path.open('w') as file:
                file.write(response.text.lower())
            print(f"Text data has been saved {folder_name}")
        else: requests.exceptions.RequestException
        print(f"Error Fetching data from txt: {url}") 
    except requests.exceptions.RequestException as err:
        print(f"Error fetching data from {url}: {err}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
   
    """Fetch text data from a URL and writes it to a file.
    Failed to fetch text will prompt for any issues with fetch.
    parameters
    foldername: name of the folder that data will be save to 
    filename: name of files that is created from fetch
    url: url which data will come from"
    """
       
def process_txt_data(folder_name: str, filename: str, results):
    with open(Path(folder_name).joinpath(filename), 'r') as file:
        raw_words = file.read().split() # splits text into strings
    words = [] # Empty list to store words without non-word characters
    for word in raw_words:
        word = requests.sub('[,()?.\";!-]', '', word) # removes non-word characters from each word
        word = word.lower() # converts each word to lowercase
        words.append(word)
        unique_words = set(words) # set to store unique words
    with open(Path(folder_name).joinpath(results), 'w') as file:
        file.write(f"Unique words: {len(unique_words)}\n")
        for word in unique_words:
            file.write(f"The word {word} appears {words.count(word)} times.\n")
    """
    Process the txt file data from txt and outputs txt file
    Paremeters
    folder_name: Name of saved folder where txt file is 
    filename: name of the txt file 
    results: name of statistical analysis  for count of times for each unique words
    """
    
#Excel file
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('wb') as file:
            file.write(response.content)
            print(f"Excel data saved to {file_path}")
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")
        
    """ Fetch excel data from URL line and creates a file.
    parameters
    foldername: name of the folder that data will be save to 
    filename: name of files that is created from fetch
    url: url which data will come from
    Print display of if fetch was successful or not"""
    
def process_excel_data(folder_name, filename, url):
    file_path = Path(folder_name).joinpath(filename)
    excel_data = pd.read_excel(file_path) #use pd.read_excel to for python to be able to read and get information from excel files
    excel_data_list = excel_data.values.tolist()
    
    entrees = []  
    for row in excel_data_list:
        entrees.append(row)
        
        total_games= 33
        isclub_index = 1  #use column IsClub and 1 is number for column. Python starts with 0. 
        gamesWon_index = 2 #use column games won and 1 is number for column.
        custom_message = f"""This Excel file shows data of {len(entrees)} football clubs.
            \nCork City is 1 of the {len(isclub_index)} football clubs and leading the league in wins with a total of {max(gamesWon_index)} wins. Leauge win average is {round(sum(gamesWon_index)/(total_games))} wins."""
       
    new_file_path = Path(folder_name).joinpath(url)
    with new_file_path.open('w') as file:
        file.write(custom_message)
        print(f"Text data saved to {new_file_path}")
       
        """ Process excel file  to create a file that displays fetched excel data from url.
        parameters
        foldername: name of the folder that data will be save to 
        filename: name of files that is created from fetch
        url: url which data will come from
        Entrees detail row infortion from excel. ColumnName_index is column which data will be pulled and used for statistical analysis, 
        custom message will print once a successful file has been created detailing analysis reported. """
        
#CVS file
def fetch_and_write_csv_data(folder_name, filename, url):
    '''
    Fetch CSV data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
            print(f"CSV data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def process_csv_file(folder_name,filename,results):
    with open(Path(folder_name).joinpath(filename), 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter= ',')
        states= []
        for row in reader:
            states.append(row)
            
    State_column_index = 0
    #states column number in CSV fil 0 = Column A. Python starts from 0
    usa_states = [int(row[State_column_index])]
    #count of rows in State column
    
    custom_message = f'''This csv file shows data for USA. They have a total of {len(usa_states)} states.'''
            
    new_file_path = Path(folder_name).joinpath(results)
    with new_file_path.open('w') as file:
        file.write(custom_message)
        print(f"Text data saved to {new_file_path}")
    '''Processes the data.csv file and outputs a txt file that shows the number of states in america.
    parameters
    folder_name: Name of the folder to find the file
    filename: Name of the file to open
    results: Name of the file to save the statistical analysis to
    ''' 

#JSON file
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
            print(f"JSON data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")
    '''
    Fetch JSON data from a URL and writes it to a file. If done correclty no issues a prompt of HSON data save. If issues occure at Failed to fetch data prompt will display check error code
    parameters:
    folder_name: Name of the folder to save the data to
    filename: Name of the file to save the data to
    url: URL to fetch the data from
    '''

def process_json_data(folder_name, filename, results):
    ''' Function to process a json file. It tells you the likes and dislikes of pets'''
    file_path = Path(folder_name).joinpath(filename)
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    custom_message = "This json file tells us the following information:\n"

    for obj in data:
        team_name = obj['team_name']
        stadium = obj['stadium']
        team_abbreviation = obj['team_abbreviation']

        # Print information for each pet
        info = (f"{team_name} abrrivation is {team_abbreviation} and play at {stadium}.\n")
        custom_message += info

    new_file_path = Path(folder_name).joinpath(results)
    with new_file_path.open('w') as file:
        file.write(custom_message)
        print(f"Text data saved to {new_file_path}")
    """
      Processes the data.json file and outputs a txt file thatdetails NFL teams and their stadiums.
    parameters:
    folder_name:  Name of the folder to find the file
    filename: Name of the file to open
    results: Name of the file to save the statistical analysis to
    
    """
       
        
def main():
   # Main function to demonstrate capabilities of fetching data from web sources and processing them for statistical analysis.
    print(f"Name: {yourname_attr_my_name_string}")
    print(f"{projectname}")

 # URLs with differnt data types
url_text = "https://archive.org/stream/damonpythiasplay00bani/damonpythiasplay00bani_djvu.txt"
url_excel = "https://github.com/jameskiernan1989/FixtureGenerator/raw/master/testdata.xls"
url_csv = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
url_json = "https://raw.githubusercontent.com/oritzio/football-database/master/USA_NFL.json"

# folder names to write data to
txt_folder_name = "data-txt"
excel_folder_name = "data-excel"
csv_folder_name = "data-csv"
json_folder_name = "data-json"
    
    # file names to write data to
txt_filename = 'data.txt'
excel_filename = 'data.xls'
csv_filename = 'data.csv'
json_filename = 'data.json'
    
    # fetch data and write to files
fetch_and_write_txt_data(txt_folder_name, txt_filename, url_text)
fetch_and_write_excel_data(excel_folder_name, excel_filename, url_excel)
fetch_and_write_csv_data(csv_folder_name, csv_filename,url_csv)
fetch_and_write_json_data(json_folder_name, json_filename, url_json)   
    # process data and write to files as text files
process_txt_data(txt_folder_name, txt_filename, 'results_txt.txt')
process_excel_data(excel_folder_name, excel_filename, 'results_excel.txt')
process_csv_file(csv_folder_name,csv_filename, 'results_csv.txt')
process_json_data(json_folder_name, json_filename, 'results_json.txt')

# conditional execution
if __name__ == "__main__":
    main()