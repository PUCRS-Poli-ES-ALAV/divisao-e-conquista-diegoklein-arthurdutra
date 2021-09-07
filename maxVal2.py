import random
import time

cont = 0

def generateRandomList(numRange, listSize):
    randomList = random.sample(range(0,numRange), listSize)
    return randomList


def maxVal2(A, init, end):
    global cont

    if (end-init) <=1:
        cont += 1
        return max(A[init], A[end])
    else:
        m = (init + end)//2
        v1 = maxVal2(A,init,m)
        v2 = maxVal2(A,m+1,end)
        return max(v1,v2)

if __name__ == '__main__':
    inicio = time.time()
    list32 = generateRandomList(100, 32)
    teste1 = maxVal2(list32)
    fim = time.time()
    print("Lista de 32")
    print("Maior valor da Lista: ", teste1)
    print("Número de Iterações: ", cont)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")