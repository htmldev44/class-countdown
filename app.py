from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_events():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, date, category FROM events")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        category = request.form.get("category", "General")
        conn = sqlite3.connect("events.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (name, date, category) VALUES (?, ?, ?)", (name, date, category))
        conn.commit()
        conn.close()
        return redirect("/")
    events = get_events()
    return render_template("index.html", events=events)

@app.route("/delete/<int:event_id>", methods=["POST"])
def delete_event(event_id):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)