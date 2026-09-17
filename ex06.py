num1 = int(input("insira o primeiro número: "))
num2 = int(input("insira o segundo número: "))

oper = input("soma (+) ou subtração (-) ? ")

if(oper == "+"):
    calc = (num1 + num2)
    print("a resposta é: " ,calc)

elif(oper == "-"):
    calc = (num1 - num2)
    print("a resposta é: " ,calc)

else:
    print("algo deu errado, tente novamente")