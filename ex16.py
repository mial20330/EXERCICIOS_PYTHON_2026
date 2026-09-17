sal = int(input("informe seu salário: "))

aum = input("insira a porcentagem de aumento: ")
aum = float(aum.replace(",","."))/100
total = (sal * aum + sal)
print(total)