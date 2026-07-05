# SSH Log Analyzer

A simple Python-based log analysis tool that parses Linux SSH authentication logs and generates a security summary. This project was built to practice Python file handling, string parsing, and basic security automation concepts.

## Features

- Reads Linux SSH authentication logs
- Counts total log entries
- Counts successful logins
- Counts failed login attempts
- Identifies unique IP addresses
- Lists the most active failed login IPs
- Detects possible brute-force attacks (more than 3 failed attempts)
- Displays users who successfully logged in

## Project Structure

```
log-analyzer/
│
├── src/
│   ├── log_analyzer.py
│   └── sample.log
│
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10+
- Standard Library
  - ipaddress

No external packages are required.

## Sample Output

```
============ Log Summary ============

Total log entries: 30

Successful logins: 7

Failed logins: 18

Unique IPs: 9

Top Failed IPs:
185.220.101.12 : 6
61.177.172.44 : 5
45.33.32.156 : 3

Possible Brute Force Attempts (>3 failures)
-------------------------------------------
185.220.101.12
61.177.172.44

Users Logged in:
----------------
alice
bob
charlie
david
eve
frank
george
```

## Concepts Practiced

- File handling
- Functions
- Lists
- String manipulation
- Basic log parsing
- Python standard library
- Simple security analysis

## Future Improvements

- Parse logs using regular expressions
- Use dictionaries for faster IP counting
- Export reports to CSV or JSON
- Add command-line arguments
- Support multiple log file formats
- Improve brute-force detection logic

## License

This project is intended for educational and portfolio purposes.