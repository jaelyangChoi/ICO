class PersonalKeywordSQL:
    INSERT_KEYWORD = "INSERT INTO personalKeyword(keyword, user) VALUES(%s, %s)"
    DELETE_KEYWORD = "DELETE FROM personalKeyword WHERE keyword = %s AND user = %s"
    SELECT_KEYWORDS = """SELECT keyword FROM personalKeyword, User
                WHERE personalKeyword.user = user._index
                AND user.id = %s"""
