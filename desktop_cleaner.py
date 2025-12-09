import os
import shutil

#path to Desktop
desktop_path = os.path.expanduser('~/Desktop')

#dictionary to save files
file_by_type = {}

for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)

    #check if object is a file
    if os.path.isfile(file_path):
        file_type = os.path.splitext(filename)[1]
    
        if file_type not in file_by_type:
            file_by_type[file_type] = []
        
        file_by_type[file_type].append(file_path)

for file_type, files in file_by_type.items():
    dir_name = f"{file_type[1:]}"
    dir_path = os.path.join(desktop_path, dir_name)
    
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    
    for file_path in files:
        shutil.move(file_path, dir_path)
