from ml.ml_by_pumsa import sub_predict_comment as sml
from ml.model_by_word import model as wml


class ModelCombine:
    def total_predict(self, comment):
        word_ml = wml.ModelByWord()
        sub_pumsa_ml = sml.CommentPredict()

        sub_pumsa_result = sub_pumsa_ml.predict(comment)
        word_ml_result = str(word_ml.predict(comment)[0])

        if word_ml_result == sub_pumsa_result:
            return sub_pumsa_result

        else:
            if 0.5 < sub_pumsa_ml.predict_score < 0.7:
                return word_ml_result
            else:
                return sub_pumsa_result
