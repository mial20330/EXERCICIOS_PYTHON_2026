print("Em qual turno você estuda?")
turno = input("('M'- Matutino) ('V' - Vespertino) (N - Noturno) \n")

if(turno == "m"):
    print("Bom dia!")

elif(turno == "v"):
    print("Boa tarde!")

elif(turno == "n"):
    print("Boa noite!")

else:
    print("Valor inválido!")