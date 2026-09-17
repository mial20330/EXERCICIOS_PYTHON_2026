n1 = int(input("insira o primeiro número: "))
n2 = int(input("insira o segundo número: "))
n3 = int(input("insira o terceiro número: "))

if(n1 >= n2 and n1 >= n3):
    ord1 = n1
    if(n2 >= n3):
        ord2 = n2
        ord3 = n3
    else:
        ord2 = n3
        ord3 = n2

elif(n2 >= n1 and n2 >= n3):
    ord1 = n2
    if(n1 >= n3):
        ord2 = n1
        ord3 = n3
    else:
        ord2 = n3
        ord3 = n1

else:
    ord1 = n3
    if(n1 >= n2):
        ord2 = n1
        ord3 = n2
    else:
        ord2 = n2
        ord3 = n1

print("A ordem certa é: " ,ord1, " > " ,ord2, " > " ,ord3)