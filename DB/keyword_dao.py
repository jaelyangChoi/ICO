from user_dao import *

class KeywordDAO:
    # db_conn = None

    def __init__(self):
        self.db_conn = DBConnection()

    def select_default_keywords(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = """SELECT word FROM DefaultKeywords"""
            cursor.execute(sql)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            return keyword_list

        except Exception as e:
            print(e)

    def insert_personal_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            """sql = "SELECT _index From User WHERE id = %s"
            cursor.execute(sql, id)

            result = cursor.fetchone()
            user_index = result[0]"""
            user_dao = UserDAO()

            sql = """INSERT INTO PersonalKeywords(keyword, user) VALUES(%s, %s)"""
            cursor.execute(sql, (keyword, user_dao.select_index(id)))
            conn.commit()

        except Exception as e:
            print(e)

    def select_personal_keywords_by_user(self, id):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = """SELECT keyword FROM PersonalKeywords, User
                    WHERE PersonalKeywords.user = User._index
                    AND User.id = %s"""
            cursor.execute(sql, id)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            return keyword_list

        except Exception as e:
            print(e)

    def delete_personal_keyword(self, id, keyword):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            """sql = "SELECT _index FROM User WHERE id=%s"
            cursor.execute(sql, id)

            result = cursor.fetchone()
            user_index = result[0]"""
            user_dao = UserDAO()

            sql = """DELETE FROM PersonalKeywords
                    WHERE user=%s AND keyword=%s"""
            cursor.execute(sql, (user_dao.select_index(id), keyword))
            conn.commit()

        except Exception as e:
            print(e)