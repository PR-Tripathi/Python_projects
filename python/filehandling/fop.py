### read A Whole File

with open('example.txt','r') as file:
    for line in file:
        print(line.strip())
