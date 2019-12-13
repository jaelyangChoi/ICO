class DefaultKeyword:
    def __init__(self):
        self._data = {
            'index': None,
            'keyword': None,
            'split_keyword': None
        }

    # getter
    def get_data(self):
        return self._data

    def get_keyword(self):
        return self._data['keyword']

    def get_split_keyword(self):
        return self._data['split_keyword']

    # setter
    def set_all(self, data):
        self._data['index'] = data[0]
        self._data['keyword'] = data[1]
        self._data['split_keyword'] = data[2]

    def set_keyword(self, keyword):
        self._data['keyword'] = keyword

    def set_split_keyword(self, split_keyword):
        self._data['split_keyword'] = split_keyword


