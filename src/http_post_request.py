import requests
from typing import Dict, Any, Optional

def send_http_post_request(
    url: str, 
    data: Optional[Dict[str, Any]] = None, 
    headers: Optional[Dict[str, str]] = None, 
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL for the POST request.
        data (dict, optional): The payload to send in the request. Defaults to None.
        headers (dict, optional): Custom headers for the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.

    Raises:
        ValueError: If the URL is empty or None.
        requests.RequestException: For network-related errors.
    """
    # Validate input URL
    if not url:
        raise ValueError("URL cannot be empty")

    # Set default headers if not provided
    headers = headers or {}
    headers.setdefault('Content-Type', 'application/json')

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return response details
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'data': response.json() if response.text else {}
        }

    except requests.HTTPError:
        # Re-raise HTTP errors without wrapping
        raise
    except requests.RequestException as e:
        # Handle other request-related exceptions
        raise RuntimeError(f"HTTP POST request failed: {str(e)}") from e