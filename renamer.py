import glob
import csv
import os

# Change the directory if needed
#os.chdir()

# Change '.tiff' to the extension of the files you want to change
current_file_names = sorted(glob.glob('*.tiff'))

# Set the date which the pictures were taken
date_taken = '2018_10_19'

# Change 'IDs.csv' to the name of file containing the new file names
with open('IDs.csv', 'r') as f:
    reader = csv.reader(f)
    new_file_names = list(reader)

ext = []
for file in current_file_names:
    name, ext = os.path.splitext(file)

# Make a list of the new file names
new_name = []
for i in new_file_names:
    length = len(str(i).replace("['", '').replace("']", ''))
    if length == 1:
        i = '{}{}'.format('00000', i)
    elif length == 2:
        i = '{}{}'.format('0000', i)
    elif length == 3:
        i = '{}{}'.format('000', i)
    elif length == 4:
        i = '{}{}'.format('00', i)
    elif length == 5:
        i = '{}{}'.format('0', i)
    else:
        i = i
    new_name.append('{}{}{}{}'.format(date_taken, "_", i, ext))

# Join the current file names and the new file names into one list
names_list = zip(current_file_names, new_name)
for item in names_list:
    print(item)

# Rename the files
for item in names_list:
    os.rename(item[0], str(item[1]).replace("['", '').replace("']", ''))
