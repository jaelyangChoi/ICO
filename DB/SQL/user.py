class SQL:
    SELECT_INDEX = "SELECT _index FROM User WHERE id = %s"
    SELECT_EMAIL = "SELECT _index, id, name, email FROM user WHERE email = %s"
    CHECK_EMAIL = """SELECT EXISTS (SELECT *
                                    FROM User
                                    WHERE email = %s)"""
