import os

def write_file(working_directory, file_path, content):
    
    try: 
        abs_working_dir = os.path.abspath(working_directory)

    except:
        return f'Error: Could not find the absolute path for working directory'


    try:
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    except:
        return f'Error: Could not join and establish absolute file path for the file path and working directory'
    
    try:
    
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
    except:
        return f'Error: Could not establish that file path is within or outside the working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, "w") as f: 
                    f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except:
        return f'Error: Could not establish if the file path exists or not and did not create a filepath'


#os.makedirs: Create a directory and all its parents
#os.path.dirname: Return the directory name