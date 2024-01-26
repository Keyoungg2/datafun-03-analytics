""" This document is being used for Key2Analytics Consulting company. This code will be updated as analytical data is imported, processed, and stored for future reference. """
#Please be sure to have Math and Statistics import in order to ran statistical analysis on data

import math
import statistics

def main(): # This will be the main function for displaying the information.
    print(byline)
    
#Defined variables  
company_name: str = "Key2Analytics Consulting"
completed_project: int = 10
#Below is the number of days each project took.
completed_project_days = list = [5,10,8,7,7,4,6,12,15,9]
count_active_projects: int = 5
Goal_completeion_time_in_days: float = 15.5
company_rating: int = 4
LLC_business_type: bool = True
Employees: list = ['Dave (Visualization)', 'Key (Manager)', 'Shelby (Analyst 1)', 'Cho (Analyst 2']
Rating_Review: list = [5,2,5,3,4,4,5,2,5,4,4,5]
#Rating scale 1-5 int
active_project_number: list = ['AA4', 'BC3','CC', 'DA78', 'HG4']

#F-strings from  non variables  above
intro: str = "Hello welcome to Key2 Analytics. We are glad you are interested in our services look below to find information about our team and our performance"
line_of_business: str = f"Are we a small Local LLC business? This is {LLC_business_type}."
current_employees: str = f"Our current employees and there positions are {Employees}."
company_overall_rating: str = f"Our current review rating is {company_rating}."
active_projects: str = f"We are currently working on {count_active_projects} projects."

lowreview = min(Rating_Review)
highreview = max(Rating_Review)
total = sum(Rating_Review)
count = len(Rating_Review)
mean = statistics.mean(Rating_Review)
mode = statistics.mode(Rating_Review)
median = statistics.median(Rating_Review)
Standard_deviation = statistics.stdev(Rating_Review)

#Creating string for company stats called on byline introduction
company_stats_string: str = f"""
Descriptive Statistics for company performance
lowest rated review: {lowreview}
highest rated review: {highreview}
Number of review: {count}
total review rating: {total}
average rating: {mean}
most common rating: {mode}
median rating: {median}
"""

byline: str = f"""
{intro}
{line_of_business}
{current_employees}
{active_projects}
{company_stats_string}
"""

#code can only run from this script
if __name__ == '__main__':
    main()



