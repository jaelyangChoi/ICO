from db_connection import DBConnection
from DAO.index import *


class URL_DAO(Index):
    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = ""

    def select_url_index(self, url):
        self.sql = "SELECT _index FROM Articles WHERE URL = %s"
        return self.select_index(url)
