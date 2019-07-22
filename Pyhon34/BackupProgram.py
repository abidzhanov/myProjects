import os
import time


# Files that must be copied is gathered in one folder
source = ['"C:\\Users\Asus_Book\Documents\My documents"',
           'C:\\Users\Asus_Book\Documents\Book']

# The folder that stores files
target_dir = 'C:\\Backup' #!!!!

# The files are moved in zip archive
# present date is served as a subdirectory name
today = target_dir + os.sep + time.strftime('%Y%m%d')

# present date is served as a name of zip file
now = time.strftime('%H%M%S')

# create a directory if it does not exist
if not os.path.exists(today):
    os.mkdir(today) # creating a directory
    print('Directory created successfully', today)

# name of zip file 
target = today + os.sep + now + '.zip'

# Using a zip command to move files into zip archive
zip_command = "7z a {0} {1}".format(target, ' '.join(source))

# Running creating a zip copy
if os.system(zip_command) == 0:
    print('Backup is created successfully in', target)
else:
    print('Failed backuping files')

