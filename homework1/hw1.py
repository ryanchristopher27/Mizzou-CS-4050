# CS 4050
# Homework 1
# Ryan Christopher

# Imports
from timeit import default_timer as time
import sys

# Functions
def binarySearch(num, data):
    high = len(data)
    low = 0
    count = 1

    while(low <= high):
        mid = (low+high)//2

        if (int(num) > data[mid]):
            low = mid+1
        elif (int(num) < data[mid]):
            high = mid-1      
        else:
            return mid

        if (count < 5):
            printPointers(high, low, count)
        count+=1

    return -1

def getData(name):
    f = open(name, "r")
    fileData = f.read()
    f.close()

    dataString = fileData.split(" ")
    dataString.pop()

    data = []
    for num in dataString:
        data.append(int(num))

    return data

def printPointers(h, l, count):
    print("Iteration ", count)
    print("High Pointer: ", h)
    print("Low Pointer: ", l)

def main():
    # Get FileName and Number as user input
    # fileName = input("Enter the name of the data file: ")
    # number = int(input("Enter the number to search for: "))

    mainStart = time()

    # Get Command Line Arguments
    fileName = sys.argv[1]
    number = sys.argv[2]

    #Get Data
    data = getData(fileName)
    
    # Binary Search
    searchStart = time()
    index = binarySearch(number, data)
    searchEnd = time()

    # Print Output
    print("Index: ", index)
    mainEnd = time()
    print("Algorithm Time: ", searchEnd - searchStart)
    print("All Time: ", mainEnd - mainStart)

main()