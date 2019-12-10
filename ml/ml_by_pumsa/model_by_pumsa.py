import data_preprocessing as dp
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB

import pickle
ML_FILE_PATH = "../../dataset_pumsa_ml/"


class ModelByPumsa:
    def __init__(self):
        self.x_train, self.x_test, self.y_train, self.y_test = dp.DataPreprocessing().preprocessing_data_by_pumsa()
        self.common_words_list=self.load_pickle_file("common_words_list")

    def save_as_pickle_file(self, pickle_file_name, pickle_data):
        """pickle file 생성"""

        f = open(ML_FILE_PATH+pickle_file_name+".pkl", "wb")
        pickle.dump(pickle_data, f)
        f.close()
        return f

    def load_pickle_file(self, pickle_file_name):
        f = open(ML_FILE_PATH+pickle_file_name+".pkl", "rb")
        pickle_data = pickle.load(f)
        f.close()
        return pickle_data

    def save_tensor_model(self,model, tensor_model_name):
        model_json = model.to_json()
        with open(ML_FILE_PATH+tensor_model_name+".json", "w") as json_file:  # 학습된 모델저장
            json_file.write(model_json)
        model.save_weights(ML_FILE_PATH+tensor_model_name+".h5")  # 가중치저장

    def learning_tensor_model(self, layer_units_list, epochs_count, model_name):
        """모델 생성 및 학습"""

        model = models.Sequential()
        input_layer_unit = [layer_units_list[0]]
        inter_layer_unit = layer_units_list[1:-1]
        output_layer_unit = [layer_units_list.pop()]

        model.add(layers.Dense(input_layer_unit.pop(), activation='relu', input_shape=(100,)))
        for inter_unit in input_layer_unit:
            model.add(layers.Dense(inter_unit, activation='relu'))
        model.add(layers.Dense(output_layer_unit.pop(), activation='sigmoid'))

        model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                      loss=losses.binary_crossentropy,
                      metrics=[metrics.binary_accuracy])

        model.fit(self.x_train, self.y_train, epochs=epochs_count, batch_size=500)

        self.save_tensor_model(model, model_name)
        return model

    def tensor_model_evaluate(self, model):
        return model.evaluate(self.x_test, self.y_test)

    def learning_decisionTree_model(self, model_name):
        dcf = DecisionTreeClassifier(max_depth=4)
        dcf.fit(self.x_train, self.y_train)
        self.save_as_pickle_file(model_name, dcf)
        return dcf

    def learning_randomForest_model(self, model_name):
        rcf = RandomForestClassifier(max_depth=4, n_estimators=100, max_features=1 )
        rcf.fit(self.x_train, self.y_train)
        self.save_as_pickle_file(model_name, rcf)
        return rcf

    def learning_linear_model(self, model_name):
        lcf = linear_model.LogisticRegression()
        lcf.fit(self.x_train,self.y_train)
        self.save_as_pickle_file(model_name, lcf)
        return lcf

    def learning_naive_bayes_model(self, model_name):
        ncf = GaussianNB()
        ncf.fit(self.x_train,self.y_train)
        self.save_as_pickle_file(model_name, ncf)
        return ncf
# tf_result=[]
# ###epochs###
# tm1=ModelByPumsa()
# tf_result.append(tm1.tensor_model_evaluate(tm1.learning_tensor_model([64,64,1],10,"tensor1")))
# tm2=ModelByPumsa()
# tf_result.append(tm2.tensor_model_evaluate(tm2.learning_tensor_model([64,64,1],20,"tensor2")))
# tm3=ModelByPumsa()
# tf_result.append(tm3.tensor_model_evaluate(tm3.learning_tensor_model([64,64,1],30,"tensor3")))
# tm4=ModelByPumsa()
# tf_result.append(tm4.tensor_model_evaluate(tm4.learning_tensor_model([64,64,1],50,"tensor4")))
# tm5=ModelByPumsa()
# ###units 숫자###
# tf_result.append(tm5.tensor_model_evaluate(tm5.learning_tensor_model([16,16,1],20,"tensor5")))
# tm6=ModelByPumsa()
# tf_result.append(tm6.tensor_model_evaluate(tm6.learning_tensor_model([64,64,1],20,"tensor6")))
# tm7=ModelByPumsa()
# tf_result.append(tm7.tensor_model_evaluate(tm7.learning_tensor_model([128,128,1],20,"tensor7")))
# ###레이어 층수###
# tm8=ModelByPumsa()
# tf_result.append(tm8.tensor_model_evaluate(tm8.learning_tensor_model([64,32,32,1],20,"tensor8")))
# tm9=ModelByPumsa()
# tf_result.append(tm9.tensor_model_evaluate(tm9.learning_tensor_model([64,32,32,32,32,1],20,"tensor9")))
#
# fp=open(ML_FILE_PATH+"tensor_result_sample.txt","w")
# fp.write(str(tf_result))
# fp.close()

# ml1=ModelByPumsa()
# ml1.learning_decisionTree_model("decisiontree")
# ml2=ModelByPumsa()
# ml2.learning_randomForest_model("randomforest")
# ml3=ModelByPumsa()
# ml3.learning_linear_model("linear")
# ml4=ModelByPumsa()
# ml4.learning_naive_bayes_model("naive_bayes")
