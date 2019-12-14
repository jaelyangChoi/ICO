from DAO.user import *
from DTO.defaultKeyword import *
from SQL.defaultKeyword import DefaultKeywordSQL as SQL


class DefaultKeywordDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def select_all(self):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()
            cursor.execute(SQL.SELECT_ALL)

            data_list = []
            for result in cursor.fetchall():
                default_keyword = DefaultKeyword()
                default_keyword.set_all(result)
                data_list.append(default_keyword)

            self.db_conn.close_db()
            return data_list

        except Exception as e:
            print(e)
            return e

    def select_keywords(self):
        return self.execute_sql_for_one_component_list(SQL.SELECT_KEYWORDS)

    def select_split_keywords(self):
        return self.execute_sql_for_one_component_list(SQL.SELECT_SPLIT_KEYWORDS)
