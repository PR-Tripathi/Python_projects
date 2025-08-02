## Joining Paths
import os

# dir_name="folder"
# file_name="file.txt"
# full_path = os.path.join(os.getcwd(),dir_name,file_name)
# print(full_path) 

# path='example.txt'
# if os.path.exists(path):
#     print(f"The Path'{path}' exists")
# else:
#     print(f"the path '{path} dont exist'")

## Getting  The Absolute Path 
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)