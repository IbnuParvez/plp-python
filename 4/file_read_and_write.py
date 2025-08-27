#read and write challenge

with open("file.txt", "r") as file:
    content = file.read()

modified_content = content.upper()

with open("output.txt", "w") as output:
    output.write(modified_content)


  