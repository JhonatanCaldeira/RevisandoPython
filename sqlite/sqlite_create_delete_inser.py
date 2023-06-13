import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FILE = 'db.sqlite3'
DB_PATH = ROOT_DIR / DB_FILE
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# SQLite não tem truncate

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# Criar Tabela
cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
               '('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')'
               )

connection.commit()

# Inserindo valores
# (name, weight) values (:nome, :peso) e passar um dicionário
cursor.executemany(
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?,?)', [
        ["Jhonatan", 80.9], ["Brizzida", 69.6], ["Eduardo", 70.4]]
)
connection.commit()

cursor.close()
connection.close()
