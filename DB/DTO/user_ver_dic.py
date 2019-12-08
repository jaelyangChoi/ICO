class User:
    def __init__(self, id, name, email):
        self._user = {
            'index': None,
            'id': id,
            'name': name,
            'email': email
        }

    # getter
    def get_user(self):
        return self._user

    def get_index(self):
        return self._user['index']

    def get_id(self):
        return self._user['id']

    def get_name(self):
        return self._user['name']

    def get_email(self):
        return self._user['email']

    # setter
    def set_all(self, result):
        self._user['index'] = result[0]
        self._user['id'] = result[1]
        self._user['name'] = result[2]
        self._user['email'] = result[3]

    def set_id(self, id):
        self._user['id'] = id

    def set_name(self, name):
        self._user['name'] = name

    def set_email(self, email):
        self._user['email'] = email
