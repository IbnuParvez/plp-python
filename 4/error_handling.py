#error handling challenge

name = input("What's the file name ? ")

try:
  with open(name, "r") as file:
    print("File name is: ")
    print(file.read())

except FileNotFoundError:
  print("File you named is not currently available")

except PermissionError:
  print("You do not have boss priviledges to view this file let alone read it")