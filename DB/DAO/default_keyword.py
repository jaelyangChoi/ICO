from DAO.user import *
from DTO.defaultKeyword import *


class DefaultKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_all(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = "SELECT * FROM DefaultKeyword"
            cursor.execute(sql)

            keyword_list = []
            for result in cursor.fetchall():
                default_keyword = DefaultKeyword()
                default_keyword.set_all(result)
                keyword_list.append(default_keyword)

            self.db_conn.close_db()
            return keyword_list

        except Exception as e:
            return -1

    def select_keywords(self):
<<<<<<< HEAD
        return self.execute_sql_for_one_component_list("""SELECT keyword
                                            FROM DefaultKeyword""")

    def select_split_keywords(self):
        return self.execute_sql_for_one_component_list("""SELECT splited_keyword
                                            FROM DefaultKeyword""")

    def execute_sql_for_one_component_list(self, sql):
=======
        return self.execute_sql_for_list("""SELECT keyword
                                            FROM DefaultKeyword""")

    def select_split_keywords(self):
        return self.execute_sql_for_list("""SELECT splited_keyword
                                            FROM DefaultKeyword""")

    def execute_sql_for_list(self, sql):
>>>>>>> fd41c3694998fd2a9f4b8a15e41187d503de3691
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
