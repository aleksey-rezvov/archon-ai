def truncate_str(s: str, max_length: int = 100) -> str:
    """Truncate string to max_length and add ellipsis if needed."""
    s = str(s)
    return f"{s[:max_length]}..." if len(s) > max_length else s 
