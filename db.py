# db.py
import sqlite3
from pathlib import Path

DB_FILE = Path("links.db")

# Cria o banco se não existir
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id TEXT PRIMARY KEY,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Salva um link novo
def salvar_link(id, original_url):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO links (id, original_url) VALUES (?, ?)", (id, original_url))
    conn.commit()
    conn.close()

# Busca um link pelo ID
def buscar_link(id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT original_url FROM links WHERE id = ?", (id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
