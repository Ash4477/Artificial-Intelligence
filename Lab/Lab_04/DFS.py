import queue

# Functions

def printPath(parentArray, goalNode) :
    nodeArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    i = goalNode
    while (parentArray[i] != -1):
        print(nodeArray[i], " <- ", end = "")
        i = parentArray[i]
    print('A <- ')


def depthFirstTraversal(graph) :
    myStack = queue.LifoQueue()
    nodeArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    visArray = [False, False, False, False, False, False, False]
    startNode = 0

    myStack.put(startNode)

    while (not myStack.empty()):
        if (visArray[startNode] == False):
            for j in range(len(graph[0])):
                if (graph[startNode][j] == True):
                    myStack.put(j)
        
        print(startNode, end=" ")
        visArray[startNode] = True
        startNode = myStack.get()


def depthFirstSearch(graph, goalNode) :
    myStack = queue.LifoQueue()

    visArray = [False, False, False, False, False, False, False]
    parentArray = [-1, -1, -1, -1, -1, -1, -1]
    startNode = 0

    myStack.put(startNode)

    while (not myStack.empty() and startNode != goalNode):
        if (visArray[startNode] == False):
            for j in range(len(graph[0])):
                if (graph[startNode][j] == True):
                    myStack.put(j)
                    parentArray[j] = startNode
        
        visArray[startNode] = True
        startNode = myStack.get()
    printPath(parentArray, goalNode)


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


goalNode = 5
depthFirstTraversal(graph)


