# Graph Processing Project

## Project Description
This project implements various graph processing algorithms as per the "Graphes et Optimisation" assignment requirements.

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Installation
1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python graph_processing.py
```

### Input Methods
1. Manual Input: Enter graph vertices and adjacency matrix manually
2. File Input: Load graph from a text file with adjacency matrix

### Features
- Graph acquisition
- Connectivity verification
- Spanning tree algorithms
- Graph comparison
- Isomorphism detection
- Eulerian graph analysis

## Example Input Formats
### Adjacency Matrix (Undirected)
```
5
0 4 0 0 2
4 0 3 0 1
0 3 0 5 0
0 0 5 0 6
2 1 0 6 0
```

### Adjacency Matrix (Directed)
```
5
0 1 0 0 2
0 0 3 0 1
0 0 0 5 0
0 0 0 0 6
0 0 0 0 0
```

## Menu Options
1. Undirected Graph Operations
2. Directed Graph Operations
3. Graph Comparison
4. Exit

## Troubleshooting
- Ensure correct matrix dimensions
- Use space-separated values
- Check network connectivity
