import pandas as pd
from hgtk import text, letter, checker
from sklearn.externals import joblib

from .const import ALPHABET_LIST, CHOSUNG_LIST, JONGSUNG_LIST, JUNGSUNG_LIST, NUMBER_LIST, SPECIAL_CHARACTERS_LIST


class ModelByWord:
    def __init__(self):
        text.decompose = self.__decompose
        self._model = joblib.load("./dataset/model_sgd.pkl")
        self._word_list = [CHOSUNG_LIST, JUNGSUNG_LIST, JONGSUNG_LIST,
                           SPECIAL_CHARACTERS_LIST, NUMBER_LIST, ALPHABET_LIST]

    @staticmethod
    def __decompose(text, latin_filter=True, compose_code=u" "):
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
        df_list = ["cho", "jung", "jong", "special_characters", "number", "alphabet"]

        comment_decompose = text.decompose(comment)
        result = list(filter(lambda word: word != ' ', comment_decompose.split(' ')))
        result = list(filter(lambda element: element != '', result))

        df_dict = {}
        for key, word_type in zip(df_list, self._word_list):
            df_dict[key] = pd.DataFrame(0, columns=word_type, index=range(1), dtype=float)

        for word in result:
            total_letter_count = 0

            if checker.is_hangul(word):
                length = len(word)

                if length == 3:
                    df_dict['cho'][word[0]] += 1
                    df_dict['jung'][word[1]] += 1
                    df_dict['jong'][word[2]] += 1
                    total_letter_count += 3
                elif length == 2:
                    df_dict['cho'][word[0]] += 1
                    df_dict['jung'][word[1]] += 1
                    df_dict['jong'][' '] += 1
                    total_letter_count += 3
                else:
                    if word in CHOSUNG_LIST:
                        df_dict['cho'][word[0]] += 1
                    elif word in JUNGSUNG_LIST:
                        df_dict['jung'][word[0]] += 1
                    else:
                        df_dict['jong'][word[0]] += 1

                    total_letter_count += 1
            else:
                if word.lower() in ALPHABET_LIST:
                    word = word.lower()
                    df_dict['alphabet'][word] += 1
                elif word in NUMBER_LIST:
                    df_dict['number'][word] += 1
                else:
                    if word in SPECIAL_CHARACTERS_LIST:
                        df_dict['special_characters'][word] += 1
                    else:
                        df_dict['special_characters']['etc'] += 1

        df_result = pd.concat(df_dict, axis=1)

        return df_result

    def predict(self, comment):
        data = self._preprocess(comment)
        predict = self._model.predict(data)

        return predict
