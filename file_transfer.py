import shutil
import os

#set where the souce of the files are
source = '/Users/manda/OneDrive/Desktop/Folder A/'

#set the destination path to folderB
destination = '/Users/manda/OneDrive/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
        #we are saying move the files represented by 'i' to their new destination
        shutil.move(source+i, destination)
