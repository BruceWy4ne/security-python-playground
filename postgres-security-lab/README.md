# 🔐 PostgreSQL Security Lab

A hands-on PostgreSQL lab built to practice relational database fundamentals and connect Python with PostgreSQL using Psycopg. The project uses a simple user and login-attempt database to simulate security-related data investigation.

## Features

- Create a PostgreSQL database schema
- Create relational `users` and `login` tables
- Use primary keys and foreign keys
- Insert multiple records using SQL
- Query and filter login activity
- Analyze failed login attempts
- Use `JOIN` and `LEFT JOIN`
- Use aggregation with `COUNT`, `GROUP BY`, and `HAVING`
- Sort and limit query results
- Execute SQL files using `psql`
- Connect Python to PostgreSQL using Psycopg
- Execute SQL queries from Python
- Use parameterized SQL queries
- Process PostgreSQL results using Python
- Identify users with repeated failed login attempts

## Technologies Used

- PostgreSQL
- SQL
- Python 3
- Psycopg 3

## Project Structure

```text
postgres-security-lab/
│
├── README.md
├── schema.sql
├── seed.sql
├── investigation.sql
└── db_test.py
