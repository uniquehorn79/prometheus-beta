def validate_single_digit_ip_address(ip_address: str) -> bool:
    """
    Validate if the input is a valid IP address with single-digit numeric segments.
    
    Args:
        ip_address (str): The IP address string to validate
    
    Returns:
        bool: True if the IP address is valid, False otherwise
    
    Validation Rules:
    - Must have exactly 4 segments separated by dots
    - Each segment must be a single digit (0-9)
    """
    # Check if the input is a string and not empty
    if not isinstance(ip_address, str) or not ip_address:
        return False
    
    # Split the IP address into segments
    segments = ip_address.split('.')
    
    # Check if there are exactly 4 segments
    if len(segments) != 4:
        return False
    
    # Validate each segment
    for segment in segments:
        # Check if segment is a single digit
        if (len(segment) != 1 or 
            not segment.isdigit()):
            return False
    
    return True