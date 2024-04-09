""" I supposed in division, second number can't be zero.
so I used "break".
The code using only what I learned is below under this code"""

# 숫자를 안받았을 때 계속해서 input 뜨게 하려면 반복문 중첩?

calculator = True

while calculator:

  first_number = int(input("Choose a number: \n"))
  second_number = int(input("Choose another one: \n"))

  operator = input("Choose an operation: \n\t Options are: + , - , * or /. \n\t Write 'exit' to finish. \n")

  if operator == "+":
    result = first_number + second_number
  elif operator == "-":
    result = first_number - second_number
  elif operator == "*":
    result = first_number * second_number
  elif operator == "/":
    if second_number == 0:
      result = "You can't divided by zero"
    else:
      result = first_number / second_number
  elif operator == "exit":
    break
  else:
    result = "Invalid operation"

  print(f"Result: {result}")


"""
calculator = True

while calculator:

  first_number = int(input("Choose a number: \n"))
  second_number = int(input("Choose another one: \n"))

  operator = input("Choose an operation: \n\t Options are: + , - , * or /. \n\t Write 'exit' to finish. \n")

  if operator == "+":
    result = first_number + second_number
    print(f"Result: {result}")
  elif operator == "-":
    result = first_number - second_number
    print(f"Result: {result}")
  elif operator == "*":
    result = first_number * second_number
    print(f"Result: {result}")
  elif operator == "/":
    result = first_number / second_number
    print(f"Result: {result}")
  else:
    calculator = False
"""