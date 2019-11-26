from DAO.index import *


class UrlDAO(Index):

    def select_index(self, url):
        return self.execute_sql_for_one_result(url,
                                               """SELECT _index
                                               FROM Articles
                                               WHERE URL = %s""")
