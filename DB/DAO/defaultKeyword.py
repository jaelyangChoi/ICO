from DTO.defaultKeyword import *
from DAO.user import *
from SQL.defaultKeyword import SQL as sql


class DefaultKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_all(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(sql.SELECT_ALL)

            data = []
            for result in cursor.fetchall():
                default_keyword = DefaultKeyword()
                default_keyword.set_all(result)
                data.append(default_keyword)

            self.db_conn.close_db()
            return data

        except Exception as e:
            return e

    def select_keywords(self):
        return self.execute_sql_for_one_component_list(sql.SELECT_KEYWORDS)

    def select_split_keywords(self):
        return self.execute_sql_for_one_component_list(sql.SELECT_SPLIT_KEYWORDS)

    def execute_sql_for_one_component_list(self, query):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(query)

            keywords = []
            for result in cursor.fetchall():
                keywords.append(result[0])

            self.db_conn.close_db()
            return keywords

        except Exception as e:
            return e
