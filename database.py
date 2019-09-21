#!/usr/bin/env python3

import mysql.connector
from config import host,user,password

mydb = mysql.connector.connect(
  host=host,
  user=user,
  passwd=password,
)

mycursor = mydb.cursor()

class manageDB:
    def createDB (self, name):
        mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(name))

    def createTB (self,database, name):
        mycursor.execute("USE {}".format(database))
        mycursor.execute("CREATE TABLE IF NOT EXISTS {} (links VARCHAR(255))".format(name))

    def insertTB (self, database, table, html_links):
        mycursor.execute("USE {}".format(database))
        sqlFormula = "INSERT INTO {} (links) VALUES ('{}')".format(table, html_links)
        mycursor.execute(sqlFormula, html_links)
        mydb.commit()

if __name__ == "__main__":
    manageDB = manageDB()
    manageDB.createDB('xyz')
    manageDB.createTB('xyz', 'movies')
    manageDB.insertTB('xyz', 'movies', 'nathanielam0ah@github.com')
