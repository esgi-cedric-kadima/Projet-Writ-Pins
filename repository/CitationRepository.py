import json

from repository.DBRepository import DBRepository
from fastapi import HTTPException


class CitationRepository(DBRepository):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS citation 
                        (id INTEGER PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL, source TEXT NOT NULL, preference int, tags JSON, id_utilisateur int NOT NULL, FOREIGN KEY (id_utilisateur) REFERENCES User(id))""")
        self.conn.commit()

    def create_citation(self, item_dict):
        self.conn.execute(
            "INSERT INTO citation (title, content, source, preference, tags, id_utilisateur) VALUES (?, ?, ?, ?, ?, ?)",
            (item_dict['title'], item_dict['content'], item_dict['source'], item_dict['preference'], json.dumps(item_dict['tags']),
             item_dict['id_utilisateur']))
        item_id = self.cursor.lastrowid
        self.conn.commit()
        return item_id

    def list_citations(self):
        self.cursor.execute("SELECT * FROM citation")
        citations = self.cursor.fetchall()
        return citations

    def get_citation(self, citation_id):
        self.cursor.execute("SELECT * FROM citation WHERE id=?", (citation_id,))
        citation = self.cursor.fetchone()
        return citation

    def update_citation(self, citation_id, item_dict):
        self.cursor.execute("SELECT * FROM citation WHERE id=?", (citation_id,))
        existing_citation = self.cursor.fetchone()
        if not existing_citation:
            return HTTPException(status_code=404, detail="Item not found")
        self.cursor.execute(
            "UPDATE citation SET title=?, content=?, source=?, preference=?, tags=?, id_utilisateur=? WHERE id=?", (
                item_dict['title'], item_dict['content'], item_dict['source'], item_dict['preference'],
                item_dict['tags'],
                item_dict['id_utilisateur'], citation_id))
        self.conn.commit()
        return citation_id

    def delete_citation(self, citation_id):
        self.cursor.execute("SELECT * FROM citation WHERE id=?", (citation_id,))
        existing_citation = self.cursor.fetchone()
        if not existing_citation:
            return HTTPException(status_code=404, detail="Item not found")
        self.cursor.execute("DELETE FROM citation WHERE id=?", (citation_id,))
        self.conn.commit()
        return citation_id
