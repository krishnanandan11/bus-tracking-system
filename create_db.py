import sqlite3

conn = sqlite3.connect("bus.db")
cur = conn.cursor()

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

# Location table
cur.execute("""
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bus_id INTEGER,
    latitude REAL,
    longitude REAL
)
""")

# Insert sample users
cur.execute("INSERT INTO users (username, password, role) VALUES ('student1','123','student')")
cur.execute("INSERT INTO users (username, password, role) VALUES ('driver1','123','driver')")

conn.commit()
conn.close()

print("Database created successfully")