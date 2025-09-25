import sqlite3

# Database file
DB_FILE = 'parking_project.db'

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('employee', 'customer')) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    license_plate TEXT,
    state TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    username TEXT UNIQUE,
    password TEXT,
    position TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS violations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    employee_id INTEGER,
    violation_type TEXT,
    fine_amount REAL,
    make TEXT,
    model TEXT,
    color TEXT,
    license_plate TEXT,
    state TEXT,
    date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(employee_id) REFERENCES employees(id)
)
''')

# Add sample employees
cursor.execute("INSERT OR IGNORE INTO employees (name, username, password, position) VALUES (?, ?, ?, ?)",
               ("Angela", "Angela", "AT1001!!", "Enforcement"))
cursor.execute("INSERT OR IGNORE INTO employees (name, username, password, position) VALUES (?, ?, ?, ?)",
               ("Mike", "Mike", "MD1001!!", "Enforcement"))

conn.commit()
conn.close()

print("Database and tables created. Sample employees added.")
