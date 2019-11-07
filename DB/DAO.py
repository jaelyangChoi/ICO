from DTO import *
from db_connection import *
import pymysql

class DatabaseDAO:
    # dbConn = None

    def __init__(self):
        self.dbConn = db_connection()

    def insertComment(self, data):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = "SELECT _index FROM Articles WHERE URL = %s"
            cursor.execute(sql, data.getURL())

            result = cursor.fetchone()
            url_index = result[0]

            sql = "SELECT _index FROM User WHERE id = %s"
            cursor.execute(sql, data.getWriter())

            result = cursor.fetchone()
            writer_index = result[0]

            sql = "INSERT INTO comments(text, propriety, MLlearning, URL, writer) VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data.getText(), data.getPropriety(), data.getLearning(), url_index, writer_index))
            conn.commit()

        except Exception as e:
            print(e)

    def selectCommentsByURL(self, url):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = """SELECT Comments._index, text, propriety, User.id, time
                    FROM Comments, User, Articles
                    WHERE Comments.writer = User._index
                    AND Comments.URL = Articles._index
                    AND Articles.URL = %s"""
            cursor.execute(sql, url)

            dataList = []

            for result in cursor.fetchall():
                data = SelectedCommentData()
                data.setAll(result)
                dataList.append(data)

            return dataList

        except Exception as e:
            print(e)

    def selectDefaultKeywords(self):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = """SELECT word FROM DefaultKeywords"""
            cursor.execute(sql)

            keywordList = []
            for result in cursor.fetchall():
                keywordList.append(result[0])

            return keywordList

        except Exception as e:
            print(e)

    def insertPersonalKeyword(self, id, keyword):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = """SELECT _index From User WHERE id = %s"""
            cursor.execute(sql, id)

            result = cursor.fetchone()
            user_index = result[0]

            sql = """INSERT INTO PersonalKeywords(keyword, user) VALUES(%s, %s)"""
            cursor.execute(sql, (keyword, user_index))
            conn.commit()

        except Exception as e:
            print(e)

    def selectPersonalKeywordsByUser(self, id):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = """SELECT keyword FROM PersonalKeywords, User
                    WHERE PersonalKeywords.user = User._index
                    AND User.id = %s"""
            cursor.execute(sql, id)

            keywordList = []
            for result in cursor.fetchall():
                keywordList.append(result[0])

            return keywordList

        except Exception as e:
            print(e)

    def deletePersonalKeywords(self, id, keyword):
        try:
            conn = self.dbConn.getConnection()
            cursor = conn.cursor()

            sql = "SELECT _index FROM User WHERE id=%s"
            cursor.execute(sql, id);

            result = cursor.fetchone()
            user_index = result[0]

            sql = """DELETE FROM PersonalKeywords
                    WHERE user=%s AND keyword=%s"""
            cursor.execute(sql, (user_index, keyword))
            conn.commit()

        except Exception as e:
            print(e)
