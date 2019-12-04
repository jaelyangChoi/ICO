from DAO.user import *


class PersonalKeywordDAO:

    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = ""

    def select_keywords(self, id):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = """SELECT keyword FROM PersonalKeyword, User
                     WHERE PersonalKeyword.user = User._index
                     AND User.id = %s"""
            cursor.execute(sql, id)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            return -1

    def insert_keyword(self, id, keyword):
        self.sql = "INSERT INTO PersonalKeyword(keyword, user) VALUES(%s, %s)"
        self.control_keyword(id, keyword)

    def delete_keyword(self, id, keyword):
        self.sql = """DELETE FROM PersonalKeyword
                      WHERE keyword = %s AND user = %s"""
        self.control_keyword(id, keyword)

    def control_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            user_dao = UserDAO()

            user_index = user_dao.select_index(id)
            cursor.execute(self.sql, (keyword, user_index))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            print(e)
