import random
import time

cont = 0

def generateRandomList(numRange, listSize):
    randomList = random.sample(range(0,numRange), listSize)
    return randomList


def maxVal1(A):
    global cont
    
    max = A[0]

    for i in A:
        cont += 1
        if i > max:
            max = i
    
    return max


if __name__ == '__main__':
    inicio = time.time()
    list32 = generateRandomList(100, 32)
    teste1 = maxVal1(list32)
    fim = time.time()
    print("Lista de 32")
    print("Maior valor da Lista: ", teste1)
    print("Número de Iterações: ", cont)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")

    cont = 0
    inicio = time.time()
    list2048 = generateRandomList(3050, 2048)
    teste2 = maxVal1(list2048)
    fim = time.time()
    print("Lista de 2048")
    print("Maior valor da Lista: ", teste2)
    print("Número de Iterações: ", cont)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")

    cont = 0
    inicio = time.time()
    listMil = generateRandomList(1050000, 1048576)
    teste3 = maxVal1(listMil)
    fim = time.time()
    print("Lista de 1048576")
    print("Maior valor da Lista: ", teste3)
    print("Número de Iterações: ", cont)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")

    