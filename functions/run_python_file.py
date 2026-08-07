import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
  abs_path_wd = os.path.abspath(working_directory)
  abs_file_path = os.path.join(abs_path_wd, file_path)
  target_dir = os.path.normpath(abs_file_path)
    
  # Will be True or False
  valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
    
  if not valid_target_dir:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(abs_file_path):
    return f'Error: "{file_path}" does not exist or is not a regular file'

  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file'

  try:
    command = ["python", abs_file_path]
    if not args is None:
      command.extend(args)

    output = subprocess.run(
      command, 
      cwd=abs_path_wd,
      timeout=30,
      capture_output=True,
      text=True
    )
    final_str = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
"""
    if output.stdout == "" and output.stderr == "":
      final_str += "No output produced"
    if output.returncode != 0:
      final_str += "Process exited with code X"

    return final_str
  
  except Exception as e:
    return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file to run, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "An optional array of strings to be used as the CLI args for the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}