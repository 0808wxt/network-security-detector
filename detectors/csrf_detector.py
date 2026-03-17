# CSRF Vulnerability Detection Code

import requests
from urllib.parse import urlparse, urljoin

class CSRFDetector:
    def __init__(self, target_url):
        self.target_url = target_url

    def find_forms(self):
        try:
            response = requests.get(self.target_url)
            response.raise_for_status()  # Raises an error for 4xx/5xx responses
            forms = response.text.split('<form')  # Simple form detection
            return forms
        except requests.RequestException as e:
            print(f"Error fetching target URL: {e}")
            return []

    def check_csrf(self):
        forms = self.find_forms()
        for form in forms:
            if 'csrf' in form.lower() or 'token' in form.lower():
                print("Potential CSRF protection found.")
            else:
                print("No CSRF protection detected in form.")

if __name__ == '__main__':
    target = input("Enter the target URL: ").strip()
    detector = CSRFDetector(target)
    detector.check_csrf()