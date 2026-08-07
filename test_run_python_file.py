from functions.run_python_file import run_python_file

commands = [
  {
    "name": "main.py"
  },
  {
    "name": "main.py",
    "operation": ["3 + 5"]
  },
  {
    "name": "tests.py"
  },
  {
    "name": "../main.py"
  },
  {
    "name": "nonexistent.py"
  },
  {
    "name": "lorem.txt"
  }
]



for command in commands:
  if "operation" in command:
    result = run_python_file("calculator", command["name"], command["operation"])

  else:
    result = run_python_file("calculator", command["name"])

  print(result)
