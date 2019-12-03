from ml.ml_by_pumsa import predict_comment as pml
from ml.model_by_word import model as wml


class ModelCombine:
    def total_predict(self, comment):
        pumsa_ml = pml.CommentPredict()
        word_ml = wml.ModelByWord()

        pumsa_ml_result = pumsa_ml.predict(comment)
        word_ml_result = word_ml.predict(comment)[0]

        print(pumsa_ml_result, word_ml_result, pumsa_ml.predict_score)

        if pumsa_ml_result == word_ml_result:
            return word_ml_result
        else:
            if 0.6 < pumsa_ml.predict_score < 0.7:
                return word_ml_result
            else:
                return pumsa_ml_result


