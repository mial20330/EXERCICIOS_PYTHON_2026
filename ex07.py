while(True):
    nota1 = int(input("insira a primeira nota: "))
    if(nota1 > 10 or nota1 < 0):
        print("ta errado aí jovem")
    else:
        break

while(True):
    nota2 = int(input("insira a segunda nota: "))
    if(nota2 > 10 or nota2 < 0):
        print("ta errado aí jovem")
    else:
        break

while(True):
    nota3 = int(input("insira a terceira nota: "))
    if(nota3 > 10 or nota3 < 0):
        print("ta errado aí jovem")
    else:
        break

while(True):
    nota4 = int(input("insira a quarta nota: "))
    if(nota4 > 10 or nota4 < 0):
        print("ta errado aí jovem")
    else:
        break

mater = input("insira a matéria: ")

media = (nota1 + nota2 + nota3 + nota4) / 4

if(media >= 7):
    print("você esta aprovado " ,mater, " com a média de: " ,media)

elif(media < 7):
    print("você está reprovado em " ,mater, " com a média de: " ,media)

else:
    print("não tem como ter essa nota kk")