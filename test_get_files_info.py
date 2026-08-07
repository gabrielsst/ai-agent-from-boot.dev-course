from functions.get_files_info import get_files_info

directories = ["", "pkg", "/bin", "../"]
default_message = "Result for current directory:\n "

for dir in directories:
  if dir == "":
    print(f"Result for current directory:")
    print(" ", get_files_info("calculator"))
  else:
    print(f"Result for {dir} current directory:")
    print(" ", get_files_info("calculator", dir))
  print()
