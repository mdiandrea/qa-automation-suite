🧪 SQL Test Suite
This module validates SQL queries against a mock in-memory database using Python’s sqlite3 engine. It’s designed to simulate backend QA scenarios and ensure query accuracy before deployment.

📂 Folder Structure
Code
sql_tests/
├── sample_query.sql         # SQL query to be tested
├── test_queries.py          # Python test runner
reports/
└── sql_report.txt           # Log of test results
🚀 How It Works
test_queries.py creates a temporary SQLite database

It populates a users table with mock data

It loads and executes sample_query.sql

It compares the result to expected output

It prints PASS or FAIL and logs details to sql_report.txt

✅ Sample Query
sql
SELECT first_name, last_name FROM users WHERE last_name IN ('Doe', 'Smith');
🧠 Expected Results
Defined in test_queries.py:

python
expected_results = {
    'sample_query.sql': [('John', 'Doe'), ('Jane', 'Smith')]
}
📊 Output Example
Code
Actual result: [('John', 'Doe'), ('Jane', 'Smith')]
sample_query.sql: PASS
🔧 Future Enhancements
Loop through all .sql files automatically

Externalize expected results into .json or .yaml

Add colored console output for quick feedback

Integrate with pytest or CI/CD pipelines
