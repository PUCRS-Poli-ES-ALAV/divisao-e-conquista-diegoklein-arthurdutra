import random
import time

def generateRandomList(listSize):
    randomList = random.sample(range(0,2000000), listSize)
    return randomList


def maxVal1(A):
    return max(A)


if __name__ == '__main__':
    inicio = time.time()
    list32 = generateRandomList(32)
    const32 = maxVal1(list32)
    fim = time.time()
    print("Lista de 32")
    print(const32)
    print("Número de Iterações: 0")
    print("Tempo de Execução: ",fim - inicio)
    print(" ")
    inicio = time.time()
    list2048 = generateRandomList(2048)
    const2048 = maxVal1(list2048)
    fim = time.time()
    print("Lista de 2048")
    print(const2048)
    print("Número de Iterações: 0")
    print("Tempo de Execução: ",fim - inicio)
    print(" ")
    inicio = time.time()
    listMil = generateRandomList(32)
    constMil = maxVal1(listMil)
    fim = time.time()
    print("Lista de 1048576")
    print(constMil)
    print("Número de Iterações: 0")
    print("Tempo de Execução: ",fim - inicio)
    print(" ")

    