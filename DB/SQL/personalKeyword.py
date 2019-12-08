class SQL:
    INSERT = "INSERT INTO PersonalKeyword(keyword, user) VALUES(%s, %s)"
    DELETE = "DELETE FROM PersonalKeyword WHERE keyword = %s AND user = %s"
    SELECT = """SELECT keyword FROM PersonalKeyword, User
                WHERE PersonalKeyword.user = User._index
                AND User.id = %s"""
