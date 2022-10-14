import re

def arithmetic_arranger(problems):

  if(len(problems) > 5):
    return "Error: Muitos problemas."
    
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""
  for problem in problems:
    if(re.search("[^\s0-9.+-]", problem)):
      if(re.search("[\]", problem) or re.search("[*]", problem)):
        return "Error: Operadores devem ser '+' ou '-'."
      return "Error: Numeros devem conter apenas digitos."

    firstNumber = problem.split(" ")[0]
    operador = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return "Error: Numeros não podem conter mais que quatro digitos."

    sum = ""
    if(operador == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
    elif(operador == "-"):
      sum = str(int(firstNumber) - int(secondNumber))

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operador + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    for s in range (length):
      line += "-"

    if problem != problems[-1]:
       first += top + '    '
       second += bottom + '    '
       lines += line + '    '
       sumx += res + '    '
       solve = True
    else:
       first += top
       second += bottom
       lines += line
       sumx += res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines + "\n" 
  return string

