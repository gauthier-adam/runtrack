def calcul(num1,operator,num2):
    if operator == "-":
        print(num1 - num2)
    elif operator == "+":
        print(num1 + num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "%":
        print(num1 % num2)
    elif operator == "/":
        print(num1 / num2)

    else:
        print("eror 404")

calcul(2,"+",8)
