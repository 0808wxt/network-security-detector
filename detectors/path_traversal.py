import os

# Path Traversal Vulnerability Detection

def is_safe_path(base_path, user_input_path):
    # Safely join base path with the user input path
    full_path = os.path.join(base_path, user_input_path)
    # Normalize the path to remove any symbolic links, .. etc.
    full_path = os.path.normpath(full_path)
    # Check if the normalized path starts with the base path
    return full_path.startswith(os.path.abspath(base_path))

# Example usage
if __name__ == '__main__':
    base_path = '/var/www/html/'
    user_input = '../../etc/passwd'  # Example input that could be a path traversal
    if is_safe_path(base_path, user_input):
        print('Path is safe')
    else:
        print('Potential path traversal vulnerability detected!')