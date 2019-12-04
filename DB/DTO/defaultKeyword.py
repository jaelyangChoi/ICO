class DefaultKeyword:
    def __init__(self, index=None, keyword=None, split_keyword=None):
        self._index = index
        self._keyword = keyword
        self._split_keyword = split_keyword

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