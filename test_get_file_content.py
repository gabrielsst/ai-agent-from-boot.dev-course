from functions.get_file_content import get_file_content

file_paths = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

for file_path in file_paths:
  result = get_file_content("calculator", file_path)
  print(result)
