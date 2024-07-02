from pathlib import Path
import sqlite3

ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / 'banco.db'


def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            data_nascimento TEXT,
                            cpf TEXT UNIQUE,
                            endereco TEXT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            numero INTEGER,
                            agencia TEXT,
                            cliente_id INTEGER,
                            saldo REAL,
                            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT,
                            valor REAL,
                            data TEXT,
                            conta_id INTEGER,
                            FOREIGN KEY (conta_id) REFERENCES contas (id)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            data_hora TEXT,
                            acao TEXT,
                            detalhes TEXT
                          )''')
    conn.close()

create_tables()
