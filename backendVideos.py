'''
    File name: backendVideos.py
    Author: Øyvind Holtskog
    Date created: 3/20/2018
    Date last modified: 4/25/2018
    Python Version: 3.6.4
'''

import psycopg2

class VideoDatabase:
    def __init__(self, db):
        self.db = db
        self.connection = psycopg2.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, title TEXT, producer TEXT, year TEXT, director TEXT)")
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM videos")
        rows = self.cursor.fetchall()
        return rows

    def get_index(self):
        self.cursor.execute("SELECT * FROM videos")
        rows = self.cursor.fetchall()
        return (len(rows) + 1)

    def insert(self,title, producer, year, director):
        index = self.get_index()
        self.cursor.execute("INSERT INTO videos VALUES (%s, %s, %s, %s, %s)",\
                            (index, title.title(), producer.title(), year, director.title()))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM videos WHERE id=%s", (id,))
        self.connection.commit()

    def update(self, id, title, producer, year, director):
        self.cursor.execute("UPDATE videos SET title=%s, producer=%s, year=%s, director=%s WHERE id=%s", (title.title(), producer.title(), year, director, id))
        self.connection.commit()

    def search(self, title="", producer="", year="", director=""):
        if str(title) is not "":
            titles = []
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT title FROM videos")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if title.title() in item[0]:
                    new_title = item[0]
                    titles.append(new_title)
            rows = []
            for names in titles:
                self.cursor.execute("SELECT * FROM videos WHERE title=%s", (names,))
                row = self.cursor.fetchall()
                rows.append(row)
            return rows
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
        elif str(director) is not "" and str(director) is not " ":
            directors = ["hello"]
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT director FROM videos")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if str(director).title() in item[0]:
                    new_director = item[0]
                    if directors[0] in "hello":
                        directors[0] = new_director
                    elif new_director not in directors:
                        directors.append(new_director)                  
            rows = []
            for name in directors:
                self.cursor.execute("SELECT * FROM videos WHERE director=%s", (name,))
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
            self.cursor.execute("SELECT * FROM videos WHERE title=%s OR producer=%s OR year=%s OR director=%s", (title.title(), producer.title(), year, director))
            rows = self.cursor.fetchall()
            return rows

    def __del__(self):
        self.connection.close()