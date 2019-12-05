class User:
    def __init__(self, id, name, email, index=None):
        self._data = {
            'index': index,
            'id': id,
            'name': name,
            'email': email
        }

    def set_id(self, id):
        self._data['id'] = id

    def set_name(self, name):
        self._data['name'] = name

    def set_email(self, email):
        self._data['email'] = email

    def get_index(self):
        return self._data['index']

    def get_id(self):
        return self._data['id']

    def get_name(self):
        return self._data['name']

    def get_email(self):
        return self._data['email']

    def get_user(self):
        return self._data
