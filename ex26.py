print("calculando um número elevado ao outro \n")
n1 = int(input("insira o primeiro número: "))
n2 = int(input("insira o segundo número: "))
if(n1 < 10 or n2 < 10):
    num1 = n1**n2
    num2 = n2**n1

    print(f"1 é {num1} e 2 é {num2}")
    
else:
    print("valor inválido!!")