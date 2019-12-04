class Comment:
    def __init__(self):
        self._data = {
            "index": 0,
            "comment": "",
            "property": "-",
            "ML_learning": 0,
            "url": "",
            "userID": "",
            "time": ""
        }

    # getter
    def get_data(self):
        return self._data

    def get_index(self):
        return self._data['index']

    def get_comment(self):
        return self._data['comment']

    def get_property(self):
        return self._data['property']

    def get_learning(self):
        return self._data['ML_learning']

    def get_url(self):
        return self._data['url']

    def get_user_id(self):
        return self._data['userID']

    def get_time(self):
        return self._data['time']

    # setter
    def set_insert_data(self, comment):
        self._data['userID'] = comment['userID']
        self._data['comment'] = comment['comment']
        self._data['property'] = comment['property']
        self._data['url'] = comment['url']

    def set_all(self, data):
        self._data['index'] = data[0]
        self._data['comment'] = data[1]
        self._data['property'] = data[2]
        self._data['userID'] = data[3]
        self._data['time'] = data[4]

    def set_comment(self, comment):
        self._data['comment'] = comment

    def set_property(self, property):
        if property == '+' or property == '-':
            self._data['property'] = property
        else:
            return -1

    def set_learning(self, learning):
        if learning == 0 or learning == 1:
            self._data['ML_learning'] = learning
        else:
            return -1

    def set_url(self, url):
        self._data['url'] = url

    def set_user_id(self, userID):
        self._data['userID'] = userID