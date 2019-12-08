from DTO.comment import *
from DAO.url import *
from DAO.user import *
from SQL.comment import SQL as sql


class CommentDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def insert_comment(self, data):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            url = UrlDAO()
            user = UserDAO()

            cursor.execute(sql.INSERT, (data.get_comment(),
                                        data.get_property(),
                                        data.get_learning(),
                                        url.select_index(data.get_url()),
                                        user.select_index(data.get_user_id())))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            return e

    def select_comments_by_url(self, url):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql.SELECT, url)

            comments = []
            for result in cursor.fetchall():
                comment = Comment()
                comment.set_all(result)
                comments.append(comment)

            self.db_conn.close_db()
            return comments

        except Exception as e:
            return e

    def update_my_comment(self):
        pass

    def delete_my_comment(self):
        pass
