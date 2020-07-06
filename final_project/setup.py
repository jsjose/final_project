# Initialize DB.

import sys
import os
import sqlite3

from sqlite3 import Error

from libs.test_db import testDB 

def run_project(args):
    '''
    Create DB, create tables
    '''
    dbName = '.\\data\\testdb.db'
    #dbName = ''
    mydb = testDB(dbName)

    cursorObj = mydb.conn.cursor()
    
    #cursorObj.execute("CREATE TABLE url(id integer PRIMARY KEY, path text, status_code int, urlTested text, position text, headers text)")
    cursorObj.execute("CREATE TABLE url(datetime text, path text, status_code int, urlTested text, headers blob)")

    mydb.conn.commit()

    mydb.close()

if __name__ == '__main__':
    #print(os.getcwd())
    print('Setup of final project for course Complete Python Bootcamp')
    run_project(sys.argv)