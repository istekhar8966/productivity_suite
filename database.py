#!/usr/bin/env python
# Manages the SQLite database connection and initial table setup.

import sqlite3

def create_connection():
    """Creates and returns a connection to the SQLite database."""
    try:
        # The database file will be created in the same directory as the script.
        conn = sqlite3.connect('productivity.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_tables(conn):
    """Ensures the necessary tables (todos, notes) exist in the database."""
    try:
        c = conn.cursor()
        # The `todos` table stores task information.
        c.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        # The `notes` table stores simple text notes.
        c.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")