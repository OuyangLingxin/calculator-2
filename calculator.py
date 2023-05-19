"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
with open("output.txt", "a") as f:
  while True:
    user_input = input("> ")
    tokens = user_input.split(' ')
    if tokens[0] == 'q':
      break
    elif len(tokens) < 3:
      print("please enter correct number of arguments")
      break
    elif tokens[0] not in ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']:
      print("please enter the correct command")
      break
    elif type(tokens[1]) != "numbe" or type(tokens[2]) != "numbe":
      print("please enter numbers only")
      break
    elif tokens[0] == "+":
      print(add(float(tokens[1]), float(tokens[2])), file=f)
    elif tokens[0] == "-":
      print(subtract(float(tokens[1]), float(tokens[2])), file=f)
    elif tokens[0] == "*":
      print(multiply(float(tokens[1]), float(tokens[2])), file=f)
    elif tokens[0] == "/":
      print(divide(float(tokens[1]), float(tokens[2])), file=f)
    elif tokens[0] == "square":
      print(square(float(tokens[1])), file=f)
    elif tokens[0] == "cube":
      print(cube(float(tokens[1])), file=f)
    elif tokens[0] == "pow":
      print(power(float(tokens[1]), float(tokens[2])), file=f)
    elif tokens[0] == "mod":
      print(mod(float(tokens[1]), float(tokens[2])), file=f)