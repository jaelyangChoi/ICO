from DTO.defaultKeyword import *
from DAO.user import *
from SQL.comment import *


class DefaultKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_all(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.SELECT_ALL_FROM_DEFAULT_KEYWORD)

            keywords = []
            for result in cursor.fetchall():
                default_keyword = DefaultKeyword()
                default_keyword.set_all(result)
                keywords.append(default_keyword)

            self.db_conn.close_db()
            return keywords

        except Exception as e:
            return e

    def select_keywords(self):
        return self.execute_sql_for_one_component_list(SQL.SELECT_KEYWORD_FROM_DEFAULT_KEYWORD)

    def select_split_keywords(self):
        return self.execute_sql_for_one_component_list(SQL.SELECT_SPLIT_KEYWORD_FROM_DEFAULT_KEYWORD)

    def execute_sql_for_one_component_list(self, sql):
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
            return e
