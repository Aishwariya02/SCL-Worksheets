# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:45:33 2022

@author: 20pt02
"""

import networkx as nx
import matplotlib.pyplot as plt

# graph = {
#   '1':  ['2','3'],
#   '2' : ['4','5'], 
#   '3' : ['6'],
#   '4' : ['7','8'],
#   '5' : [],
#   '6' : [],
#   '7' : ['9'],
#   '8' : [],
#   '9' : []
# }

graph = {
    '0' : ['1','2','4'],
    '1' : ['3','5'],
    '2' : ['6'],
    '4' : [],
    '3' : [],
    '5' : [],
    '6' : []}

#depths = [0,0,1,1,2,2,2,3,3,4]
currdepth = 0
limit = 1
#goals = ['6']

g = nx.Graph()
for key in graph:
    if len(graph[key]) == 0:
        continue
    for i in graph[key]:
        g.add_edge(key, i)
# nx.draw(g,with_labels = True)

s = '0'
visited = set()
path = []
def dfs(visited, graph, node, currdepth):  #function for dfs 
    if node not in visited and currdepth <= limit:
        path.append(node)
        visited.add(node)
        currdepth += 1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, currdepth)
dfs(visited,graph,s,currdepth)
print(path)
color_map=[]

for node in g:
    color_map.append('Gray')
edge_color_map=[]
for u,v in g.edges:
    if u in path and v in path:
        edge_color_map.append('Green')
    else:
        edge_color_map.append('Black')
        
plt.figure()
plt.title('Visualization of dls')
nx.draw(g, node_color=color_map,edge_color=edge_color_map,with_labels=True)
plt.show()



    