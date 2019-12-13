class User:
    def __init__(self):
        self._index = None
        self._id = None
        self._name = None
        self._email = None

    def to_json(self):
        return {
            'index': self._index,
            'id': self._id,
            'name': self._name,
            'email': self._email
        }

    # getter
    def get_index(self):
        return self._index

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    # setter
    def set_all(self, result):
        self._index = result[0]
        self._id = result[1]
        self._name = result[2]
        self._email = result[3]

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email
