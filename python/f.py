###File And  Directory Access

"""import os 
print(os.getcwd())"""


###Creating Directory
"""import os
os.mkdir('test_dir')
"""

#Data Serialization
"""import json
data ={'name':'krish','age':25}
 
json_str =json.dumps(data)
print(json_str)
print(type(json_str)) 


parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data)) """

#csv

# import csv 

# with open ('example.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name','age'])
#     writer.writerow(['krish',32])


# with open('example.csv', mode='r') as file:
#     reader =csv.reader(file)
#     for row in reader:
#         print(row)
