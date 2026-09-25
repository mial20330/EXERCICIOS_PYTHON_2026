print("descobrindo idade e entre outros \n")
id = int(input("insira o ano em que vc nasceu: "))

if(id >= 2026 or id <= 1960):
    print("tem como não kkk")

else:
    nsc = 2026 - id         #a
    mes = nsc * 12          #b
    dia = nsc * 365 + 15    #c
    sem = dia / 7           #d
    antes = 2019 - id       #e

    print(f"sua idade atual é: {nsc}")
    print(f"sua idade em mêses é: {mes}")
    print(f"sua idade em dias é: {dia}")
    print(f"sua idade em semanas é: {round(sem)}")
    print(f"em 2019 você tinha {antes} anos de idade")
