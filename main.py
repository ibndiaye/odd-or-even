print("welcome to this simple calculator")

number = int(input("Which number do you want to check? "))
divider = int(input("what do you want to divide it by? "))
operation=number%divider
result=round(number/divider, 2)
if operation == 0:
  print(f"{result} is an even number")
else:
  print(f"{result} is an odd number")
