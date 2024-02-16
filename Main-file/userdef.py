#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv


# In[2]:


load=pd.read_fwf("uploads/test_lis.txt")


# In[3]:


load.head(5)


# In[4]:


import re
f = open('uploads/test_lis.txt', 'r')
content = f.read()

x = re.findall(r'MASS REPORT(.*?)LIST OF SMALLEST TIME-STEP VALUES', content, re.DOTALL)
content1 = ("".join(x))


# In[5]:


def write_to_file(file,data):
    with open(file,'w') as f:
        f.write(data)
        
write_to_file('k3.txt',content1)


# In[6]:


def remove_lines(file, start, end):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file,'w') as f:
        for line in lines[:start] + lines[end:]:
            f.write(line)
            
remove_lines('k3.txt', 0,6)


# In[7]:


def remove_lines(file, start, end):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file,'w') as f:
        for line in lines[:start] + lines[end:]:
            f.write(line)
            
remove_lines('k3.txt', 1806,1808)


# In[8]:


import csv
with open('k3.txt') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)


# In[9]:


cvc=pd.read_fwf('k3.txt',names=['PART',
                               'MTYP',
                               'NB. OF ELEMENTS',
                               'INPUT     ELEM. MASS',
                               'ADDED INIT MASS SCALE',
                               'ADDED DYN. MASS SCALE',
                               'ADDED NON-STRU. MASS',
                               'ADDED   MASSTRIM',
                              'ADDED NODAL MASS',
                               'FINAL     ELEM. MASS',
                              'FINAL NODAL MASS'],
                            colspecs='infer',widths=None, infer_nrows=1806)

cvc.to_csv('k4.csv',index=None)


# In[10]:


qwe=pd.read_csv('k4.csv')
qwe.head()


# In[11]:


qwe.info()


# In[12]:


def percentage_change(col1,col2):
#        if col1 == 0.0:
#          return col2 * 100

    return ((col2 - col1) / col1) * 100


qwe['Percentage Increased'] = percentage_change(qwe['INPUT     ELEM. MASS'], qwe['FINAL     ELEM. MASS'])


# In[13]:


qwe.head(150)


# In[14]:


qwe.to_csv('k4.csv',index=False)


# In[15]:


df = pd.read_csv('k4.csv')

# fill NaN values with 0.0 in a specific column
df['Percentage Increased'].fillna(0.0, inplace=True)

# write the updated DataFrame to a new CSV file
df.to_csv('k4.csv', index=False)


# In[16]:


df.info()


# In[17]:


import csv

# Define the path to the input and output CSV files
input_file = 'k4.csv'
output_file = 'output.csv'

# Define the columns you want to extract from the input file
columns_to_extract = ['PART', 'NB. OF ELEMENTS', 'Percentage Increased']

# Open the input and output CSV files
with open(input_file, 'r', newline='') as input_csv_file, \
     open(output_file, 'w', newline='') as output_csv_file:

    # Create CSV reader and writer objects
    csv_reader = csv.DictReader(input_csv_file)
    csv_writer = csv.DictWriter(output_csv_file, fieldnames=columns_to_extract)

    # Write headers to output CSV file
    csv_writer.writeheader()

    # Loop through each row in the input CSV file and extract specific columns
    for row in csv_reader:
        extracted_data = {column: row[column] for column in columns_to_extract}
        csv_writer.writerow(extracted_data)


# In[18]:


yu= pd.read_csv("output.csv")
yu.info()


# In[19]:


import csv

# Define the path to the input and output CSV files
input_file = 'output.csv'
output_file = 'k6.csv'

# Define the column you want to check for values greater than the user-defined value
search_column = 'Percentage Increased'



# Define the user-defined value
# user_defined_value = float(input("Enter Number\n"))
user_defined_value = float(input("Enter Number:\n"))

# Open the input and output CSV files
with open(input_file, 'r', newline='') as input_csv_file, \
     open(output_file, 'w', newline='') as output_csv_file:

    # Create CSV reader and writer objects
    csv_reader = csv.DictReader(input_csv_file)
    csv_writer = csv.DictWriter(output_csv_file, fieldnames=csv_reader.fieldnames)

    # Write headers to output CSV file
    csv_writer.writeheader()

    # Loop through each row in the input CSV file and extract rows where the value in the search column is greater than the user-defined value
    for row in csv_reader:
        if float(row[search_column]) > user_defined_value:
            csv_writer.writerow(row)


# # In[ ]:

import matplotlib.pyplot as plt
import pandas as pd

# Load a CSV file into a Pandas dataframe
data = pd.read_csv('k6.csv')

# Convert the y column values to lakhs
# data['PART'] = data['PART'] / 10000000

# Plot a line chart of the data
plt.scatter(data['Percentage Increased'], data['PART'])

# Add labels and title to the chart
plt.xlabel('Percentage Increased')
plt.ylabel('PART(in Lakhs)')
plt.title('Data Visualization')

# Show the chart
plt.show()