import pytest
from src.depth_first_search import depth_first_search

def test_basic_dfs():
    """
    Test basic DFS traversal on a simple graph.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Test starting from 'A'
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_dfs_with_callback():
    """
    Test DFS with a callback function.
    """
    visited_nodes = []
    
    def mock_callback(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    
    depth_first_search(graph, 'A', visit_callback=mock_callback)
    assert visited_nodes == ['A', 'B', 'D', 'C', 'E']

def test_dfs_single_node_graph():
    """
    Test DFS on a graph with only one node.
    """
    graph = {'A': []}
    result = depth_first_search(graph, 'A')
    assert result == ['A']

def test_invalid_start_node():
    """
    Test that an error is raised when the start node is not in the graph.
    """
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_invalid_graph_type():
    """
    Test that an error is raised when an invalid graph type is provided.
    """
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        depth_first_search([], 'A')  # Passing a list instead of a dict

def test_disconnected_graph():
    """
    Test DFS on a graph with disconnected components.
    """
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C'],
        'E': []
    }
    
    # Start from a node in one component
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']
    
    # Start from a node in another component
    result = depth_first_search(graph, 'C')
    assert result == ['C', 'D']