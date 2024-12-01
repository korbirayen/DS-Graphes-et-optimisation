import numpy as np
import networkx as nx
import itertools

class GraphProcessor:
    def __init__(self):
        """Initialize the graph processor with multiple input methods"""
        self.graph = None
        self.is_directed = False
        self.input_methods = {
            '1': 'Adjacency Matrix',
            '2': 'Incidence Matrix', 
            '3': 'Successor/Predecessor Dictionary'
        }

    def create_graph(self):
        """
        Create a graph with multiple input methods as specified in the PDF
        """
        # Graph type selection
        graph_type = input("Is this a directed graph? (yes/no): ").lower()
        self.is_directed = graph_type == 'yes'

        # Input method selection
        print("\nSelect Graph Input Method:")
        for key, method in self.input_methods.items():
            print(f"{key}. {method}")
        
        while True:
            input_choice = input("Enter input method (1-3): ")
            if input_choice in self.input_methods:
                break
            print("Invalid input method. Try again.")

        # Input graph based on selected method
        if input_choice == '1':
            return self._input_adjacency_matrix()
        elif input_choice == '2':
            return self._input_incidence_matrix()
        else:
            return self._input_successor_dictionary()

    def _input_adjacency_matrix(self):
        """Input graph via adjacency matrix"""
        while True:
            try:
                num_vertices = int(input("Enter number of vertices: "))
                print("\nEnter adjacency matrix (space-separated values):")
                
                matrix = []
                for i in range(num_vertices):
                    row = list(map(float, input(f"Row {i+1}: ").split()))
                    if len(row) != num_vertices:
                        raise ValueError("Matrix must be square!")
                    matrix.append(row)
                
                self.graph = np.array(matrix)
                return self.graph
            
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def _input_incidence_matrix(self):
        """Input graph via incidence matrix"""
        while True:
            try:
                num_vertices = int(input("Enter number of vertices: "))
                num_edges = int(input("Enter number of edges: "))
                
                print("\nEnter incidence matrix (space-separated values):")
                matrix = []
                for i in range(num_vertices):
                    row = list(map(float, input(f"Row {i+1}: ").split()))
                    if len(row) != num_edges:
                        raise ValueError("Incorrect number of edge entries!")
                    matrix.append(row)
                
                self.graph = np.array(matrix)
                return self.graph
            
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def _input_successor_dictionary(self):
        """Input graph via successor dictionary"""
        while True:
            try:
                num_vertices = int(input("Enter number of vertices: "))
                
                graph_dict = {}
                print("\nEnter successors for each vertex (space-separated vertex indices):")
                for i in range(num_vertices):
                    successors = list(map(int, input(f"Successors for vertex {i}: ").split()))
                    graph_dict[i] = successors
                
                # Convert dictionary to adjacency matrix
                matrix = np.zeros((num_vertices, num_vertices))
                for vertex, successors in graph_dict.items():
                    for succ in successors:
                        matrix[vertex][succ] = 1
                
                self.graph = matrix
                return self.graph
            
            except ValueError:
                print("Invalid input. Please use valid vertex indices.")

    def analyze_graph(self):
        """Comprehensive graph analysis based on PDF requirements"""
        # Convert to appropriate NetworkX graph type
        if self.is_directed:
            G = nx.from_numpy_array(self.graph, create_using=nx.DiGraph)
        else:
            G = nx.from_numpy_array(self.graph)

        print("\n=== Graph Analysis ===")

        if not self.is_directed:
            # Undirected Graph Specific Analysis
            self._undirected_graph_analysis(G)
        else:
            # Directed Graph Specific Analysis
            self._directed_graph_analysis(G)

    def _undirected_graph_analysis(self, G):
        """Analysis for undirected graphs as per PDF requirements"""
        print("\n--- Undirected Graph Analysis ---")

        # 1. Connectivity Verification
        connectivity = nx.is_connected(G)
        print("Graph Connectivity:", "Connected" if connectivity else "Not Connected")

        # 2. Maximum Spanning Tree (Prim's Algorithm)
        try:
            max_spanning_tree = nx.maximum_spanning_tree(G)
            print("\nMaximum Spanning Tree:")
            print("Edges:", list(max_spanning_tree.edges(data=True)))
        except Exception as e:
            print("Could not compute Maximum Spanning Tree:", str(e))

        # 3. Minimum Spanning Tree (Kruskal's Algorithm)
        try:
            min_spanning_tree = nx.minimum_spanning_tree(G)
            print("\nMinimum Spanning Tree:")
            print("Edges:", list(min_spanning_tree.edges(data=True)))
        except Exception as e:
            print("Could not compute Minimum Spanning Tree:", str(e))

    def _directed_graph_analysis(self, G):
        """Analysis for directed graphs as per PDF requirements"""
        print("\n--- Directed Graph Analysis ---")

        # 1. Strong Connectivity Verification
        strong_connectivity = nx.is_strongly_connected(G)
        print("Strong Connectivity:", "Connected" if strong_connectivity else "Not Connected")

        # If not strongly connected, compute reduced graph
        if not strong_connectivity:
            try:
                reduced_graph = nx.condensation(G)
                print("\nReduced Graph:")
                print("Nodes:", list(reduced_graph.nodes()))
                print("Edges:", list(reduced_graph.edges()))
            except Exception as e:
                print("Could not compute reduced graph:", str(e))

        # 2. Root Vertex Finding
        root_vertices = [v for v in G.nodes() if G.in_degree(v) == 0]
        print("\nRoot Vertices:", root_vertices if root_vertices else "None")

        # 3. Longest Path Arborescence (if root vertex exists)
        if root_vertices:
            root = root_vertices[0]
            try:
                longest_path = self._compute_longest_path_arborescence(G, root)
                print("\nLongest Path Arborescence:")
                print("Path from root vertex:", longest_path)
            except Exception as e:
                print("Could not compute longest path:", str(e))

    def _compute_longest_path_arborescence(self, G, start_vertex):
        """
        Compute longest path arborescence using Bellman-Ford approach
        """
        # Add edge weights if not present
        for (u, v, d) in G.edges(data=True):
            if 'weight' not in d:
                d['weight'] = 1

        # Compute longest path
        try:
            longest_paths = nx.single_source_bellman_ford(G, start_vertex)
            return longest_paths
        except nx.NetworkXError:
            print("Could not compute longest path.")
            return None

