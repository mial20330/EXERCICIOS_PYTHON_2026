print("calculadora \n")

n1 = int(input("insira o primeiro número: "))
n2 = int(input("insira o segundo número: "))

print("Soma (+) subtração (-) Multiplicação (*) Divisão (/)")
op = input("insira qual a sua operação: ")

if(op == "+"):
    resul = n1 + n2
    print(f"o resultado de {n1} + {n2} é igual a {resul}")

elif(op == "-"):
    resul = n1 - n2
    print(f"o resultado de {n1} - {n2} é igual a {resul}")

elif(op == "*"):
    resul = n1 * n2
    print(f"o resultado de {n1} * {n2} é igual a {resul}")

elif(op == "/"):
    resul = n1 / n2
    print(f"o resultado de {n1} / {n2} é igual a {resul}")

else:
    print("valor inválido")