from db_connection import *
from DAO.index import *


class UserDAO(Index):
    def __init__(self):
        self.db_conn = DBConnection()
        self.sql = ""

    def select_user_index(self, user):
        self.sql = "SELECT _index FROM User WHERE id = %s"
        return self.select_index(user)
