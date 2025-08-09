# Script: WIP

import getpass
import hashlib
import sqlite3
from sqlite3 import Error

DB_FILE = "user.db"

# Create a connexion to the SQLite db

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# create a table of users

def create_table():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL
                )
            ''')
            conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()


# Variables

password = None

def password_set():
    while True:
        global password
        password = getpass.getpass("Set a password: ")
        first_check = getpass.getpass("Please confirm your password: ")

        if first_check == password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("Password set")
            return hashed_password        
        else:
            print("Passwords don't match")


# Check if user exists

def user_exists (username):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
            exists = cursor.fetchone() is not None
            conn.close()
            return exists
        except Error as e:
            print(f"Error checking user: {e}")
            conn.close()
    return False

# Register a user

def save_user(username, password_hash):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, password_hash))
            conn.commit()
            print(f"\nUser {username} registered successfully")
        except Error as e:
            print(f"Error saving user: {e}")
        finally:
            conn.close()

# Verify the users password

def verify_user(username, password):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()
            if result:
                stored_hash = result[0]
                return hashlib.sha256(password.encode()).hexdigest() == stored_hash
            return False
        except Error as e:
            print(f"Error verifiyng user: {e}")
            conn.close()
    return False

# Initiate the database

create_table()

# REgister a new user

name = input("Enter your username: ")

if user_exists(name):
    print("Username already exists")
else:
    hashed_password = password_set()
    save_user(name, hashed_password)

# Check password

check = getpass.getpass("Please enter your password: ")
if verify_user(name, check):
    print(f"\nWelcome {name}\tAccess granted")
else:
    print("\nWrong password")    
