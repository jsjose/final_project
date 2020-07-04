# DB manager. this module manages db connection, update and closing

import sqlite3

class testDB:
    def __init__(self):
        super().__init__()

        try:
            con = sqlite3.connect(':memory:')
            print("Connection is established: Database is created in memory")
        except Error:
            print(Error)
        finally:
            con.close()