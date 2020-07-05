# DB manager. this module manages db connection, update and closing

import sqlite3
from sqlite3 import Error

class testDB:
    def __init__(self, dbName=':memory'):
        super().__init__()

        try:
            print(dbName)
            self.conn = sqlite3.connect(dbName)
            print("Connection is established: Database is created in "+dbName)
        except Error:
            print(Error)
        #finally:
        #    self.con.close()

    def close(self):
        self.conn.close()