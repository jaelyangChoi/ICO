from DAO.user import *


class KeywordDAO:
    # db_conn = None

    def __init__(self):
        self.db_conn = DBConnection()

    def select_default_keywords(self):
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

    def insert_personal_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            user_dao = UserDAO()

            sql = "INSERT INTO PersonalKeywords(keyword, user) VALUES(%s, %s)"
            cursor.execute(sql, (keyword, user_dao.select_index(id)))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            print(e)

    def select_personal_keywords_by_user(self, id):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = """SELECT keyword FROM PersonalKeywords, Users
                    WHERE PersonalKeywords.user = Users._index
                    AND Users.id = %s"""
            cursor.execute(sql, id)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            print(e)

    def delete_personal_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            user_dao = UserDAO()

            sql = """DELETE FROM PersonalKeywords
                    WHERE keyword = %s AND user = %s"""
            cursor.execute(sql, (keyword, user_dao.select_index(id)))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            print(e)
