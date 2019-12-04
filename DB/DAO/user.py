from DAO.index import *


class UserDAO(Index):

    def select_index(self, user):
        return self.execute_sql_for_one_result(user,
                                               """SELECT _index
                                               FROM User
                                               WHERE id = %s""")

    def is_correct_emial(self, emial):
        if self.execute_sql_for_one_result(emial,
                                           """SELECT *
                                        FROM User
                                        WHERE email = %s""") is None:
            return -1;
        return 0
