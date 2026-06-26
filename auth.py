import sqlite3

db = sqlite3.connect("users.db")

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)
    return result.fetchone()

def register(username, password):
    db.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
    db.commit()

def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id={user_id}"
    return db.execute(query).fetchone()

def delete_user(username):
    db.execute(f"DELETE FROM users WHERE username='{username}'")
    db.commit()
