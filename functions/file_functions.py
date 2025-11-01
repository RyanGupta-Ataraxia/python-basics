# file_functions.py
# Basic file handling functions

def write_to_file(filename, content):
    """Write content to a file (overwrites existing content)."""
    with open(filename, 'w') as f:
        f.write(content)
    return f"Content written to {filename}"

def read_from_file(filename):
    """Read and return content from a file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {filename} not found."

def append_to_file(filename, content):
    """Append content to an existing file."""
    with open(filename, 'a') as f:
        f.write(content)
    return f"Content appended to {filename}"
