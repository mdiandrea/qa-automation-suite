python
import sqlite3
import os

# Define path to SQL files
SQL_DIR = os.path.dirname(__file__)
REPORT_PATH = os.path.join(SQL_DIR, '..', 'reports', 'sql_report.txt')

# Sample expected results for validation
expected_results = {
    'sample_query.sql': [('John', 'Doe'), ('Jane', 'Smith')]
}

def run_sql_test(file_name):
    with sqlite3.connect(':memory:') as conn:
        cursor = conn.cursor()

        # Create mock table and data
        cursor.execute("CREATE TABLE users (first_name TEXT, last_name TEXT)")
        cursor.executemany("INSERT INTO users VALUES (?, ?)", [
            ('John', 'Doe'),
            ('Jane', 'Smith'),
            ('Alice', 'Johnson')
        ])

        # Load and execute SQL query
        with open(os.path.join(SQL_DIR, file_name), 'r') as f:
            query = f.read()
            cursor.execute(query)
            result = cursor.fetchall()

        # Compare results
        expected = expected_results.get(file_name, [])
        passed = result == expected

        # Log result
        with open(REPORT_PATH, 'a') as report:
            report.write(f"{file_name}: {'PASS' if passed else 'FAIL'}\n")
            report.write(f"Expected: {expected}\nActual: {result}\n\n")

        print(f"{file_name}: {'PASS' if passed else 'FAIL'}")

if __name__ == "__main__":
    run_sql_test('sample_query.sql')