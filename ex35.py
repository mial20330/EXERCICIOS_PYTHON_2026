print("\n convertendo tintas! \n")
area =  float(input("insira a área em metros: "))

if(area <= -0):
    print("valor inválido")

else:
    metros_por_litro = 3
    litros_por_lata = 18
    preço_lata = 80
    litros_necessarios = area / metros_por_litro
    latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
    custo_total = latas_totais * preço_lata

    print(f"para {area} m², precisamos de {litros_totais:.2f} litros") #o ":.2f" foi usado para mostrar somente os dois primeiros números após a virgula!!
    print(f"você precisa de {latas_totais:.2f} latas para pintar {area} m²")
    print(f"isso tudo custará R${custo_total:.2f}")