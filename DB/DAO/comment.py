from DTO.comment import *
from DAO.url import *
from DAO.user import *
from SQL.comment import CommentSQL as SQL


class CommentDAO:
    def __init__(self):
        self.db_conn = DBConnection()

    def insert_comment(self, data):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            url = UrlDAO()
            user = UserDAO()

            cursor.execute(SQL.INSERT_COMMENT,
                           (data.get_comment(),
                            data.get_property(),
                            data.get_learning(),
                            url.select_index(data.get_url()),
                            user.select_index(data.get_user_id())))
            conn.commit()

            self.db_conn.close_db()

        except Exception as e:
            print(e)
            return e

    def select_comments_by_url(self, url):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.SELECT_COMMENTS, url)

            comment_list = []
            for result in cursor.fetchall():
                comment = Comment()
                comment.set_all(result)
                comment_list.append(comment)

            self.db_conn.close_db()
            return comment_list

        except Exception as e:
            return e

    def update_comment(self, data):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.UPDATE_COMMENT,
                           (data.get_comment(),
                            data.get_index()))
            conn.commit()

        except Exception as e:
            return e

    def delete_comment(self, index):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.DELETE_COMMENT, index)
            conn.commit()

        except Exception as e:
            return e
