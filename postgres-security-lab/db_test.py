import psycopg
from collections import Counter

conn = psycopg.connect(
    "dbname=security_lab_test user=postgres password=PASSSWORD host=localhost")

cur = conn.cursor()


cur.execute(
    "SELECT users.username, login.status FROM login JOIN users ON users.id = login.user_id;")

rows = cur.fetchall()
f = []
for i in rows:
    if i[1] == "failed":
        f.append(i[0])
print("Suspicious users: ")
failed = Counter(f)
for i, j in failed.items():
    if j > 2:
        print(i, "-", j, "failed attempts")
cur.close()
conn.close()
