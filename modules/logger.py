
import sqlite3
from datetime import datetime

class EventLogger:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._initialize_table()

    def _initialize_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS event_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                user TEXT,
                action TEXT,
                target TEXT,
                details TEXT
            )
        ''')
        self.conn.commit()

    def log(self, user, action, target, details=""):
        timestamp = datetime.now().isoformat()
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO event_log (timestamp, user, action, target, details)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, user, action, target, details))
        self.conn.commit()

    def close(self):
        self.conn.close()
