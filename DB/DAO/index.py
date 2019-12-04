from abc import *
from db_connection import *


class Index:

    def __init__(self):
        self.db_conn = DBConnection()

    @abstractmethod
    def select_index(self, url):
        pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

    def execute_sql_for_one_result(self, input, sql):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(sql, input)

            result = cursor.fetchone()
            self.db_conn.close_db()

            return result

        except Exception as e:
            print(e)
            return -1
