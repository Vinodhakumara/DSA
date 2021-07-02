# Graph Data Structur Undirect Cycle Graph
gdict = {
    "vinod":["manu","salu","rahul"],
    "manu":["vinod","salu"], 
    "salu":["vinod","manu","hem"],
    "tom":["hem","rahul"],
    "hem": ["tom","salu"],
    "rahul":["vinod","tom"]
}
class Graph:
    def __init__(self, gdata=None):
        self.gdata= gdata
    # Add edges
    def addEdge(self, node, edge): 
        self.gdata[node].append(edge)
    # Count Edges
    def countEdges(self, node):
        return len(self.gdata[node])
    # Show edges
    def showEdges(self,node):
        return self.gdata[node]
    # Add Nodes
    def addNode(self, node):
        self.gdata[node] = []
    # Count Nodes
    def countNodes(self):
        return len(self.gdata)
    # Normal Traversal 
    def showNode(self):
        return self.gdata.keys()
    # Traversal: BFS-Breadth First Search
    def bfs(self,vertex):
        queue = [vertex]                         # Add all nodes to a queue
        visited = [vertex]                       # It's like a dummy to mentioned which all visited
        while queue:                             # Runs until queue is empty
            deVertex = queue.pop(0)              # Pop(remove) Visited Node
            print(deVertex)
            for adjacentVertex in self.gdata[deVertex]:  # Loop all of deVertex Edges(connections)
                if adjacentVertex not in visited:         # Only runs if node is not visited
                    queue.append(adjacentVertex)    # Add which all needs to be visit
                    visited.append(adjacentVertex)  # Add to visit a nodes
    # Traversal: DFS-Depth First Search
    def dfs(self,vertex):
        stack = [vertex]                         # Add all nodes to a queue
        visited = [vertex]                       # It's like a dummy to mentioned which all visited
        while queue:                             # Runs until queue is empty
            popVertex = queue.pop()              # Pop(remove) Visited Node
            print(popVertex)
            for adjacentVertex in self.gdata[popVertex]:  # Loop all of deVertex Edges(connections)
                if adjacentVertex not in visited:         # Only runs if node is not visited
                    stack.append(adjacentVertex)    # Add which all needs to be visit
                    visited.append(adjacentVertex)  # Add to visit a nodes
    # Topologocal Ordering
    def topologicalSort(self):
        visited=[]
        stack=[]
        for k in self.graph:
            if k not in visited:
                self.toplogicalSortHelpper(k,visited,stack)
    # Topological Sort Helpper
    def topologicalSortHelpper(self,n,visited,stack):
        visited.append(n)
        for i in self.graph[n]:
            if i not in visited:
                self.topologicalSortHelpper(i,visited,stack)
        stack.insert(0,n)
    
a = Graph(gdict)
a.showNode()
a.bfs("manu")