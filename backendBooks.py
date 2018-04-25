'''
    File name: backendBooks.py
    Author: Øyvind Holtskog
    Email: oholtskog@hotmail.com
    Copyright: Copyright 2018, Øyvind Holtskog
    Date created: 3/20/2018
    Date last modified: 4/25/2018
    Python Version: 3.6.4
'''

import psycopg2

class BookDatabase:
    """ This class is the backend behavior of books """
    def __init__(self, db):
        """ This method initializes the database server """
        self.db = db
        self.connection = psycopg2.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.connection.commit()

    def view(self):
        """ This method returns a list of all the books in the databse """
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def get_index(self):
        """ This method makes sure returns the next index in the database """
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return (len(rows) + 1)

    def insert(self,title, author, year, isbn):
        """ This method inserts the string variables received from books into the database """
        index = self.get_index()
        self.cursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s, %s)",\
                            (index, title.title(), author.title(), year, isbn))
        self.connection.commit()

    def delete(self, id):
        """ This method allows you to delete an item in the database given the selected index """
        self.cursor.execute("DELETE FROM books WHERE id=%s", (id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        """ This method allows you to update an item in the database given the parameters above """
        self.cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title.title(), author.title(), year, isbn, id))
        self.connection.commit()

    def search(self, title="", author="", year="", isbn=""):
        """
        This method allows you to search fro anythin in the database.
        It allows you to search fro a single character or single name etc.
        As long as you search for something - even a space - it will return whatever contains that
        """
        if str(title) is not "":
            titles = []
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT title FROM books")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if title.title() in item[0]:
                    new_title = item[0]
                    titles.append(new_title)
            con.close()
            rows = []
            for names in titles:
                self.cursor.execute("SELECT * FROM books WHERE title=%s", (names,))
                row = self.cursor.fetchall()
                rows.append(row)
            return rows
        elif str(author) is not "":
            authors = ["hello"]
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT author FROM books")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if str(author).title() in item[0]:
                    new_author = item[0]
                    if authors[0] in "hello":
                        authors[0] = new_author
                    elif new_author not in authors:
                        authors.append(new_author) 
            con.close()                 
            rows = []
            for name in authors:
                self.cursor.execute("SELECT * FROM books WHERE author=%s", (name,))
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
        elif str(isbn) is not "":
            isbns = []
            con = psycopg2.connect(self.db)
            cur = con.cursor()
            cur.execute("SELECT isbn FROM books")
            element = cur.fetchall()
            for item in element:
                item = list(item)
                if isbn in item[0]:
                    new_isbn = item[0]
                    isbns.append(new_isbn)
            con.close()
            rows = []
            for number in isbns:
                self.cursor.execute("SELECT * FROM library WHERE isbn=%s", (number,))
                row = self.cursor.fetchall()
                rows.append(row)
            return rows
        else:
            self.cursor.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title.title(), author.title(), year, isbn))
            rows = self.cursor.fetchall()
            return rows

    def __del__(self):
        """ This method makes sure you disconnect from the database server """
        self.connection.close()