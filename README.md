# Graph Coloring Solver

This program implements a **backtracking algorithm** to solve the **graph coloring problem**. It determines whether a given graph can be colored with at most **K colors** such that no two adjacent vertices share the same color.

---

## Input Format (File: `graph_input.txt`):
1. **First line**: Three integers - `n m k`
   - `n` → Number of vertices
   - `m` → Number of edges
   - `k` → Number of colors available
2. **Next `m` lines**: Each line contains two integers `u v` (0-based index) representing an edge between vertex `u` and vertex `v`.

---

## Example 1 (Coloring Possible):
### **Input (`graph_input.txt`):**
```
4 3 3
0 1
1 2
2 3
```

### **Output:**
```
Coloring Possible with 3 Colors
Color Assignment: [1, 2, 1, 2]
```

---

## Example 2 (Coloring Not Possible):
### **Input (`graph_input.txt`):**
```
3 3 2
0 1
1 2
2 0
```

### **Output:**
```
Coloring Not Possible with 2 Colors
```

---

