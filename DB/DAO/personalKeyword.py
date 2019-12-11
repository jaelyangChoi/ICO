from DAO.user import *
from SQL.personalKeyword import PersonalKeywordSQL as SQL


class PersonalKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = ""

    def select_keywords(self, user_index):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.SELECT_KEYWORDS, user_index)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            print(e)
            return e

    def insert_keyword(self, user_index, keyword):
        self.sql = SQL.INSERT_KEYWORD
        self.control_keyword(user_index, keyword)

    def delete_keyword(self, user_index, keyword):
        self.sql = SQL.DELETE_KEYWORD
        self.control_keyword(user_index, keyword)

    def control_keyword(self, user_index, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(self.sql, (keyword, user_index))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            print(e)
            return e