def main():
    """Main menu for graph processing tool"""
    processor = GraphProcessor()
    
    while True:
        print("\n=== Graph Processing Tool ===")
        print("1. Create New Graph")
        print("2. Analyze Graph")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            processor.create_graph()
            print("Graph created successfully!")
        
        elif choice == '2':
            if processor.graph is None:
                print("Please create a graph first!")
            else:
                processor.analyze_graph()
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

# Bonus Graph Comparison Class to fulfill Partie 2 requirements
class GraphComparator:
    @staticmethod
    def are_isomorphic(G1, G2):
        """
        Check if two graphs are isomorphic
        """
        graph1 = nx.from_numpy_array(G1)
        graph2 = nx.from_numpy_array(G2)

        matcher = nx.isomorphism.GraphMatcher(graph1, graph2)
        
        if matcher.is_isomorphic():
            return True, matcher.mapping
        return False, None

    @staticmethod
    def is_eulerian(G):
        """
        Check if a graph is Eulerian
        """
        graph = nx.from_numpy_array(G)
        
        # For undirected graph
        if not nx.is_directed(graph):
            return nx.is_eulerian(graph)
        
        # For directed graph
        else:
            return all(graph.in_degree(node) == graph.out_degree(node) 
                       for node in graph.nodes())

def graph_comparison_demo():
    """Demonstration of graph comparison features"""
    print("\n=== Graph Comparison ===")
    
    # Create first graph
    print("Graph 1:")
    processor1 = GraphProcessor()
    G1 = processor1.create_graph()
    
    # Create second graph
    print("\nGraph 2:")
    processor2 = GraphProcessor()
    G2 = processor2.create_graph()
    
    comparator = GraphComparator()
    
    # Isomorphism check
    is_iso, mapping = comparator.are_isomorphic(G1, G2)
    print("\nIsomorphism Check:")
    print("Are graphs isomorphic?", is_iso)
    if is_iso:
        print("Isomorphism Mapping:", mapping)
    
    # Eulerian check
    print("\nEulerian Check:")
    print("Is Graph 1 Eulerian?", comparator.is_eulerian(G1))
    print("Is Graph 2 Eulerian?", comparator.is_eulerian(G2))

# Add graph comparison option to main menu
def enhanced_main():
    """Enhanced main menu with graph comparison option"""
    while True:
        print("\n=== Advanced Graph Processing Tool ===")
        print("1. Create and Analyze Graph")
        print("2. Compare Graphs")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            main()
        elif choice == '2':
            graph_comparison_demo()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the enhanced program
if __name__ == "__main__":
    enhanced_main()