from DAO.index import *
from SQL.url import SQL as sql


class UrlDAO(Index):
    def select_index(self, url):
        return self.execute_sql_for_one_result(url, sql.SELECT)
