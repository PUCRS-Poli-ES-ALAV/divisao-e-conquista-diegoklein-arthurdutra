from itertools import count
import random

cont = 0

def mergeSort(testList):
    

    length = len(testList)
    middle_index = length//2


    if length > 1:
        cont += 1
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
                cont += 1
                testList[k] = A[i]
                i += 1
            else:
                cont += 1
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
    randomList = random.sample(range(0,1000000), listSize)
    return randomList
#Execução
if __name__ == '__main__':
    # generateRandomList(32)
    # generateRandomList(2048)
    # generateRandomList(1048576)
    testList = [5, 1]
    print("Lista Inicial: ", end="\n")
    printList(testList)
    mergeSort(testList)
    print("Lista Organizada: ", end="\n")
    printList(testList)
    print(count)
