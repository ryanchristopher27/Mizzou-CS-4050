# CS 4050
# Homework 1
# Ryan Christopher

# Imports
from timeit import default_timer as time
import sys

# Functions

# Passed the number being searched for and the data array of integers
# Sets starting pointer values and then runs the binary search loop until number is found or not
# Returns the index of the number if it is found or -1 if it was not found
def binarySearch(num, data):
    # Pointer initialization
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

# Passed the name of the file
# Opens file, gathers data, closes file, splits data up by the spaces, and then puts all the data into an array of integers
# Returns the data array of integers
def getData(name):
    f = open(name, "r")
    fileData = f.read()
    f.close()

    # Splits up data that is read and pops unneeded white space off the end
    dataString = fileData.split(" ")
    dataString.pop()

    # Transfers data to an array of of integers
    data = []
    for num in dataString:
        data.append(int(num))

    return data

# Passed the high pointer, low pointer, and iteration counter
# Prints out the values of the high pointer, low pointer, and iteration counter
def printPointers(h, l, count):
    print("Iteration ", count)
    print("High Pointer: ", h)
    print("Low Pointer: ", l)

def main():
    # Get FileName and Number as user input
    # fileName = input("Enter the name of the data file: ")
    # number = int(input("Enter the number to search for: "))

    mainStart = time() # Start of all time

    # Get Command Line Arguments
    fileName = sys.argv[1]
    number = sys.argv[2]

    #Get Data
    data = getData(fileName)
    
    # Binary Search
    searchStart = time() # Start of algo time
    index = binarySearch(number, data)
    searchEnd = time() # End of algo time

    # Print Output
    print("Index: ", index)
    mainEnd = time() # End of all time
    print("Algorithm Time: ", searchEnd - searchStart)
    print("All Time: ", mainEnd - mainStart)

main()