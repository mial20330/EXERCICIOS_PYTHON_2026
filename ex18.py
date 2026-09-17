dep = int(input("insira o valor do depósito: "))
juros = int(input("insira o valor da taxa de juros: "))

juros = (juros / 100)

calc = (juros * dep)
total = (calc + dep)

print("o seu rendimento total é: " ,total)