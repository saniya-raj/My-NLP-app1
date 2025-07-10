import json
import hashlib

USER_DB = 'users.json'

def load_users():
    try:
        with open(USER_DB, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DB, 'w') as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, password):
    users = load_users()
    if email in users:
        return False, "User already exists."
    users[email] = {"name": name, "password": hash_password(password)}
    save_users(users)
    return True, "Registration successful."

def login_user(email, password):
    users = load_users()
    if email in users and users[email]['password'] == hash_password(password):
        return True, users[email]['name']
    return False, "Invalid credentials."
