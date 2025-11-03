import sqlite3

_connection = sqlite3.connect("data.db")
_connection.row_factory = sqlite3.Row

def create_table():
    _connection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, data TEXT)")
    
def commit_changes():
    _connection.commit()
    
def close_connection():
    _connection.close()

def add_entry(content, date):
    with _connection:
        _connection.execute("INSERT INTO entries VALUES (?,?)", (content, date))
    
    
def get_entries():
    cursor = _connection.execute("SELECT * FROM entries")
    return cursor