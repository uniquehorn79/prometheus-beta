import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_path():
    """Test a simple graph with a straightforward shortest path."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 6  # 2 (A to C) + 1 (C to B) + 3 (B to D)

def test_single_node_path():
    """Test path from a node to itself."""
    graph = {
        'A': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_complex_path():
    """Test a more complex graph with multiple possible routes."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4

def test_start_node_not_in_graph():
    """Test error when start node is not in the graph."""
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start node 'C' not found in the graph"):
        dijkstra_shortest_path(graph, 'C', 'B')

def test_end_node_not_in_graph():
    """Test error when end node is not in the graph."""
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    with pytest.raises(ValueError, match="End node 'C' not found in the graph"):
        dijkstra_shortest_path(graph, 'A', 'C')

def test_no_path_exists():
    """Test error when no path exists between nodes."""
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists between A and C"):
        dijkstra_shortest_path(graph, 'A', 'C')