from DAO.user import *


class DefaultKeywordDAO:

    def __init__(self):
        self.db_conn = DBConnection()

    def select_keywords(self):
        return self.execute_sql_for_list("""SELECT keyword
                                            FROM DefaultKeywords""")

    def select_split_keywords(self):
        return self.execute_sql_for_list("""SELECT splited_keyword
                                            FROM DefaultKeywords""")

    def execute_sql_for_list(self, sql):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(sql)

            keyword_list = []
            for result in cursor.fetchall():
                keyword_list.append(result[0])

            self.db_conn.close_db()
            return keyword_list

        except Exception as e:
            return -1
