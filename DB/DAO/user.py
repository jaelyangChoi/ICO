from DAO.index import *


class UserDAO(Index):

    def select_index(self, user):
        return self.execute_sql_for_one_result(user,
                                               """SELECT _index
                                               FROM User
                                               WHERE id = %s""")

    def is_correct_password(self, id, pw):
        if self.execute_sql_for_one_result(id,
                                           """SELECT password
                                           FROM User
                                           WHERE id = %s""") == pw:
            return True
        return False

    def update_password(self, id, old_pw, new_pw):
        if self.is_correct_password(id, old_pw) is True:
            try:
                conn = self.db_conn.get_connection()
                cursor = conn.cursor()

                sql = "UPDATE User SET password = %s WHERE id = %s"
                cursor.execute(sql, (new_pw, id))
                conn.commit()

                self.db_conn.close_db()

            except Exception as e:
                return -1

        else:
            return 0

    def insert_new_user(self):
        pass