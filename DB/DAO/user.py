from db_connection import *
from DAO.index import *

class UserDAO(Index):
    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = "SELECT _index FROM User WHERE id = %s"

"""
    def select_index(self, writer):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT _index FROM User WHERE id = %s"
            cursor.execute(sql, writer)

            result = cursor.fetchone()
            self.db_conn.close_db()
            return result[0]

        except Exception as e:
            print(e)
"""