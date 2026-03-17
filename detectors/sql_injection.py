def detect_sql_injection(query):
    sql_injection_patterns = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' UNION SELECT",
        "' DROP TABLE",
        "' AND 'a'='a",
        """
    ]

    for pattern in sql_injection_patterns:
        if pattern in query:
            return True
    return False

# Example of usage:
if __name__ == '__main__':
    user_input = "SELECT * FROM users WHERE username = 'admin' AND password = 'password'"  # Simulate user input
    if detect_sql_injection(user_input):
        print("SQL Injection detected!")
    else:
        print("No SQL Injection detected.")
