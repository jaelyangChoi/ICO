class Comment:
    def __init__(self):
        self._index = None
        self._comment = None
        self._property = None
        self._learning = None
        self._url = None
        self._userID = None
        self._time = None

    def to_json(self):
        return {
            "index": self._index,
            "comment": self._text,
            "property": self._propriety,
            "ML_learning": self._learning,
            "url": self._url,
            "userID": self._writer,
            "time": self._time
        }

    # getter
    def get_index(self):
        return self._index

    def get_comment(self):
        return self._comment

    def get_property(self):
        return self._property

    def get_learning(self):
        return self._learning

    def get_url(self):
        return self._url

    def get_user_id(self):
        return self._userID

    def get_time(self):
        return self._time

    # setter
    def set_insert_data(self, comment):
        self._userID = comment['userID']
        self._comment = comment['comment']
        self._property = comment['property']
        self._url = comment['url']

    def set_all(self, result):
        self._index = result[0]
        self._comment = result[1]
        self._property = result[2]
        self._userID = result[3]
        self._time = result[4]

    def set_comment(self, comment):
        self._comment = comment

    def set_property(self, property):
        if property == '+' or property == '-':
            self._property = property
