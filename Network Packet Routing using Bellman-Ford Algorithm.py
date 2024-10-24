class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        self.graph = []  # List to store all edges

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Bellman-Ford algorithm to find the shortest path from source to all vertices
    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0  # Distance of source vertex from itself is always 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the calculated shortest distances
        self.print_solution(dist)

    # Utility function to print the calculated distances
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# Example usage:
g = Graph(5)  # Creating a graph with 5 vertices

# Adding edges to the graph
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(4, 3, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 1, -3)

# Running Bellman-Ford algorithm from vertex 0
g.bellman_ford(0)
