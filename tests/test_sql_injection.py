import unittest
from sql_injection_detector import is_sql_injection

class TestSQLInjectionDetector(unittest.TestCase):

    def test_valid_query(self):
        self.assertFalse(is_sql_injection("SELECT * FROM users WHERE id = 1"))

    def test_simple_injection(self):
        self.assertTrue(is_sql_injection("1; DROP TABLE users;"))

    def test_injection_with_comment(self):
        self.assertTrue(is_sql_injection("1 OR '1'='1'--"))

    def test_encoded_injection(self):
        self.assertTrue(is_sql_injection("%27%20OR%20%271%27%3D%271%27"))

    def test_no_injection(self):
        self.assertFalse(is_sql_injection("SELECT * FROM users WHERE name = 'Alice'"))

if __name__ == '__main__':
    unittest.main()