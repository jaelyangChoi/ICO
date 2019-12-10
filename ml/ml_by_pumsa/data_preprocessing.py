import csv
import pandas as pd
from konlpy.tag import Okt  # Okt(Open Korean Text) 클래스
import nltk  # 자연어 처리 패키지 문서탐색용, Test 클래스
import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import pickle


COMMENTSFILENAME = "comments"
PUMSALIST = ['Adjective', 'Adverb', 'Alpha', 'Determiner', 'Exclamation', 'KoreanParticle', 'Noun', 'Verb']
ML_FILE_PATH = "../../dataset_pumsa_ml/"
COMMONWORDSCOUNT = 100


class DataPreprocessing:

    def __init__(self):
        self.comments = self.read_csv_file(COMMENTSFILENAME)
        self.stop_words = self.read_csv_file("stop_words")['stopword'].tolist()

        self.train_data = self.reindex(self.comments.sample(frac=0.7, random_state=2019))  # 7:3 비율로 train, test data 분리
        self.test_data = self.reindex(self.comments.drop(self.train_data.index))
        self.common_words_list = []

    def read_csv_file(self, csv_file_name):
        """csv파일을 dataframe 형식으로 가져오기"""

        df = pd.read_csv(ML_FILE_PATH + csv_file_name + ".csv")
        return df

    def tokenize(self, sentence):
        """품사"""

        okt = Okt()
        return okt.pos(sentence, norm=True, stem=True)

    def reindex(self, data):
        """인덱스 재정렬"""

        data.reset_index(drop=True)
        return data

    def make_token_word_list(self, tagged_token_sentences):
        """긍/부정 달린 tokenize 문장 리스트를  tokenize 단어 리스트로 생성"""

        #  tagged_token_sentence [[[('좃', 'Noun'), ('국사', 'Noun')], 0]]

        token_word_list = []
        for token_sentence in tagged_token_sentences:
            for token_word in token_sentence[0]:
                token_word_list.append(token_word)

        return token_word_list

    def remain_selected_pumsa_word(self, token_words):
        """선택한 품사만 남김"""

        selected_pumsa_words=[]
        for token_word in token_words:
            if token_word[1] in PUMSALIST:
                selected_pumsa_words.append(token_word)
        return selected_pumsa_words

    def remain_meaning_word(self, token_words):
        """의미있는 단어만 남김"""

        selected_meaning_words=[]
        for token_word in token_words:
            if token_word[0] not in self.stop_words:
                selected_meaning_words.append(token_word)
        return selected_meaning_words

    def make_common_words_list(self, token_words):
        """단어 빈도수 측정 위한 common words list 생성"""

    # token_words [('좃', 'Noun'), ('국사', 'Noun'), ('기단', 'Noun')]

        temp_token_words = self.remain_selected_pumsa_word(token_words)
        token_words_list = self.remain_meaning_word(temp_token_words)
        text = nltk.Text([token_word[0] for token_word in token_words_list], name='NMSC')

    # common_words_list ['하다', '있다', '없다']

        self.common_words_list = [common_word[0] for common_word in text.vocab().most_common(COMMONWORDSCOUNT)]

        return self.common_words_list

    def count_word_frequency(self, token_sentence):
        """단어 빈도수 측정"""

        token_words = []
        for token_word in token_sentence:
            token_words.append(token_word[0])  # 단어+품사에서 단어만 추가
        return [token_words.count(word) for word in self.common_words_list]

    def save_as_pickle_file(self, pickle_file_name, pickle_data):
        """pickle file 생성"""

        f = open(ML_FILE_PATH+pickle_file_name+".pkl", "wb")
        pickle.dump(pickle_data, f)
        f.close()
        return f

    def preprocessing_data_by_pumsa(self):
        """data preprocessing"""

        train_token_data = [[self.tokenize(self.train_data['comment'][ind]), self.train_data['labeling'][ind]] for ind in
                            self.train_data.index]  # train_token_data [[[('좃', 'Noun'), ('국사', 'Noun')], 0]]
        test_token_data = [[self.tokenize(self.test_data['comment'][ind]), self.test_data['labeling'][ind]] for ind in
                           self.test_data.index]
        self.save_as_pickle_file("common_words_list",
                                 self.make_common_words_list(self.make_token_word_list(train_token_data)))

        # x : 단어 빈도수 벡터화 y : 0,1 라벨

        train_x = [self.count_word_frequency(train_token_row[0]) for train_token_row in
                   train_token_data]
        test_x = [self.count_word_frequency(test_token_row[0]) for test_token_row in test_token_data]
        train_y = [train_token_row[1] for train_token_row in train_token_data]
        test_y = [test_token_row[1] for test_token_row in test_token_data]

        x_train = np.asarray(train_x).astype('float32')
        x_test = np.asarray(test_x).astype('float32')
        y_train = np.asarray(train_y).astype('float32')
        y_test = np.asarray(test_y).astype('float32')
        return x_train, x_test, y_train, y_test
