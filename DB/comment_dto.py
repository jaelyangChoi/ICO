class Comment:
    def __init__(self):
        self._index = 0
        self._text = ""
        self._propriety = 0
        self._writer = ""
        self._time = ""

    # getter
    def get_index(self):
        return self._index

    def get_text(self):
        return self._text

    def get_propriety(self):
        return self._propriety

    def get_learning(self):
        return self._learning

    def get_url(self):
        return self._url

    def get_writer(self):
        return self._writer

    def get_time(self):
        return self._time

    # setter
    def set_all(self, data):
        self._index = data[0]
        self._text = data[1]
        self._propriety = data[2]
        self._writer = data[3]
        self._time = data[4]

    def set_text(self, txt):
        self._text = txt

    def set_propriety(self, propriety):
        if propriety >= 0 and propriety <= 2:
            self._propriety = propriety

    def set_learning(self, learning):
        if learning == 0 or learning == 1:
            self._learning = learning

    def set_url(self, URL):
        self._url = URL

    def set_writer(self, writer):
        self._writer = writer

COMMENT = {
    'index': 0,
    'text': '',
    'propriety': 0,
    'writer': '',
    'time': ''
}