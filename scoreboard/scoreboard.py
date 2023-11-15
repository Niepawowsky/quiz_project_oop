import sqlite3
from pathlib import Path

class Scoreboard:
    def __init__(self, score_record):
        self.scoreboard_init()
        self.score_record = score_record
        self.add_record()


    def scoreboard_init(self):
        source = Path(__file__).resolve().parent
        db_path = source / "scoreboard.db"

        with sqlite3.connect(db_path) as database:
            cursor = database.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS scoreboard(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            score INTEGER,
                            date TEXT)''')


    def scoreboard_connection(self):
        source = Path(__file__).resolve().parent
        db_path = source / "scoreboard.db"

        with sqlite3.connect(db_path) as database:
            self.cursor = database.cursor()
            return self.cursor


    def add_record(self):
        sql = 'INSERT INTO scoreboard VALUES(null, ?, ?, ?)'
        cursor = self.scoreboard_connection()
        cursor.execute(sql,(self.score_record['name'],self.score_record['score'], self.score_record['time']))
        cursor.connection.commit()


class Scoreboard_viewer:
    def __init__(self):
        self.view_scoreboard()

    def view_scoreboard(self):
        source = Path(__file__).resolve().parent
        db_path = source / "scoreboard.db"

        with sqlite3.connect(db_path) as database:
            cursor = database.cursor()
            cursor.execute('''SELECT name, score, date FROM scoreboard ORDER BY score DESC''')
            result = cursor.fetchall()

            print("Name\tScore\tDate")
            print("-----------------------")
            for row in result:
                print("\t".join(map(str, row)))


