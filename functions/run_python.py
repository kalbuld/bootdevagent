import os
import subprocess

def run_python_file(working_directory, file_path):
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.splitext(abs_file_path)[1] == ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try: 
        result = subprocess.run(["python3", abs_file_path], capture_output=True, timeout=30, cwd=abs_working_dir, text=True)
        
        stdout = result.stdout
        stderr = result.stderr
        returncode = result.returncode

        if not returncode ==0:
            return f'Process exited with code {returncode}' + '\n' + f'STDOUT: {stdout}' + "\n" + f'STDERR: {stderr}'
        if stdout == "" and stderr == "":
            return 'No output produced'
        return f'STDOUT: {stdout}' + "\n" + f'STDERR: {stderr}'


    except Exception as e:
        return f"Error: executing python file: {e}"
