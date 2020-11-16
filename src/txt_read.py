# Created By: Hrithik Bansal
# Contact Me: hrithikbansal70@gmail.com | www.hrithikbansal.com
# Date: 06/15/2020
# Description: A simple python program which converts all text in an
#              txt document which contains emails into a single CSV
#              file containing all the emails, removing duplicates and
#              other unnecessary text.

# Dependencies: run the shell script lib to install the dependencies

import csv
import pandas as pd
import re

# Source file which contains the emails/email values
file = open('email_list.txt', 'r')

# Regex to match generic emails
em_regex = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'

# Some Variables for Data Keeping
lst = []
# Set is used to compile the data to avoid duplicates
unq = set()

for val in file:
    # All values are converted to lower case and space is stripped from the
    # left in order to filter data before regex matching
    val = val.lower().lstrip()
    emails = re.findall(em_regex, val)
    if emails is None:
        pass
    else:
        for email in emails:
            unq.add(email)

# Convert the set into a list and sort it lexicographically
# for easy manipulation
lst = list(unq)        
lst.sort()
# print(lst) # Uncomment to view all emails extracted from the data 
print(len(lst)) # Gives the length of the list/number of data entries

# Convert the list into a CSV file for direct import into E-mail
# management suite (GMail, Outlook etc.)
dict = {'E-mails':lst} # Add a header for aesthetics
df = pd.DataFrame(dict)
# print(df) # Uncomment to view the data frame
df.to_csv('email1.csv', index = False) 

print("All Text Successfully Converted to a CSV File!")
