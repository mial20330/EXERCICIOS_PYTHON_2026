print("dias da semana!\n")
print(" 1 - domingo \n 2 - segunda \n 3 - terça \n 4 - quarta \n 5 - quinta \n 6 - sexta \n 7 - sábado \n")

dia = int(input("insira o dia da semana em número: "))

if(dia > 7 or dia <= -0):
    print("valor inválido!!")

elif(dia == 1):
    print("o seu dia da semana é domingo")    
    
elif(dia == 2):
    print("o seu dia da semana é segunda")
    
elif(dia == 3):
    print("o seu dia da semana é terça")

elif(dia == 4):
    print("o seu dia da semana é quarta")

elif(dia == 5):
    print("o seu dia da semana é quinta")

elif(dia == 6):
    print("o seu dia da semana é sexta")

else:
    (dia == 7)
    print("o seu dia da semana é sábado")