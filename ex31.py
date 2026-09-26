print("tabuada do 1 ao 10 \n")
num = int(input("Digite um número: "))

if(num > 10 or num <= -0):
    print("valor inválido!!")

elif(num == "0"):
    print("qualquer número multiplicado por 0 é igual a 0!!")

else:
    for i in range(1, 11):
        resul = num * i
        print(num, "*", i ,  "=", resul)