class UserSQL:
    SELECT_INDEX = "SELECT _index FROM user WHERE id = %s"
    SELECT_USER = "SELECT _index, id, name, email FROM user WHERE email = %s"
    CHECK_EMAIL = """SELECT EXISTS (SELECT *
                                    FROM user
                                    WHERE email = %s)"""
