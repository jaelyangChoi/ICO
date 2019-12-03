class Comment:
    def __init__(self):
        self._comment = {
            "idx": 0,
            "text": "",
            "property":'+',
            "ML_learning": 0,
            "url": "",
            "writer": "",
            "time": ""
        }

    # getter
    def get_comment(self):
        return self._comment

    def get_index(self):
        return self._comment['idx']

    def get_text(self):
        return self._comment['text']

    def get_property(self):
        return self._comment['property']

    def get_learning(self):
        return self._comment['ML_learning']

    def get_url(self):
        return self._comment['url']

    def get_writer(self):
        return self._comment['writer']

    def get_time(self):
        return self._comment['time']

    # setter
    def set_insert_comment(self, comment):
        self._comment['writer'] = comment['userID']
        self._comment['text'] = comment['comment']
        self._comment['property'] = comment['property']
        self._comment['url'] = comment['url']


    def set_all(self, data):
        self._comment['idx'] = data[0]
        self._comment['text'] = data[1]
        self._comment['property'] = data[2]
        self._comment['writer'] = data[3]
        self._comment['time'] = data[4]

    def set_text(self, txt):
        self._comment['text'] = txt

    def set_property(self, property):
        if property == 0 or property == 1:
            self._comment['property'] = property
        else:
            return -1

    def set_learning(self, learning):
        if learning == 0 or learning == 1:
            self._comment['ML_learning'] = learning
        else:
            return -1

    def set_url(self, url):
        self._comment['url'] = url

    def set_writer(self, writer):
        self._comment['writer'] = writer