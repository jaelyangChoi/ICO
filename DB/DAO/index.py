from db_connection import *


class Index:

    def select_index(self, input):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(self.sql, input)

            result = cursor.fetchone()
            self.db_conn.close_db()
            return result[0]

        except Exception as e:
            print(e)