from DAO.index import *


class UserDAO(Index):

    def select_index(self, user):
        return self.execute_sql_for_one_result(user,
                                               """SELECT _index
                                               FROM User
                                               WHERE id = %s""")

    def is_existing_email(self, email):
        return self.execute_sql_for_one_result(email,
                                               """SELECT EXISTS (
                                               SELECT *
                                               FROM User
                                               WHERE email = %s)""")
