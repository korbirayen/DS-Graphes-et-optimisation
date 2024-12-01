class Graph:
    def __init__(self):
        self.graph_type = None  # 'directed' or 'undirected'
        self.graph_representation = None  # 'adjacency', 'incidence', or 'dictionary'
        self.adj_matrix = []
        self.inc_matrix = []
        self.dictionary = {}
        self.n = 0

    def acquire_graph(self):
        print("Enter the type of graph (directed/undirected):")
        self.graph_type = input().strip().lower()
        print("Enter the input method (adjacency/incidence/dictionary):")
        self.graph_representation = input().strip().lower()

        if self.graph_representation == 'adjacency':
            self._input_adjacency_matrix()
        elif self.graph_representation == 'incidence':
            self._input_incidence_matrix()
        elif self.graph_representation == 'dictionary':
            self._input_dictionary()
        else:
            print("Invalid input method.")

    def _input_adjacency_matrix(self):
        print("Enter the number of vertices:")
        self.n = int(input().strip())
        print("Enter the adjacency matrix row by row:")
        self.adj_matrix = [list(map(int, input().strip().split())) for _ in range(self.n)]

    def _input_incidence_matrix(self):
        print("Enter the number of vertices:")
        self.n = int(input().strip())
        print("Enter the incidence matrix row by row:")
        self.inc_matrix = [list(map(int, input().strip().split())) for _ in range(self.n)]

    def _input_dictionary(self):
        print("Enter the number of vertices:")
        self.n = int(input().strip())
        print("Enter the dictionary of neighbors (key: list of neighbors):")
        for _ in range(self.n):
            vertex, neighbors = input("Vertex and neighbors (e.g., 1: 2,3): ").split(':')
            self.dictionary[int(vertex.strip())] = list(map(int, neighbors.strip().split(',')))

    def display_graph(self):
        print("Graph Type:", self.graph_type)
        if self.graph_representation == 'adjacency':
            print("Adjacency Matrix:")
            for row in self.adj_matrix:
                print(row)
        elif self.graph_representation == 'incidence':
            print("Incidence Matrix:")
            for row in self.inc_matrix:
                print(row)
        elif self.graph_representation == 'dictionary':
            print("Dictionary Representation:")
            for vertex, neighbors in self.dictionary.items():
                print(f"{vertex}: {neighbors}")

# Main function
if __name__ == "__main__":
    graph = Graph()
    graph.acquire_graph()
    graph.display_graph()
