# CS 4050
# Homework 1
# Ryan Christopher

# Imports
import math
import random

# Functions
##def binarySearch():


##def getData():

def printHML(h, m, l):
    print("High: ", h)
    print("Mid: ", m)
    print("Low: ", l)


def main():
    #fileName, number = input("Enter the filename a number. Format: (filename, number)").split(", ")
    
    # Get FileName and Number
    fileName = input("Enter the name of the data file: ")
    number = input("Enter the number to search for: ")

    #Get Data
    f = open(fileName, "r")
    fileData = f.read()
    f.close()

    #data = []
    data = fileData.split(" ")
    data.pop()

    high = len(data)
    mid = high//2
    low = 0
    print(data[mid])
    print(len(data))
    printHML(high, mid, low)

    hold = 1
    while(hold < 10):
        print("data[mid] = ", data[mid])
        if (number > data[mid]):
            low = mid+1
            mid = (high+low)//2
            print("more")
            printHML(high, mid, low)
        elif (number < data[mid]):
            high = mid-1
            mid = (high+low)//2
            print("less")
            printHML(high, mid, low)
        elif ((number == data[mid]) or (low == mid == high)):
            print("exit")
            hold = 0
        hold+=1
    
    if (number == data[mid]):
        index = mid
    else:
        index = -1

    print(index)

main()