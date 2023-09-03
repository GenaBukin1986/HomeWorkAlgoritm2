from random import randint
import os

def clear():
    os.system('cls')
    
def kuchasort(array):
    for i in range(len(array)// 2 - 1, -1, -1):
        kucha(array,len(array),i)
    
    for i in range(len(array) - 1, -1, -1):
        array[0],array[i] = array[i],array[0]
        kucha(array,i,0)

def kucha(array, heapSize, rootIndex):
    largest = rootIndex
    leftChild = 2 * rootIndex + 1
    rigthChild = 2 * rootIndex + 2
    
    if leftChild < heapSize and array[leftChild] > array[largest]:
        largest = leftChild
    
    if rigthChild < heapSize and array[rigthChild] > array[largest]:
        largest = rigthChild
        
    if largest != rootIndex:
        array[rootIndex],array[largest] = array[largest],array[rootIndex]
        
        kucha(array,heapSize,largest)
clear()
n = [18, 16, 15, 7, 15, 5, 2, 10, 2, 7, 5, 16, 0, 8, 7] 
print(n)
kuchasort(n)
print(n)