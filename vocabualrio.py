with open('palabras.txt', 'r') as file:
    lista = file.read().splitlines()

orden = sorted(lista)