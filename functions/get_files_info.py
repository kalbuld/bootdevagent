import os

def get_files_info(working_directory, directory=None):
    
    try:
        work_dir_path = os.path.abspath(working_directory)
    except:
        return f'Error: Could not get the absolute path for {working_directory}'
    try: 
        dir_path = os.path.abspath(os.path.join(work_dir_path,directory))
    except:
        return f'Error: Could not get the absolute path for {directory}'
        
    if not dir_path.startswith(work_dir_path):
        return f'Error: Cannot list "{dir_path}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{dir_path}" is not a directory'
    
    contents = []
    separator = "\n"

    try: 

        for item in os.listdir(dir_path):
            try: 
                contents.append(f"- {item}: {os.path.getsize(os.path.join(dir_path, item))} bytes, is_dir={os.path.isdir(os.path.join(dir_path, item))}")
            except:
                return f'Error: Could not add {item}'
    except:
        return f'Failed to iterate over items in {dir_path}'
    
    return separator.join(contents)
            

