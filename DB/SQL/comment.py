class CommentSQL:
    INSERT_COMMENT = "INSERT INTO comment(comment, property, MLlearning, url_index, user_index) VALUES(%s, %s, %s, %s, %s)"
    SELECT_COMMENTS = """SELECT comment._index, comment, property, user.id, time
                         FROM comment, user, article
                         WHERE comment.user_index = user._index
                         AND comment.url_index = article._index
                         AND article.URL = %s
                         ORDER BY time DESC"""
    UPDATE_COMMENT = "UPDATE comment SET comment = %s WHERE _index = %s"
    DELETE_COMMENT = "DELETE FROM comment WHERE _index = %s"