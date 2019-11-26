from DAO.keyword import *
from DAO.user import *


class DefaultKeywordDAO():

    def __init__(self):
        self.db_conn = DBConnection()

    def select_keywords(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT word FROM DefaultKeywords"
            cursor.execute(sql)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            print(e)
