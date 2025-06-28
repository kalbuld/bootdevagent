import os

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
    except:
        return f"Error: Cannot find absolute path to working directory {working_directory}"
    try:
        abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    except:
        return f"Error: Cannot find absolute path to file at {file_path}"
    
    try:
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{abs_file_path}" as it is outside the permitted working directory'
    except:
        return f'Error: Could not ascertain wheither the file path is in the directory or not'
    
    try:
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{abs_file_path}"'
    except:
        return f'Error: Could not evaluate if {abs_file_path} is a file or not'
    
    MAX_CHARS = 10000

    try:
        with open(abs_file_path, "r") as f:
            if os.path.getsize(abs_file_path) > 10000:
                file_string_content = f.read(MAX_CHARS)
                addended_file_string_content = file_string_content + "\n" + f'[...File "{file_path}" truncated at 10000 characters]'
                return addended_file_string_content
            file_string_content = f.read()
            return file_string_content
    except:
        return f"Error: Could not open and read file at {abs_file_path}"
    
    


