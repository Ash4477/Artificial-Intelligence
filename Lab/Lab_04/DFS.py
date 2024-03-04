import queue

# Functions

def depthFirstTraversal(graph) :
    myStack = queue.LifoQueue()

    visArray = [False, False, False, False, False, False, False]
    parentArray = [-1, -1, -1, -1, -1, -1, -1]
    nodeArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    startNode = 0

    myStack.put(startNode)

    while (not myStack.empty()):
        if (visArray[startNode] == False):
            for j in range(len(graph[0])):
                if (graph[startNode][j] == True):
                    myStack.put(j)
                    parentArray[j] = startNode
        
        visArray[startNode] = True
        startNode = myStack.get()
    
    i = 6
    while (parentArray[i] != -1):
        print(nodeArray[i], " <- ", end = "")
        i = parentArray[i]
    print('A <- ')


# Main Program         
graph = [
    [0,1,1,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]



depthFirstTraversal(graph)


