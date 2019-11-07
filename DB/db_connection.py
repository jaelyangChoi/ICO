import pymysql

# 클래스
class db_connection:
    conn = None

    # 생성자
    def __init__(self):
        pass    # 함수에서 아무것도 안할 때 사용

    def getConnection(self):
        # 예외처리
        try:
            # database에 접근
            db_connection.conn = pymysql.connect(host='localhost',
                                   user='ICO',
                                   password='ico09',
                                   db='icoservice',
                                   charset='utf8')
            # database를 사용하기 위한 cursor를 세팅
#            cursor = conn.cursor()

            return db_connection.conn

        except Exception as e:
            print(e)

    def closeDB(self):
        if db_connection.conn != None:
            db_connection.conn.close()

    # 소멸자
    def __del__(self):
        self.closeDB()