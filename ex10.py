ld1 = int(input("insira o primeiro lado: "))
ld2 = int(input("insira o segundo lado: "))
ld3 = int(input("insira o terceiro lado: "))

if(ld1 == ld2 and ld1 == ld3):
    print("esse triângulo é Equilátero")

elif(ld1 == ld2 or ld1 == ld3):
    print("esse triângulo é Isósceles")

else:
    (ld1 != ld2 and ld1 != ld3)
    print("esse triângulo é Escaleno")