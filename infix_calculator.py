print("Insert a math problem : ")
problem = input()
n1, symbol, n2 = problem.split(" ")
n1 = int(n1)
n2 = int(n2)
symbol = symbol.lower()
if symbol == "+":
    print("The answer is: ",n1 + n2)
elif symbol == "-":
    print("The answer is: ",n1 - n2)
elif symbol == "*":
    print("The answer is: ",n1 * n2)
elif symbol == "/":
    print("The answer is: ",n1 / n2)
else:
    print("Invalid operator")