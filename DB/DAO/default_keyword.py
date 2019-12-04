from DAO.user import *
from DTO.defaultKeyword import DefaultKeyword


class DefaultKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_all(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT _index, keyword, split_keyword FROM DefaultKeywords"
            cursor.execute(sql)

            devide_keyword_list = []
            for index, keyword, split_keyword in cursor.fetchall():
                default_keyword = DefaultKeyword(index, keyword, split_keyword)
                devide_keyword_list.append(default_keyword)
            self.db_conn.close_db()

            return devide_keyword_list

        except Exception as e:
            return -1

    def select_split_keywords(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT splited_keyword FROM DefaultKeywords"
            cursor.execute(sql)

            devide_keyword_list = []
            for result in cursor.fetchall():
                devide_keyword_list.append(result)
            self.db_conn.close_db()

            return devide_keyword_list

        except Exception as e:
            return -1

    def select_keywords(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT keyword FROM DefaultKeywords"
            cursor.execute(sql)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result)

            self.db_conn.close_db()

            return keyword_list

        except Exception as e:
            return -1
