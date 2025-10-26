import sqlite3

def add_event(name, date):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (name, date) VALUES (?, ?)", (name, date))
    conn.commit()
    conn.close()
    print(f"Added event: {name} on {date}")

# Example usage
add_event("Owners Birthday(william)", "2025-12-05")