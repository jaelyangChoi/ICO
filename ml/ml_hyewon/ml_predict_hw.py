import csv
import pandas as pd
from konlpy.tag import Okt  # Okt(Open Korean Text) 클래스
import nltk  # 자연어 처리 패키지 문서탐색용, Test 클래스
import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import pickle
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras.models import model_from_json
import tensorflow as tf


class CommentClassifyModel:
    def __init__(self):
        json_file = open("./ml_hyewon/model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("./ml_hyewon/model.h5")
        self.model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                  loss=losses.binary_crossentropy,
                  metrics=[metrics.binary_accuracy])

    def read_csv_file(self, csv_file_name):
        """csv파일을 dataframe 형식으로 가져오기"""

        df = pd.read_csv("./ml_hyewon/" + csv_file_name + ".csv")
        return df

    def tokenize(self, sentence):
        """품사"""

        okt = Okt()
        return okt.pos(sentence, norm=True, stem=True)

    def delete_non_meaning_pumsa(token_label_sentences):
        """의미없는 품사 제거"""

        deleted_pumsa_data = []
        pumsa_list = ["Adjective", "Adverb", "Alpha", "Determiner", "Exclamation",
                      "KoreanParticle", "Noun", "Verb"]

        # token_label_sentences ex)([('마녀', 'Noun'), ('같다', 'Adjective')], '0')
        for row in token_label_sentences:
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
        for token_word in token_sentence:  # token_sentence: [('분위기', 'Noun'), ('달리다', 'Verb')]
            token_words.append(token_word[0])  # 단어+품사에서 단어만 추가
        return [token_words.count(word) for word in selected_words]

    def data_preprocessing(self, data):
        """데이터 전처리"""

        f = open("./ml_hyewon/commonwords.pkl", "rb")
        selected_tokens=pickle.load(f)
        f.close()
        token_data = [(self.tokenize(data), '0')]  # data 토큰화, 단어+품사+임의의 라벨
        test_data = self.count_word_frequency(token_data[0][0], selected_tokens)
        return np.asarray(test_data).astype('float32')

    def predict(self, comment):
        """예측"""

        pre_data=self.data_preprocessing(comment)
        data=np.expand_dims(pre_data, axis=0)
        score = float(self.model.predict(data))
        if (score > 0.7):
            return "1"
        else:
            return "0"

