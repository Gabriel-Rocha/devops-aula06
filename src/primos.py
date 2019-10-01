numero = int(input())
inicio = 1
lista = []
while True:
    if inicio > 1:
        for i in range(2,inicio):
            if (inicio % i) == 0:
                break
        else:
            lista.append(inicio)
    if (len(lista) == numero):
        print(lista)
        break
    else:
        inicio += 1
        continue
