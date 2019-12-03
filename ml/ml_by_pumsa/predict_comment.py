import pickle

import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import pandas as pd
from konlpy.tag import Okt  # Okt(Open Korean Text) 클래스
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras import optimizers
from tensorflow.keras.models import model_from_json


class CommentPredict:
    def __init__(self):
        json_file = open("./ml/ml_by_pumsa/model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        self.predict_score = 0
        self.predict_result = 0
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("./ml/ml_by_pumsa/model.h5")
        self.model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                           loss=losses.binary_crossentropy,
                           metrics=[metrics.binary_accuracy])

    def read_csv_file(self, csv_file_name):
        """csv파일을 dataframe 형식으로 가져오기"""

        df = pd.read_csv("./ml/ml_by_pumsa/" + csv_file_name + ".csv")
        return df

    def tokenize(self, sentence):
        """품사"""

        okt = Okt()
        return okt.pos(sentence, norm=True, stem=True)

    def delete_non_meaning_pumsa(self, token_label_sentences):
        """의미없는 품사 제거"""

        deleted_pumsa_data = []
        pumsa_list = ["Adjective", "Adverb", "Alpha", "Determiner", "Exclamation",
                      "KoreanParticle", "Noun", "Verb"]

        for row in token_label_sentences: # token_label_sentences ex)[([('마녀', 'Noun'), ('같다', 'Adjective')], '0')]

            for token_word in row[0]:
                if token_word[1] in pumsa_list:
                    deleted_pumsa_data.append([token_word[0], token_word[1], row[1]])
        return deleted_pumsa_data

    def delete_stop_words(self, token_label_words):
        """의미없는 단어(불용어) 제거"""

        deleted_stop_words = []
        stop_words_list = []

        stop_words = self.read_csv_file("stop_words")
        stop_words_list = stop_words['stopword'].tolist()
        for row in token_label_words:
            if row[0] not in stop_words_list:
                deleted_stop_words.append(row)
        return deleted_stop_words

    def remain_meaning_token(self, token_data):
        """토큰 전처리"""

        deleted_pumsa_data = self.delete_non_meaning_pumsa(token_data)
        meaning_tokens = self.delete_stop_words(deleted_pumsa_data)
        return meaning_tokens

    def count_word_frequency(self, token_sentence, selected_words):
        """단어 빈도수 측정"""

        token_words = []
        for token_word in token_sentence:  # token_sentence: [['분위기', 'Noun','0')], ['달리다', 'Verb','0']]
            token_words.append(token_word[0])  # 단어+품사에서 단어만 추가
        return [token_words.count(word) for word in selected_words]

    def data_preprocessing(self, data):
        """데이터 전처리"""

        f = open("./ml/ml_by_pumsa/commonwords.pkl", "rb")
        selected_tokens = pickle.load(f)
        f.close()
        token_data=self.remain_meaning_token([(self.tokenize(data), '0')])
        test_data = self.count_word_frequency(token_data, selected_tokens)
        return np.expand_dims(np.asarray(test_data).astype('float32'), axis=0)

    def predict(self, comment):
        """예측"""

        data = self.data_preprocessing(comment)
        score = float(self.model.predict(data))
        self.predict_score = score
        if score > 0.7:
            self.predict_result = 1
            return "1"
        else:
            self.predict_result = 0
            return "0"
