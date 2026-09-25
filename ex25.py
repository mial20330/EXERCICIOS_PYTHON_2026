print("calculando números maiores do que zero \n")
n1 = int(input("insira algum número maior do que zero: "))

if(n1 > 0):
    n2 = (n1**2)
    n3 = (n1**3)
    print(f"o valor ao quadrado é {n2} e ao cubo é {n3}")

else:
    print("valor inválido!!")