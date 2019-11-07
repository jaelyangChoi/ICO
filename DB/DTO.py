class CommentDataForInsert:
    def __init__(self):
        self._text = ""
        self._propriety = 2
        self._learning = 0
        self._url = ""
        self.writer = ""

    # getter
    def getText(self):
        return self._text

    def getPropriety(self):
        return self._propriety

    def getLearning(self):
        return self._learning

    def getURL(self):
        return self._url

    def getWriter(self):
        return self._writer

    # setter
    def setText(self, txt):
        self._text = txt

    def setPropriety(self, propriety):
        if propriety >= 0 and propriety <= 2:
            self._propriety = propriety

    def setLearning(self, learning):
        if learning == 0 or learning == 1:
            self._learning = learning

    def setURL(self, URL):
        self._url = URL

    def setWriter(self, writer):
        self._writer = writer

class SelectedCommentData:
    def __init__(self):
        self._index = 0
        self._text = ""
        self._propriety = 0
        self._writer = ""
        self._time = ""

    def setAll(self, data):
        self._index = data[0]
        self._text = data[1]
        self._propriety = data[2]
        self._writer = data[3]
        self._time = data[4]

    # getter
    def getIndex(self):
        return self._index

    def getText(self):
        return self._text

    def getPropriety(self):
        return self._propriety

    def getWriter(self):
        return self._writer

    def getTime(self):
        return self._time

