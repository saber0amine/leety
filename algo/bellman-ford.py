class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Initialiser les distances de tous les nœuds à l'infini
        distance = [float('inf')] * self.V
        distance[src] = 0

        # Relaxation des arêtes V-1 fois
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Vérification des cycles de poids négatif
        for u, v, w in self.graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print("Le graphe contient un cycle de poids négatif")
                return

        # Affichage des distances minimales
        print("Distances minimales depuis le nœud source:")
        for i in range(self.V):
            print(f"Nœud {i}: Distance = {distance[i]}")


# Exemple d'utilisation
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)
