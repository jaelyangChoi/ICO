from flask import Blueprint, request, jsonify, session

from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block.block import runBlockComment
from block.filtering import filtering

update_comment_bp = Blueprint('update_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()


# 임시 db
# comments = [{'userID': 'cjl', 'comment': 'test data', 'property':'+'}]
# keywords = ['sibal', 'byungsin']

# 입력받은 댓글 db에 업로드 후 리로드
@update_comment_bp.route('/update_comment', methods=['POST'])
def update_comment():
    # 입력된 댓글 추출
    new_comment = {'userID': 'cjl0701', 'comment': request.form['comment'], 'property': '+',
                   'url': 'http://localhost:5000/news'}

    # 댓글 적절성 판단
    result = runBlockComment(new_comment['comment'])
    new_comment['property'] = result

    # db에 댓글 insert
    flag = CommentDTO.set_insert_comment(new_comment)
    print(flag)
    flag = CommentDAO.insert_comment(CommentDTO)
    print(flag)

    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url('http://localhost:5000/news')
    # for comment in comments:
    #   print(comment.get_comment()) 반환 값 {'idx': 1, 'text': '왜구들이 미쳐 날뛰네', 'propriety': 0, 'ML_learning': 0, 'url': '', 'writer': '1', 'time': datetime.datetime(2019, 12, 2, 19, 5, 19)}

    # 필터링 서비스
    if session['mode'] == 'on':
        comments = filtering(comments)

    return jsonify(comments)
