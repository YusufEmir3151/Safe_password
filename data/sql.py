import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS secret(
    info TEXT,
    ad TEXT,
    password TEXT
)""")

conn.commit()

def add_password(inf, user, password_red):
    c.execute("INSERT INTO secret VALUES (?, ?, ?)", (inf, user, password_red))
    conn.commit()

def delete_password(inf):
    c.execute("DELETE FROM secret WHERE info = ?", (inf,))
    conn.commit()

def display_passwords():
    c.execute("SELECT * FROM secret")
    results = c.fetchall()
    for row in results:
        print(row)

def change_password(inf, new_password_red):
    c.execute("UPDATE secret SET password = ? WHERE info = ?", (new_password_red, inf))
    conn.commit()
