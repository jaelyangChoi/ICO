import pickle

import nltk  # 자연어 처리 패키지 문서탐색용, Test 클래스
import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import pandas as pd
from konlpy.tag import Okt  # Okt(Open Korean Text) 클래스
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras import models
from tensorflow.keras import optimizers


def read_csv_file(csv_file_name):
    """csv파일을 dataframe 형식으로 가져오기"""

    df = pd.read_csv("./ml_hyewon/" + csv_file_name + ".csv")
    return df


def tokenize(sentence):
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


def delete_stop_words(token_label_words):
    """의미없는 단어(불용어) 제거"""

    deleted_stop_words = []
    stop_words_list = []

    stop_words = read_csv_file("stop_words")
    stop_words_list = stop_words['stopword'].tolist()
    for row in token_label_words:
        if row[0] not in stop_words_list:
            deleted_stop_words.append(row)
    return deleted_stop_words


def remain_meaning_token(token_data):
    """토큰 전처리"""

    deleted_pumsa_data = delete_non_meaning_pumsa(token_data)
    meaning_tokens = delete_stop_words(deleted_pumsa_data)
    return meaning_tokens


def count_word_frequency(token_sentence, selected_words):
    """단어 빈도수 측정"""

    token_words = []
    for token_word in token_sentence:
        token_words.append(token_word[0])  # 단어+품사에서 단어만 추가
    return [token_words.count(word) for word in selected_words]


def reindex(data):
    """인덱스 재정렬"""

    data.reset_index(drop=True)
    return data


def devide_train_test(comments):
    """test/train data 분리"""

    train_data = comments.sample(frac=0.7, random_state=2019)  # 7:3 비율로 train, test data 분리
    test_data = comments.drop(train_data.index)
    reindex(train_data)
    reindex(test_data)
    return train_data, test_data


def data_preprocessing(data_file):
    """데이터 전처리"""

    comments = read_csv_file(data_file)
    train_data, test_data = devide_train_test(comments)

    train_token_data = [(tokenize(train_data['comment'][ind]), train_data['labeling'][ind]) for ind in
                        train_data.index]  # data 토큰화, 단어+품사+라벨
    test_token_data = [(tokenize(test_data['comment'][ind]), test_data['labeling'][ind]) for ind in test_data.index]

    meaning_tokens = remain_meaning_token(train_token_data)  # 무의미 품사, 불용어 제거, 단어+품사+라벨
    tokens = [meaning_token[0] for meaning_token in meaning_tokens]  # 단어
    text = nltk.Text(tokens, name='NMSC')
    selected_tokens = [common_word[0] for common_word in text.vocab().most_common(100)]  # 자주쓰이는 단어

    f=open("./ml_hyewon/commonwords.pkl", "wb")
    pickle.dump(selected_tokens, f)
    f.close()

    train_x = [count_word_frequency(train_token_row[0], selected_tokens) for train_token_row in
               train_token_data]  # x : 단어 빈도수 벡터화 y : 0,1,2 라벨
    test_x = [count_word_frequency(test_token_row[0], selected_tokens) for test_token_row in test_token_data]
    train_y = [train_token_row[1] for train_token_row in train_token_data]
    test_y = [test_token_row[1] for test_token_row in test_token_data]

    x_train = np.asarray(train_x).astype('float32')
    x_test = np.asarray(test_x).astype('float32')
    y_train = np.asarray(train_y).astype('float32')
    y_test = np.asarray(test_y).astype('float32')

    return x_train, x_test, y_train, y_test, selected_tokens


def learning_ml():
    """학습"""

    x_train, x_test, y_train, y_test, selected_tokens = data_preprocessing('comments2')
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(100,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                  loss=losses.binary_crossentropy,
                  metrics=[metrics.binary_accuracy])

    model.fit(x_train, y_train, epochs=10, batch_size=512)

    results = model.evaluate(x_test, y_test)


    model_json = model.to_json()
    with open("./ml_hyewon/model.json", "w") as json_file: #학습된 모델저장
        json_file.write(model_json)
    model.save_weights("./ml_hyewon/model.h5") #가중치저장

    return model
