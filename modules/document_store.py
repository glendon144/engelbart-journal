import sqlite3

class DocumentStore:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, title TEXT, body TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        self.conn.commit()
    # Add this method here clearly:
    def add_document(self, title, body):
        cur = self.conn.execute(
            "INSERT INTO documents (title, body) VALUES (?, ?)", 
            (title, body)
        )
        self.conn.commit()
        return cur.lastrowid

    def update_document(self, doc_id: int, new_body: str):
        """
        Replace the body of an existing document.
        """
        self.conn.execute(
        "UPDATE documents SET body = ? WHERE id = ?",
        (new_body, doc_id)
    )
        self.conn.commit()

    def get_document_index(self):
        cur = self.conn.execute("SELECT id, title, body FROM documents ORDER BY id DESC")
        result = []
        for row in cur.fetchall():
            description = (row['body'] or "")[:60].replace("\n", " ").replace("\r", " ")
            result.append({'id': row['id'], 'title': row['title'], 'description': description})
            print("DEBUG: get_document_index returns:", result)
        """
        Return[{'id': .., 'title': .., 'description': ..}, ...] -
        'description' is a 60-char preview for text docs,
        or "[12345 bytes]" for binary (images, PDFs, ...).
        """
        cur = self.conn.execute(
            "SELECT id, title, body FROM documents ORDER BY id DESC"
        )
        result = []
        for row in cur.fetchall():
            body = row["body"] or b""
            if isinstance(body , bytes):
                # binary file - show size placeholder
                desc = f"[{len(body)} bytes]"
            else:
                # text - first 60 chars, single-line
                desc = body[:60].replace("\n", " ").replace("\r", " ")
            result.append({"id": row["id"], "title": row["title"], "description": desc})
        return result

    def get_document(self, doc_id):
        cur = self.conn.execute("SELECT id, title, body FROM documents WHERE id=?", (doc_id,))
        return cur.fetchone()

    # ... (add your other methods as needed)
    # ------------------------------------------------------------------
    # Return a list of dicts:  [{'id': 1, 'title': '...'}, ...]
    # Used by LIST in CommandProcessor
    # ------------------------------------------------------------------
    def list_documents(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, title FROM documents ORDER BY id ASC")
        rows = cur.fetchall()
        return [{"id": row[0], "title": row[1]} for row in rows]

    # ... (add your other methods as needed)

    # ------------------------------------------------------------------
    # Create a new document and return its ID
    # ------------------------------------------------------------------
    def create_document(self, title: str, body: str):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO documents (title, body, created, last_modified) "
            "VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            (title, body),
        )
        self.conn.commit()
        return cur.lastrowid

    # ------------------------------------------------------------------
    # Replace body + update last_modified
    # ------------------------------------------------------------------
    def update_document(self, doc_id: int, new_body: str):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE documents "
            "SET body = ?, last_modified = CURRENT_TIMESTAMP "
            "WHERE id = ?",
            (new_body, doc_id),
        )
        self.conn.commit()

    
    # --------------------------------------------------------------
    # Replace all outbound links for a source doc
    # dst_ids  ── list[int]  e.g.  [2, 7, 9]
    # --------------------------------------------------------------
    def update_links(self, src_id: int, dst_ids: list[int]):
        cur = self.conn.cursor()
        # remove old links first
        cur.execute("DELETE FROM links WHERE src_id = ?", (src_id,))
        # insert new set (if any)
        cur.executemany(
            "INSERT INTO links (src_id, dst_id) VALUES (?, ?)",
            [(src_id, d) for d in dst_ids],
        )
        self.conn.commit()

    
    # --------------------------------------------------------------
    # Return list[int] of all dst_id values linked from src_id
    # --------------------------------------------------------------
    def get_links(self, src_id: int):
        cur = self.conn.cursor()
        cur.execute("SELECT dst_id FROM links WHERE src_id = ?", (src_id,))
        rows = cur.fetchall()
        return [row[0] for row in rows]

    def delete_document(self, doc_id: int):
        """Permanently delete a document and commit changes."""
        self.conn.execute(
            "DELETE FROM documents WHERE id = ?",
            (doc_id,)
        )
        self.conn.commit()
