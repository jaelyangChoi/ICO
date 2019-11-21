from db_connection import *

class URL_DAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_index(self, url):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT _index FROM Articles WHERE URL = %s"
            cursor.execute(sql, url)

            result = cursor.fetchone()
            self.db_conn.close_db()
            return result[0]

        except Exception as e:
            print(e)