# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:21:16 2022

@author: 20pt02
"""
import networkx as nx
import matplotlib.pyplot as plt

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

list_vertices = ['1','2','3','4','5','6','7','8','9']
goalstates = ['6','9','7','5']
visited = dict()
for i in list_vertices:
    visited[i] = False
g1 = nx.Graph()
for key in graph:
    if len(graph[key]) == 0:
        continue
    for i in graph[key]:
        g1.add_edge(key, i)

queue = []
path = []
s = '4'
queue.append(s)
visited[s] = True
print('The BFS of the given graph is:')
while len(queue) != 0:
    #print(queue)
    s = queue.pop(0)
    path.append(s)
    print(s)
    for i in graph[s]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True

print(path)
color_map=[]
for node in g1:
    color_map.append('Gray')
edge_color_map=[]
for u,v in g1.edges:
    if u in path and v in path:
        edge_color_map.append('Green')
    else:
        edge_color_map.append('Black')
        
plt.figure()
plt.title('Visualization of bfs')
nx.draw(g1, node_color=color_map,edge_color=edge_color_map,with_labels=True)
plt.show()
    