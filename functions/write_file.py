import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
  abs_path_wd = os.path.abspath(working_directory)
  abs_file_path = os.path.join(abs_path_wd, file_path)
  target_dir = os.path.normpath(abs_file_path)
      
  # Will be True or False
  valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
      
  if not valid_target_dir:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  if os.path.isdir(abs_file_path):
    return f'Error: Cannot write to "{file_path}" as it is a directory'

  parent_dir = os.path.dirname(abs_file_path)
  try:
    os.makedirs(parent_dir, exist_ok=True)

  except Exception as e:
    return f"Error: {e}"

  try:
    with open(abs_file_path, "w") as f:
      f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  
  except Exception as e:
    return f"Error: {e}"