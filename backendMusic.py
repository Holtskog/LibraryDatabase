'''
    File name: backendMusic.py
    Author: Øyvind Holtskog
    Email: oholtskog@hotmail.com
    Copyright: Copyright 2018, Øyvind Holtskog
    Date created: 3/20/2018
    Date last modified: 4/25/2018
    Python Version: 3.6.4
'''

import psycopg2

class MusicDatabase:
    def __init__(self, db):
        """ This method initializes the database server """
        self.db = db
        self.connection = psycopg2.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, year TEXT, producer TEXT)")
        self.connection.commit()

    def view(self):
        """ This method returns a list of all the books in the databse """
        self.cursor.execute("SELECT * FROM music")
        rows = self.cursor.fetchall()
        return rows

    def get_index(self):
        """ This method makes sure returns the next index in the database """
        self.cursor.execute("SELECT * FROM music")
        rows = self.cursor.fetchall()
        return (len(rows) + 1)

    def insert(self, title, artist, year, producer):
        """ This method inserts the string variables received from music into the database """
        index = self.get_index()
        self.cursor.execute("INSERT INTO music VALUES (%s, %s, %s, %s, %s)",\
                            (index, title.title(), artist.title(), year, producer.title()))
        self.connection.commit()

    def delete(self, id):
        """ This method allows you to delete an item in the database given the selected index """
        self.cursor.execute("DELETE FROM music WHERE id=%s", (id,))
        self.connection.commit()

    def update(self, id, title, artist, year, producer):
        """ This method allows you to update an item in the database given the parameters above """
        self.cursor.execute("UPDATE music SET title=%s, artist=%s, year=%s, producer=%s WHERE id=%s",\
                            (title.title(), artist.title(), year, producer.title(), id))
        self.connection.commit()

    def search(self, title="", artist="", year="", producer=""):
        """
        This method allows you to search fro anythin in the database.
        It allows you to search fro a single character or single name etc.
        As long as you search for something - even a space - it will return whatever contains that
        """
        if str(title) is not "":
            titles = []
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT title FROM music")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if title.title() in item[0]:
                    new_title = item[0]
                    titles.append(new_title)
            rows = []
            for names in titles:
                self.cursor.execute("SELECT * FROM music WHERE title=%s", (names,))
                row = self.cursor.fetchall()
                rows.append(row)
            return rows
        elif str(artist) is not "":
            artists = ["hello"]
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT artist FROM music")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if str(artist).title() in item[0]:
                    new_artist = item[0]
                    if artists[0] in "hello":
                        artists[0] = new_artist
                    elif new_artist not in artists:
                        artists.append(new_artist)
            con.close()                
            rows = []
            for name in artists:
                self.cursor.execute("SELECT * FROM music WHERE artist=%s", (name,))
                row = self.cursor.fetchall()
                rows.append(row)
            if len(rows) == 2:
                return rows[0]+rows[1]
            elif len(rows) == 1:
                return rows[0]
            elif len(rows) > 2:
                for row in rows:
                    rows[0] = rows[0] + row
                return rows[0]      
        elif str(producer) is not "" and str(producer) is not " ":
            producers = ["hello"]
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT producer FROM videos")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if str(producer).title() in item[0]:
                    new_producer = item[0]
                    if producers[0] in "hello":
                        producers[0] = new_producer
                    elif new_producer not in producers:
                        producers.append(new_producer)                  
            rows = []
            for name in producers:
                self.cursor.execute("SELECT * FROM videos WHERE producer=%s", (name,))
                row = self.cursor.fetchall()
                rows.append(row)
            if len(rows) == 2:
                return rows[0]+rows[1]
            elif len(rows) == 1:
                return rows[0]
            elif len(rows) > 2:
                for row in rows:
                    rows[0] = rows[0] + row
                return rows[0]
        else:
            self.cursor.execute("SELECT * FROM music WHERE title=%s OR artist=%s OR year=%s OR producer=%s", (title.title(), artist.title(), year, producer))
            rows = self.cursor.fetchall()
            return rows

    def __del__(self):
        """ This method makes sure you disconnect from the database server """
        self.connection.close()