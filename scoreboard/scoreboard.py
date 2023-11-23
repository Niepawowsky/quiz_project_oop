'''
Module that takes data from quiz return
'''

import sqlite3
from pathlib import Path


class Scoreboard:
    '''
    Class Scoreboard conects to database (or create it if not exists),
    connects to database,
    saves name score and date of a played game,


    '''
    def __init__(self, score_record):
        self.scoreboard_init()
        self.score_record = score_record
        self.add_record()

    def scoreboard_init(self):

        """
        The scoreboard_init function creates a database called scoreboard.db
        if it does not already exist.
        It also creates a table in the database called scoreboard,
        which contains four columns: id, name, score and date.

        :param self: Represent the instance of the class
        :return: The database path
        :doc-author: Trelent
        """
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

        """
        The scoreboard_connection function creates a connection to
        the scoreboard.db database and returns a cursor object.

        :param self: Access the attributes and methods of a class
        :return: A cursor object
        :doc-author: Trelent
        """
        source = Path(__file__).resolve().parent
        db_path = source / "scoreboard.db"

        with sqlite3.connect(db_path) as database:
            cursor = database.cursor()
            return cursor

    def add_record(self):

        """
        The add_record function takes the score_record dictionary
        and adds it to the scoreboard database.
        The function first creates a cursor object,
        then executes an SQL statement that inserts a new record into
        the scoreboard table. The values for this new record are taken
        from the score_record dictionary.

        :param self: Access the attributes and methods of the class
        :return: Nothing
        :doc-author: Trelent
        """
        sql = 'INSERT INTO scoreboard VALUES(null, ?, ?, ?)'
        cursor = self.scoreboard_connection()
        cursor.execute(sql, (self.score_record['name'],
                             self.score_record['score'],
                             self.score_record['time']))
        cursor.connection.commit()


class ScoreboardViewer:
    '''
    Just for experimental usage - creted separate class just to know
    how class mixing works
    '''

    def __init__(self):
        self.view_scoreboard()

    def view_scoreboard(self):

        """
        The view_scoreboard function prints the scoreboard.db database
        to the console in a readable format.

        :param self: Represent the instance of the class
        :return: The scoreboard
        :doc-author: Trelent
        """
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
