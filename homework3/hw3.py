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
    visited = [False] * nNode
    level = [0] * nNode
    q = [sID]
    count = 0

    visited[sID] = True
    level[sID] = 0

    while q:
        vis = q[0]

        # print(vis)

        q.pop(0)

        for i in range(nNode):
            # print(list[vis][i])
            # print(visited[i])
            if ((int(list[vis][i]) == 1) and (not visited[i])):
                # print("found: ", i)
                q.append(i)

                visited[i] = True
                level[i] = level[vis] + 1
                count = level[i]

    # print("count: ", count)

    # for i in range(nNode):
    #     print(" ", i, " -->", level[i])
    temp = []
    for i in range(count+1):
        # print("L", i, ":")
        for j in range(nNode):
            if (level[j] == i):
                temp.append(str(j+1))
                # print(j)
        print("L"+ str(i) + ": " + ', '.join(temp))
        temp.clear()


# Main
def main():
    startTime = time()
    nNode = sys.argv[1]
    sID = sys.argv[2]
    filename = sys.argv[3]

    list = readFile(filename)

    BFS(int(sID)-1, list, int(nNode))
    endTime = time()
    print("All Time: ", (endTime - startTime)*1000, "ms")





main()