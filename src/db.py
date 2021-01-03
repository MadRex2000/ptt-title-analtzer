import sqlite3


class DB:
    def __init__(self, db_name='db.sqlite'):
        self.conn_db = sqlite3.connect(db_name)
        self.db = self.conn_db.cursor()

    def create(self):
        try:
            self.db.execute('''CREATE TABLE POST
                  (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  TITLE TEXT NOT NULL,
                  URL TEXT NOT NULL,
                  AUTHOR CHAR(50),
                  DATE CHAR(50),
                  PUSH INTEGER,
                  DATA TEXT
                  );
                  ''')

            self.conn_db.commit()
        except sqlite3.OperationalError:
            print('table already exists')

    def store(self, title, url, author, date, push, data):
        self.db.execute("""INSERT INTO POST (TITLE, URL, AUTHOR, DATE, PUSH, DATA) VALUES (?, ?, ?, ?, ?, ?)""", (title, url, author, date, push, str(data)))
        self.conn_db.commit()

    def get_all(self):
        cursor = self.db.execute("SELECT title, url, author, date, push, data from POST")
        return cursor

    def get_filter(self, word):
        cursor = self.db.execute("SELECT title, url, author, date, push, data from POST WHERE title LIKE %?%", (word,))
        return cursor

    def get(self, title):
        cursor = self.db.execute("SELECT title, url, author, date, push, data from POST WHERE title = ?", (title,))
        return cursor

    def get_id(self, title):
        cursor = self.db.execute("SELECT id from POST WHERE title = ?", (title,))
        return cursor

    def update(self, id, url, author, date, push):
        self.db.execute("UPDATE POST SET URL = ?, AUTHOR = ?, DATE = ?, PUSH = ? WHERE ID = ?", (url, author, date, push, id))
        self.conn_db.commit()
