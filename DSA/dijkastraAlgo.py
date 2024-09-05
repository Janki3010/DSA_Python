import sys


class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                       for row in range(vertices)
                      ]
    def printSol(self,dist):
        print("Vertex \tDistance from Source")
        for node in range(self.v):
            print(node,"\t    ", dist[node])

    def minDistance(self,dist,sptSet):
        min = sys.maxsize
        for u in range(self.v):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        sptSet = [False] * self.v

        for count in range(self.v):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.v):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSol(dist)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 8, 0, 11, 0, 0, 0, 0],
        [0, 8, 0, 7, 0, 0, 4, 0, 2],
        [0, 0, 7, 0, 0, 0, 14, 9, 0],
        [8, 11, 0, 0, 0, 1, 0, 0, 7],
        [0, 0, 0, 0, 1, 0, 2, 0, 6],
        [0, 0, 4, 14, 0, 2, 0, 10, 0],
        [0, 0, 0, 9, 0, 0, 10, 0, 0],
        [0, 0, 2, 0, 7, 6, 0, 0, 0]
    ]
    g.dijkstra(0)