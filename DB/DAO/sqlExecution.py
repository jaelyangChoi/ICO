from db_connection import *


class SqlExecution:
    def __init__(self):
        self.db_conn = DBConnection()

    def execute_sql_for_one_result(self, input, sql):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(sql, input)

            result = cursor.fetchone()
            self.db_conn.close_db()

            return result

        except Exception as e:
            return e

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
            print(e)
            return e
