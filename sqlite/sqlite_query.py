import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = 'db.sqlite3'
DB_PATH = ROOT_DIR / DB_FILE
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for row in cursor.fetchall():
    _id, name, weight = row
    print(name, weight)

cursor.close()
connection.close()
