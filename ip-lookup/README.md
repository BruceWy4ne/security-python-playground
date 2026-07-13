# IP Reputation Lookup

A simple Python command-line tool that checks the reputation of an IP address using the AbuseIPDB API.

The program validates user input, queries the AbuseIPDB threat intelligence database, and displays information such as abuse confidence score, ISP, country, usage type, and report history. This project was built to practice working with authenticated REST APIs and cybersecurity threat intelligence.

---

## Features

- Validate IPv4 and IPv6 addresses
- Query the AbuseIPDB API
- Display:
  - IP Address
  - Country Code
  - Internet Service Provider (ISP)
  - Usage Type
  - Abuse Confidence Score
  - Total Reports
  - TOR Exit Node Status
  - Whitelist Status
  - Last Reported Date
- Handles invalid IP address input
- Handles basic API response errors

---

## Technologies Used

- Python 3
- requests
- ipaddress
- AbuseIPDB REST API

---

## Project Structure

```
ip-reputation-lookup/
│
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    └── ip_reputation_lookup.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/security-python-playground.git
```

Navigate to the project folder:

```bash
cd security-python-playground/ip-reputation-lookup
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a free account at **AbuseIPDB** and generate an API key.

Replace the placeholder inside the source code:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key before running the program.

---

## Usage

Run the program:

```bash
python src/ip_reputation_lookup.py
```

Enter an IP address when prompted:

```
Enter an IP address: 8.8.8.8
```

Example output:

```
============================================
            IP Reputation Report
============================================

IP Address: 8.8.8.8
Country: US
ISP: Google LLC
Usage Type: Public DNS
Abuse Score: 0
Total Reports: 0
TOR Exit Node: False
Whitelisted: False
Last Reported: None
```

---

## What I Learned

During this project I learned how to:

- Validate IP addresses using Python
- Authenticate with REST APIs using API keys
- Send HTTP GET requests with custom headers
- Use query parameters in API requests
- Parse nested JSON responses
- Build a command-line cybersecurity utility

---

## Future Improvements

- Store API key using environment variables
- Handle network exceptions
- Display "Safe" or "Suspicious" based on abuse score
- Support batch IP lookups
- Export reports to CSV
- Improve terminal output formatting

---

## Data Source

AbuseIPDB

https://www.abuseipdb.com/