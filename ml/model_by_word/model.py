import joblib
import pandas as pd
from hgtk import text, letter, checker

from .const import ALPHABET_LIST, CHOSUNG_LIST, JONGSUNG_LIST, JUNGSUNG_LIST, NUMBER_LIST, SPECIAL_CHARACTERS_LIST

CHOSUNG = 3
JUNGSUNG = 2
JONGSUNG = 1


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
        comment_decompose = text.decompose(comment)
        removed_space_word = list(filter(lambda word: word != ' ', comment_decompose.split(' ')))
        split_word = list(filter(lambda element: element != '', removed_space_word))

        df_result = self._word_store_in_dataframe(split_word)

        return df_result

    def predict(self, comment):
        data = self._preprocess(comment)
        predict = self._model.predict(data)

        print(self._model.predict_proba(data))

        return predict

    def _word_store_in_dataframe(self, split_word):
        df_list = ["cho", "jung", "jong", "special_characters", "number", "alphabet"]

        temp_dict = {}
        for key, word_type in zip(df_list, self._word_list):
            temp_dict[key] = pd.DataFrame(0, columns=word_type, index=range(1), dtype=float)

        total_letter_count = 0
        for word in split_word:
            temp_dict, letter_count = self._insert_dataframe(temp_dict, word)
            total_letter_count += letter_count

        result = pd.concat(temp_dict, axis=1) / total_letter_count

        return result

    def _insert_dataframe(self, temp_dict, word):
        letter_count = 0

        if checker.is_hangul(word):
            length = len(word)

            if length == CHOSUNG:
                temp_dict['cho'][word[0]] += 1
                temp_dict['jung'][word[1]] += 1
                temp_dict['jong'][word[2]] += 1
                letter_count += 3
            elif length == JUNGSUNG:
                temp_dict['cho'][word[0]] += 1
                temp_dict['jung'][word[1]] += 1
                temp_dict['jong'][' '] += 1
                letter_count += 3
            else:
                if word in CHOSUNG_LIST:
                    temp_dict['cho'][word[0]] += 1
                elif word in JUNGSUNG_LIST:
                    temp_dict['jung'][word[0]] += 1
                else:
                    temp_dict['jong'][word[0]] += 1

                letter_count += 1
        else:
            if word.lower() in ALPHABET_LIST:
                word = word.lower()
                temp_dict['alphabet'][word] += 1
            elif word in NUMBER_LIST:
                temp_dict['number'][word] += 1
            else:
                if word in SPECIAL_CHARACTERS_LIST:
                    temp_dict['special_characters'][word] += 1
                else:
                    temp_dict['special_characters']['etc'] += 1

            letter_count += 1

        return temp_dict, letter_count
