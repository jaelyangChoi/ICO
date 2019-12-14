from DB.DAO.sqlExecution import *
from SQL.url import UrlSQL as SQL


class UrlDAO(SqlExecution):
    def select_index(self, url):
        return self.execute_sql_for_one_result(url, SQL.SELECT_INDEX)
