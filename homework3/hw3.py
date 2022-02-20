# CS 4050
# Homework 3
# Ryan Christopher

# Imports
from timeit import default_timer as time
import sys

# Functions
def readFile(filename):
    f = open(filename, "r")
    mergedList = []
    for msg in f.readlines():
        msg = msg.strip('\n')
        adm = msg.split(' ')
        mergedList.append(adm)
    return mergedList

def BFS(sID, list, nNode):
    # Initialize variables, arrays, and queues
    visited = [False] * nNode
    level = [0] * nNode
    q = [sID]
    count = 0

    # Update values with starting node
    visited[sID] = True
    level[sID] = 0

    # Iterate through queue until empty
    while q:
        vis = q[0]

        q.pop(0)

        for i in range(nNode):
            # Check if iterated node has edge with current node and is not visited
            if ((int(list[vis][i]) == 1) and (not visited[i])):
                # Add new node to queue and update arrays accordingly
                q.append(i)
                visited[i] = True
                level[i] = level[vis] + 1
                count = level[i]

    temp = []
    # Iterate through number of total levels
    for i in range(count+1):
        # Iterate through all nodes in graph
        for j in range(nNode):
            # Check if node has level equal to iterated level
            if (level[j] == i):
                temp.append(str(j+1))
        print("L"+ str(i) + ": " + ', '.join(temp))
        temp.clear()

# Main
def main():
    # Start Time
    startTime = time()
    # Get Command Line Variables
    nNode = sys.argv[1]
    sID = sys.argv[2]
    filename = sys.argv[3]
    # Read File
    list = readFile(filename)
    # Breadth First Search
    BFS(int(sID)-1, list, int(nNode))
    endTime = time()
    print("Execution Time: ", (endTime - startTime)*1000, "ms")

main()