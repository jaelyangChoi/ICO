class SQL:
    INSERT = "INSERT INTO Comment(comment, property, MLlearning, URL, userID) VALUES(%s, %s, %s, %s, %s)"
    SELECT = """SELECT Comment._index, comment, property, User.id, time
                             FROM Comment, User, Article
                             WHERE Comment.userID = User._index
                             AND Comment.URL = Article._index
                             AND Article.URL = %s"""