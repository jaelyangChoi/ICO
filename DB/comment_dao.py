from comment_dto import *
from url_dao import *
from user_dao import *

class CommentDAO:
    # db_conn = None

    def __init__(self):
        self.db_conn = DBConnection()

    def insert_comment(self, data):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            """sql = "SELECT _index FROM Articles WHERE URL = %s"
            cursor.execute(sql, data.get_url())

            result = cursor.fetchone()
            url_index = result[0]"""
            url_dao = URL_DAO()

            """sql = "SELECT _index FROM User WHERE id = %s"
            cursor.execute(sql, data.get_writer())

            result = cursor.fetchone()
            writer_index = result[0]"""
            user_dao = UserDAO()

            sql = "INSERT INTO comments(text, propriety, MLlearning, URL, writer) VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data.get_text(),
                                 data.get_propriety(),
                                 data.get_learning(),
                                 url_dao.select_index(data.get_url()),
                                 user_dao.select_index(data.get_writer())))
            conn.commit()

        except Exception as e:
            print(e)

    def select_comments_by_url(self, url):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            sql = """SELECT Comments._index, text, propriety, User.id, time
                    FROM Comments, User, Articles
                    WHERE Comments.writer = User._index
                    AND Comments.URL = Articles._index
                    AND Articles.URL = %s"""
            cursor.execute(sql, url)

            data_list = []

            for result in cursor.fetchall():
                data = Comment()
                data.set_all(result)
                data_list.append(data)

            return data_list

        except Exception as e:
            print(e)