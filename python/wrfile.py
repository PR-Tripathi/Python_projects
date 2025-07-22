# Writing File Then Reading File 


with open('example.txt','w+') as file:
    file.write("Hello My GitHub People\n")
    file.write("This Is A New Day Out There\n")

    # Move the file cursor to the beginning
    file.seek(0)

    #read the content of file
    content = file.read()
    print(content)