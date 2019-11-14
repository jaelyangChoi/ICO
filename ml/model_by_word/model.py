import numpy as np
from hgtk import text, letter, checker


class ModelByWord:
    def __init__(self):
        text.decompose = self._decompose

    @staticmethod
    def _decompose(text, latin_filter=True, compose_code=u" "):
        result = u""

        for c in list(text):
            if checker.is_hangul(c):

                if checker.is_jamo(c):
                    result = result + c + compose_code
                else:
                    result = result + "".join(letter.decompose(c)) + compose_code

            else:
                if latin_filter:  # 한글 외엔 Latin1 범위까지만 포함 (한글+영어)
                    if checker.is_latin1(c):
                        result = result + c + compose_code
                else:
                    result = result + c + compose_code

        return result

    def _preprocess(self, comment):
            comment_decompose = text.decompose(comment)
            result = list(filter(lambda word: word != ' ', comment_decompose.split(' ')))
            result = list(filter(lambda element: element != '', result))
            return result

    def fit(self, input):
        word_list = self._preprocess(input)
