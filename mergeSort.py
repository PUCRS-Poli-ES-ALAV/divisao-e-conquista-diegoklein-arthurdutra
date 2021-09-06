from itertools import count
import random
import time

cont = 0
def mergeSort(testList):
    global cont

    length = len(testList)
    middle_index = length//2


    if length > 1:
        # cont += 1
        # print(length)
        # Divisão da Lista em 2 Listas
        A = testList[:middle_index]
        B = testList[middle_index:]

        mergeSort(A)
        mergeSort(B)

        i = j = k = 0


        while i < len(A) and j < len(B):
            cont += 1
            if A[i] < B[j]:
                testList[k] = A[i]
                i += 1
            else:
                testList[k] = B[j]
                j += 1
            k += 1
 
        # Checa se algum elemento sobrou
        while i < len(A):
            cont += 1
            testList[k] = A[i]
            i += 1
            k += 1
 
        while j < len(B):
            cont += 1
            testList[k] = B[j]
            j += 1
            k += 1
    return cont

 
def printList(testList):
    for i in range(len(testList)):
        print(testList[i], end=" ")
    print()
 

def generateRandomList(listSize):
    randomList = random.sample(range(0,2000000), listSize)
    return randomList


        


#Execução
if __name__ == '__main__':
    inicio = time.time()
    list32 = generateRandomList(32)
    const32 = mergeSort(list32)
    fim = time.time()
    print("Lista de 32")
    print("Número de Iterações: ",const32)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")
    inicio = time.time()
    list2048 = generateRandomList(2048)
    cont2048 = mergeSort(list2048)
    fim = time.time()
    print("Lista de 2048")
    print("Número de Iterações: ",cont2048)
    print("Tempo de Execução: ",fim - inicio)
    print(" ")
    inicio = time.time()
    listMil = generateRandomList(1048576)
    contMil = mergeSort(listMil)
    fim = time.time()
    print("Lista de 1048576")
    print("Número de Iterações: ", contMil)
    print("Tempo de Execução: ", fim - inicio)
    
    
