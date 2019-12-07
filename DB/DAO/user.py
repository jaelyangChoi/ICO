from DAO.index import *
from DTO.user import *
from SQL.user import *


class UserDAO(Index):
    def select_index(self, user):
        return self.execute_sql_for_one_result(user, SQL.SELECT_INDEX)

    def select_user_by_email(self, email):
        user = User()
        user.set_all(self.execute_sql_for_one_result(email, SQL.SELECT_EMAIL))
        return user

    def is_existing_email(self, email):
        return self.execute_sql_for_one_result(email, SQL.CHECK_EMAIL)
