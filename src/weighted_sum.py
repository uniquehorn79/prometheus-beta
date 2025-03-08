from typing import List, Union, Tuple

def compute_weighted_sum(numbers: List[Union[int, float]], weights: List[Union[int, float]]) -> float:
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.

    Args:
        numbers (List[Union[int, float]]): A list of numbers to be weighted.
        weights (List[Union[int, float]]): A list of weights corresponding to the numbers.

    Returns:
        float: The total weighted sum.

    Raises:
        ValueError: If the lengths of numbers and weights are not equal or if lists are empty.
        TypeError: If lists contain non-numeric values.
    """
    # Check if lists are empty
    if not numbers or not weights:
        raise ValueError("Input lists cannot be empty")

    # Check if lists have equal length
    if len(numbers) != len(weights):
        raise ValueError("Numbers and weights lists must have equal length")

    # Validate numeric types
    try:
        numbers = [float(num) for num in numbers]
        weights = [float(weight) for weight in weights]
    except (TypeError, ValueError):
        raise TypeError("All elements in numbers and weights must be numeric")

    # Compute weighted sum
    weighted_sum = sum(num * weight for num, weight in zip(numbers, weights))
    return weighted_sum