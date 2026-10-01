print("calculando o seu peso ideal com base na sua altura! \n")
h = float(input("insira sua altura: "))
sx = input("você é masculino (m) ou feminino (f)?")

if(sx == "m"):
    pso = (72.7 * h) - 58
    print(f"o seu peso ideal é {pso}kg")

elif(sx == "f"):
    pso = (62.1* h ) - 44.7
    print(f"o seu peso ideal é {pso}kg")

else:
    print("valor inválido!")