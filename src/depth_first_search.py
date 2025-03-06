from typing import List, Any, Callable, Set, Optional

def depth_first_search(graph: dict, start: Any, 
                       visit_callback: Optional[Callable[[Any], None]] = None) -> List[Any]:
    """
    Perform Depth-First Search on a graph.

    Args:
        graph (dict): A dictionary representing an adjacency list graph.
                      Keys are nodes, values are lists of adjacent nodes.
        start (Any): The starting node for the search.
        visit_callback (Optional[Callable]): Optional callback function 
                                             to be called on each visited node.

    Returns:
        List[Any]: A list of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid dictionary.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Set to keep track of visited nodes to prevent cycles
    visited: Set[Any] = set()
    # List to store the order of nodes visited
    traversal_order: List[Any] = []
    
    def dfs_recursive(node: Any):
        """
        Internal recursive DFS function.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Optional callback for node visit
        if visit_callback:
            visit_callback(node)
        
        # Add to traversal order
        traversal_order.append(node)
        
        # Explore unvisited adjacent nodes
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the given start node
    dfs_recursive(start)
    
    return traversal_order