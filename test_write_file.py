from functions.write_file import write_file

write_in_file = [
  {
    "file_path": "lorem.txt",
    "content": "wait, this isn't lorem ipsum"
  },
  {
    "file_path": "pkg/morelorem.txt",
    "content": "lorem ipsum dolor sit amet"
  },
  {
    "file_path": "/tmp/temp.txt",
    "content": "this should not be allowed"
  },
]

for item in write_in_file:
  result = write_file("calculator", item["file_path"], item["content"])
  print(result)