from DAO.user import *
from SQL.personalKeyword import PersonalKeywordSQL as SQL


class PersonalKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = ""

    def select_keywords(self, id):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.SELECT, id)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            return e

    def insert_keyword(self, id, keyword):
        self.sql = SQL.INSERT
        self.control_keyword(id, keyword)

    def delete_keyword(self, id, keyword):
        self.sql = SQL.DELETE
        self.control_keyword(id, keyword)

    def control_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            user_dao = UserDAO()

            cursor.execute(self.sql, (keyword, user_dao.select_index(id)))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            return e