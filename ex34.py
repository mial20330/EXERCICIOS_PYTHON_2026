print("calculando o seu peso ideal com base na sua altura! \n")
h = float(input("insira sua altura: "))
sx = input("você é Homem (h) ou Mulher (m)?")

if(sx == "h"):
    pso = (72.7 * h) - 58
    print(f"o seu peso ideal é {pso}kg")

elif(sx == "m"):
    pso = (62.1* h ) - 44.7
    print(f"o seu peso ideal é {pso}kg")

else:
    print("valor inválido!")