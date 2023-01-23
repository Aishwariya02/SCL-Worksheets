# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        #print (node)
        path.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
g = nx.Graph()

graph = {
  '1':  ['2','3'],
  '2' : ['4','5'], 
  '3' : ['6'],
  '4' : ['7','8'],
  '5' : [],
  '6' : [],
  '7' : ['9'],
  '8' : [],
  '9' : []
}

for key in graph:
    if len(graph[key]) == 0:
        continue
    for i in graph[key]:
        g.add_edge(key, i)

visited = set() # Set to keep track of visited nodes of graph.
path = []


# Driver Code
s = '4'
print("Following is the path for Depth-First Search")
dfs(visited, graph, s)
print(path)
color_map=[]
# print(self.src)
# print(self.dest)
for node in g:
    color_map.append('Gray')
#print(self.path)
edge_color_map=[]
for u,v in g.edges:
    if u in path and v in path:
        edge_color_map.append('Green')
    else:
        edge_color_map.append('Black')
        
plt.figure()
plt.title('Visualization of dfs')
nx.draw(g, node_color=color_map,edge_color=edge_color_map,with_labels=True)
plt.show()