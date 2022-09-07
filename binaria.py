import random

if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]

    encontrado = False
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
