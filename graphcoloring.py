
def is_safe(vertex, color, graph, colors):
    
    for neighbor in graph[vertex]:  
        if colors[neighbor] == color:  
            return False  
    return True  

def assign_colors(graph, colors, vertex, k, n):
   
    if vertex == n:  
        return True
    
    for color in range(1, k + 1): 
        if is_safe(vertex, color, graph, colors):  
            colors[vertex] = color  
            if assign_colors(graph, colors, vertex + 1, k, n):  
                return True
            colors[vertex] = 0  
    
    return False  

def graph_coloring(n, k, edges):
   
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [0] * n 
    
    if assign_colors(graph, colors, 0, k, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {k} Colors")

def read_file(filename):
    
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())  
        edges = []
        for i in range(m):
             edges.append(tuple(map(int, file.readline().split())))
   
    return n, k, edges 

if __name__ == "__main__":
    filename = "graph_input.txt"  
    n, k, edges = read_file(filename)  
    graph_coloring(n, k, edges)  
