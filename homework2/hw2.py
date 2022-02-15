# CS 4050
# Homework 2
# Ryan Christopher

# Question 1


def q1():
    print("start")
    A = [-1, 2, 3, 0, 5]
    B = []
    i = 0
    j = 0
    k = 0
    T = 1
    found = False

    A.sort()

    print("before loops")
    for i in range(0, len(A)-3):
        j = i+1
        k = len(A)-1

        while (j < k):
            if (A[i] + A[j] + A[k] == T):
                print("found")
                B.append(A[i])
                B.append(A[j])
                B.append(A[k])
                found = True
                break
            elif (A[i] + A[j] + A[k] < T):
                j+=1
            else:
                k-=1
        if (found):
            break

    if (found):
        print(B)
    else:
        print("NIL")

def q2():
    # A = [3, 4, 5, 5, 6, 10, 13, 13, 20, 22, 0, 1, 2, 3, 3]
    A = [0, 1, 2, 3, 3, 3, 4, 5, 5, 6, 10, 13, 13, 22]
    

    lo=0
    hi=len(A)-1
    output = 0
    
    # while(lo < hi):
    #     if (A[lo] > A[lo+1]):
    #         output = A[lo]
    #         break
    #     elif (A[hi] < A[hi-1]):
    #         output = A[hi-1]
    #         break
    #     elif (A[lo] < A[hi]):
    #         output = A[hi]
    #         break
    #     else:
    #         lo+=1
    #         hi-=1


    while(lo <= hi):
        mid = ((hi-lo)//2) + lo

        print("lo = ", lo)
        print("mid = ", mid)
        print("hi = ", hi)

        if (lo == hi):
            output = A[lo]
            break
        elif (mid == 0 and A[mid] > A[mid+1]):
            output = A[mid]
            break
        elif (mid < hi and mid > 0 and A[mid] > A[mid+1] and A[mid] >= A[mid-1]):
            output = A[mid]
            break

        # if (A[lo] < A[hi]):
        #     output = A[hi]
        #     break
        # else:
        #     lo+=1
        #     hi-=1
        
        if (A[lo] > A[mid]):
            hi = mid-1
        else:
            lo = mid+1
        

    # output = q2search(A, lo, hi)
    
    print(output)

# def q2search(A, lo, hi):
#     if lo == hi:
#         return lo
    
#     mid = lo + (hi - lo) // 2

#     if (mid == 0 and A[mid] > A[mid+1]):
#         return A[mid]

#     if (A[mid] > A[mid-1] and A[mid] > A[mid+1] and mid < hi and mid > 0):
#         return A[mid]

#     if (A[lo] > A[mid]):
#         return q2search(A, lo, mid-1)
#     else:
#         return q2search(A, mid+1, hi)

def q3():
    A = [10, 9, 5, 9, 8, 7, 6, 4, 6, 3, 2]
    # A = [9, 8, 7, 6, 5, 4, 6, 7, 6, 5, 4, 3, 2, 1]
    B = [1]
    count = 1
    size = 1

    for i in range(0, len(A)-1):
        if (A[i] > A[i+1] and count < size):
            count+=1
        elif (A[i] > A[i+1] and count == size):
            count+=1
            size+=1
        else:
            count = 1

        B.append(size)

    print(B)

class Graph:
     
    adj = []
 
    # Function to fill empty adjacency matrix
    def __init__(self, v, e):
         
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)]
                        for j in range(v)]
 
    # Function to add an edge to the graph
    def addEdge(self, start, e):
         
        # Considering a bidirectional edge
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
 
    # Function to perform DFS on the graph
    def BFS(self, start):
         
        # Visited vector to so that a
        # vertex is not visited more than
        # once Initializing the vector to
        # false as no vertex is visited at
        # the beginning
        visited = [False] * self.v
        level = [0] * self.v
        q = [start]
 
        # Set source as visited
        visited[start] = True
        level[start] = 0
 
        while q:
            vis = q[0]
 
            # Print current node
            print(vis, end = ' ')
            q.pop(0)
             
            # For every adjacent vertex to
            # the current vertex
            for i in range(self.v):
                if (Graph.adj[vis][i] == 1 and
                      (not visited[i])):
                           
                    # Push the adjacent node
                    # in the queue
                    q.append(i)
                     
                    # set
                    visited[i] = True
                    level[i] = level[vis] + 1
        
        # L = [8][8]
        # count = 1
        for i in range(self.v):
            # L[i].append(count)
            # count+=1
            print(" ", i, " -->", level[i])
        
        # for i in range(len(L)):
            
            
        # print(L)


def q4():
    # Driver code
    v, e = 9, 12
    
    # Create the graph
    G = Graph(v, e)
    G.addEdge(1, 2)
    G.addEdge(1, 3)
    G.addEdge(2, 3)
    G.addEdge(2, 4)
    G.addEdge(2, 5)
    G.addEdge(3, 5)
    G.addEdge(3, 7)
    G.addEdge(3, 8)
    G.addEdge(4, 5)
    G.addEdge(5, 6)
    G.addEdge(7, 8)

    
    # Perform BFS
    G.BFS(1)


def main():
    # q1()
    # q2()
    # q3()
    q4()

main()
        