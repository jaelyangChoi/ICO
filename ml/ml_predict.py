from ml.ml_by_pumsa import predict_comment as pml
from ml.ml_by_pumsa import sub_predict_comment as sml
from ml.model_by_word import model as wml


class ModelCombine:
    def total_predict(self, comment):
        pumsa_ml = pml.CommentPredict()
        word_ml = wml.ModelByWord()
        sub_pumsa_ml = sml.CommentPredict()

        sub_pumsa_result = sub_pumsa_ml.predict(comment)
        pumsa_ml_result = str(pumsa_ml.predict(comment)[1])
        word_ml_result = str(word_ml.predict(comment)[0])

        print(pumsa_ml_result, sub_pumsa_result, sub_pumsa_ml.predict_score, word_ml_result)

        if pumsa_ml_result == sub_pumsa_result:
            return sub_pumsa_result

        else:
            if 0.6 < sub_pumsa_ml.predict_score < 0.8:
                return pumsa_ml_result
            else:
                return sub_pumsa_result
