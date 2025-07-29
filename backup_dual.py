
import os
import sqlite3
from datetime import datetime

# Canonical filenames considered part of the official system
CANONICAL_FILES = {
    'main.py', 'commands.py', 'command_processor.py',
    'gui_tkinter.py', 'image_generator.py', 'ai_interface.py',
    'document_store.py', 'hypertext_parser.py'
}

# Paths
ROOT_DIR = os.getcwd()
MODULES_DIR = os.path.join(ROOT_DIR, 'modules')
CANONICAL_DB = os.path.join(ROOT_DIR, 'storage', 'code_backups.db')
VARIANTS_DB = os.path.join(ROOT_DIR, 'storage', 'developervariants.db')

# Timestamp for entries
timestamp = datetime.utcnow().isoformat()

def ensure_db_schema(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS backups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT,
                    timestamp TEXT,
                    content TEXT
                )''')
    conn.commit()
    conn.close()

def save_to_db(db_path, filename, timestamp, content):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO backups (filename, timestamp, content) VALUES (?, ?, ?)", 
              (filename, timestamp, content))
    conn.commit()
    conn.close()

def run_backup():
    print(f"Scanning directory: {ROOT_DIR}\n")
    ensure_db_schema(CANONICAL_DB)
    ensure_db_schema(VARIANTS_DB)
    files = [f for f in os.listdir(ROOT_DIR) if f.endswith('.py')]

    for file in files:
        file_path = os.path.join(ROOT_DIR, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            db_path = CANONICAL_DB if file in CANONICAL_FILES else VARIANTS_DB
            save_to_db(db_path, file, timestamp, content)
            print(f"Backed up: {file} -> {'canonical' if db_path == CANONICAL_DB else 'variant'}")
        except Exception as e:
            print(f"Failed to read {file}: {e}")

    print("\nBackup complete.")

if __name__ == '__main__':
    run_backup()
