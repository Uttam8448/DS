//job scheduling
arr = [
['a', 2, 100], 
    ['b', 2, 20], 
    ['c', 1, 40], 
    ['d', 3, 35], 
    ['e', 1, 25]
    ]

print("Following is maximum profit sequence of Jobs: ")
t = 3

arr.sort(key=lambda x:x[2], reverse=True)

result = [False] * t
job = ['-1'] * t

for i in range(len(arr)):
   for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
     if result[j] is False:
       result[j] = True
       job[j] = arr[i][0]
       break

print(job)


//minnimum spanning graph
inf=99999
V=4
G=[[0,2,4,0],
  [2,0,1,3],
  [4,1,0,2],
  [0,3,2,0]]

visited=[0,0,0,0]
visited[0]=True
no_edge=0
cost=0

while (no_edge<V-1):
    x=0
    y=0
    min=inf
    for i in range(V):
        if visited[i]:
            for j in range(V):
                if ((not visited[j]) and G[i][j]):
                    if G[i][j]<min:
                        min=G[i][j]
                        x=i
                        y=j
    print(str(x),"-",str(y),": ",G[x][y])
    cost+=G[x][y]
    no_edge+=1 
    visited[y]=True

print("cost of tree: ",cost)

//single source shortest
import heapq

def prim(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    
    edge_heap = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex].items()]
    
    heapq.heapify(edge_heap)
    visited.add(start_vertex)
    
    while edge_heap:
        weight, source, destination = heapq.heappop(edge_heap)
        if destination not in visited:
            visited.add(destination)
            minimum_spanning_tree.append((source, destination, weight))
            for neighbor, weight in graph[destination].items():
                if neighbor not in visited:
                    heapq.heappush(edge_heap, (weight, destination, neighbor))
    
    return minimum_spanning_tree

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")


//Prims minimum
inf=99999
V=4
G=[[0,2,4,0],
  [2,0,1,3],
  [4,1,0,2],
  [0,3,2,0]]

visited=[0,0,0,0]
visited[0]=True
no_edge=0
cost=0

while (no_edge<V-1):
    x=0
    y=0
    min=inf
    for i in range(V):
        if visited[i]:
            for j in range(V):
                if ((not visited[j]) and G[i][j]):
                    if G[i][j]<min:
                        min=G[i][j]
                        x=i
                        y=j
    print(str(x),"-",str(y),": ",G[x][y])
    cost+=G[x][y]
    no_edge+=1 
    visited[y]=True

print("cost of tree: ",cost)



//dijkstra minimum

import heapq

def dijkstra(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    
    edge_heap = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex].items()]
    
    heapq.heapify(edge_heap)
    visited.add(start_vertex)
    
    while edge_heap:
        weight, source, destination = heapq.heappop(edge_heap)
        if destination not in visited:
            visited.add(destination)
            minimum_spanning_tree.append((source, destination, weight))
            for neighbor, weight in graph[destination].items():
                if neighbor not in visited:
                    heapq.heappush(edge_heap, (weight, destination, neighbor))
    
    return minimum_spanning_tree

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

minimum_spanning_tree = dijkstra(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
