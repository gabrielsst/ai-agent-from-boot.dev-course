import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
  try:
    abs_path_wd = os.path.abspath(working_directory)
    abs_path_dir = os.path.join(abs_path_wd, directory)
    target_dir = os.path.normpath(abs_path_dir)

    # Will be True or False
    valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd

    if not valid_target_dir:
      return f'  Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path_dir):
      return f'  Error: "{abs_path_dir}" is not a directory'

    items = []
    for item in os.listdir(abs_path_dir):
      abs_item_path = os.path.join(abs_path_dir, item)
      items.append({
        "name": item,
        "file_size": os.path.getsize(abs_item_path),
        "is_dir": os.path.isdir(abs_item_path), 
      })

    output_items = []
    for item in items:
      output_items.append(f'- {item["name"]}: file_size={item["file_size"]} bytes, is_dir={item["is_dir"]}')

    return "\n  ".join(output_items)
  except Exception as e:
    return f"  Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}