# Graph Data Structur Undirect Cycle Graph
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
        return self.gdata[node] = []
    # Traversal BSF : DSF
    def showNode(self):
        return self.gdata.keys()
    # Count Nodes
    def countNodes(self):
        return len(self.gdata)
    
a = Graph({"a":[1,2,3,4],"b":[5,6], "c":[7,8],"d":[9]})
a.showNode()