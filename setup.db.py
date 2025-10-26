import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    category TEXT
)
""")
conn.commit()
conn.close()
print("Database initialized.")