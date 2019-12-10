import pickle

import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
from konlpy.tag import Okt  # Okt(Open Korean Text) 클래스
from sklearn.externals import joblib

ML_FILE_PATH = "./dataset_pumsa_ml/"
# MODELNAME="tensor4"
MODELNAME = "linear"


class CommentPredict:
    def __init__(self):
        self.common_words_list = self.load_pickle_file("common_words_list")
        # json_file = open(ML_FILE_PATH+MODELNAME+".json", "r")
        # loaded_model_json = json_file.read()
        # json_file.close()
        # self.predict_score = 0
        # self.predict_result = "0"
        # self.model = model_from_json(loaded_model_json)
        # self.model.load_weights(ML_FILE_PATH+MODELNAME+".h5")
        # self.model.compile(optimizer=optimizers.RMSprop(lr=0.001),
        #                    loss=losses.binary_crossentropy,
        #                    metrics=[metrics.binary_accuracy])
        self.model = joblib.load(ML_FILE_PATH + MODELNAME + ".pkl")

    def load_pickle_file(self, pickle_file_name):
        f = open(ML_FILE_PATH + pickle_file_name + ".pkl", "rb")
        pickle_data = pickle.load(f)
        f.close()
        return pickle_data

    def tokenize(self, sentence):
        """품사"""

        okt = Okt()
        return okt.pos(sentence, norm=True, stem=True)

    def count_word_frequency(self, token_sentence):
        """단어 빈도수 측정"""

        token_words = []
        for token_word in token_sentence:
            token_words.append(token_word[0])  # 단어+품사에서 단어만 추가

        return [token_words.count(word) for word in self.common_words_list]

    def preprocessing_data_by_pumsa(self, comment):
        """data preprocessing"""

        data = self.tokenize(comment)
        test_data = self.count_word_frequency(data)
        return np.expand_dims(np.asarray(test_data).astype('float32'), axis=0)

    def predict(self, comment):
        """예측"""

        data = self.preprocessing_data_by_pumsa(comment)
        return str(self.model.predict(data))
        # score = float(self.model.predict(data))
        # self.predict_score = score
        # if score > 0.7:
        #     self.predict_result = "1"
        #     return "1"
        # else:
        #     self.predict_result = "0"
        #     return "0"

# dd=CommentPredict()
# df=pd.read_csv(ML_FILE_PATH+"comments_test.csv")
# comments_list=df['comment'].tolist()
# start_time = time.time()
# for comment in comments_list:
#     print(str(dd.predict(comment)[1]))
# print("실행시간:"+str(time.time()-start_time))
