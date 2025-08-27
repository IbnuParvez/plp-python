x = float(input("What is your first choice? "))

y = float(input("What is your second number "))

operation = input("Enter your preferred operation (+, -, *, /,): ")

if operation == "+":
    result = x + y 
    print(f"{x} + {y} = {result}")

elif operation == "-":
    result = x - y 
    print(f"{x} - {y} = {result}")

elif operation == "*":
    result = x * y 
    print(f"{x} * {y} = {result}")

elif operation == "/":
    if y != 0:
      result = x / y
      print(f"{x} / {y} = {result}")
    else:
      print("Division by zero is not your level boss!!!")

else:
    print("Please choose the appropriate operations as stipulated")