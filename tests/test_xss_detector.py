import unittest

class TestXSSDetector(unittest.TestCase):

    def test_simple_xss(self):
        input_data = "<script>alert('xss');</script>"
        result = xss_detector(input_data)
        self.assertTrue(result)

    def test_safe_input(self):
        input_data = "Hello, World!"
        result = xss_detector(input_data)
        self.assertFalse(result)

    def test_complex_xss(self):
        input_data = "<img src=x onerror=alert('xss') />"
        result = xss_detector(input_data)
        self.assertTrue(result)

    def test_no_input(self):
        input_data = ""
        result = xss_detector(input_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()