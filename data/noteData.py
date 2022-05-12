import sqlite3 as sl


class NoteData:
    id = None
    title = ""
    content = ""
    created = ""


class SQLiteManager:
    con = sl.connect('notes.db')

    # singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQLiteManager, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def toNoteData(self, row):
        note = NoteData()
        note.id = row[0]
        note.title = row[1]
        note.content = row[2]
        note.created = row[3]
        return note

    def getNotesList(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        notes = []
        for row in rows:
            notes.append(self.toNoteData(row))

        return notes

    def updateNote(self, note):
        cursor = self.con.cursor()
        cursor.execute("UPDATE notes SET title = ?, content = ?, created = datetime() WHERE id = ?",
                       (note.title, note.content, note.id))
        self.con.commit()

    def addNote(self, note):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO notes (title, content, created) VALUES (?, ?, datetime())",
                       (note.title, note.content))
        self.con.commit()
        # get the id of the new note
        cursor.execute("SELECT last_insert_rowid()")
        row = cursor.fetchone()
        note.id = row[0]

    def deleteNote(self, note):
        cursor = self.con.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note.id,))
        self.con.commit()
