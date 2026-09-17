while(True):
    letra = input("insira uma letra: ")
    if(letra == "A" or letra == "a" or letra == "E" or letra == "e" or letra == "I" or letra == "i" or letra == "O" or letra == "o" or letra == "U" or letra == "u"):
        print("A letra:'" ,letra, "'é uma vogal")
    else:
        print("A letra:'" ,letra, "'é uma consoante")
        break