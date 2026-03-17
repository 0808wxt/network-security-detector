import re

class XSSDetector:
    """
    A class to detect XSS vulnerabilities in given input.
    """

    def __init__(self, input_data):
        self.input_data = input_data

    def is_vulnerable(self):
        """
        Checks if the given input contains XSS vulnerabilities.
        """
        xss_patterns = [
            r'<script.*?>.*?</script>',
            r'javascript:.*?;',
            r'(<[^>]+>.*?)+',
            r'\b(on\w+=)\s*".*?"',
            r'\b(on\w+=)\s*\2.*?\2',
            r'\b(on\w+=)\s*\7.*?\7',
        ]

        for pattern in xss_patterns:
            if re.search(pattern, self.input_data, re.IGNORECASE):
                return True
        return False

# Example usage:
# detector = XSSDetector("<script>alert('XSS')</script>")
# print(detector.is_vulnerable())  # Should return True