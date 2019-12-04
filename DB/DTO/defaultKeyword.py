class DefaultKeyword:
    def __init__(self):
        self._index = None
        self._keyword = None
        self._split_keyword = None

    def set_all(self, data):
        self._index = data[0]
        self._keyword = data[1]
        self._split_keyword = data[2]

    def set_keyword(self, keyword):
        self._keyword = keyword

    def set_split_keyword(self, split_keyword):
        self._split_keyword = split_keyword

    def get_keyword(self):
        return self._keyword

    def get_split_keyword(self):
        return self._split_keyword

    def to_json(self):
        return {
            'index': self._index,
            'keyword': self._keyword,
            'split_keyword': self._split_keyword
        }
