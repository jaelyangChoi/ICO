from flask import Blueprint, session
from block import block
from DB.DAO.personal_keyword import PersonalKeywordDAO

from DB.DAO.comment import CommentDAO
from DB.DTO.comment import Comment

update_comment_bp = Blueprint('update_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()


# 댓글 필터링
def filtering(comments):
    user_info = session['info']
    # DB 에서 키워드 불러옴
    keywords = personal_keywordDB.select_keywords(user_info['id'])
    # 개인 키워드 기반 적절성 유무 판단
    if keywords:
        comments = block.privateKeywordMatch(comments, keywords)
    # 부적절한 댓글 가리기
    comments = conceal_bad_comment(comments)
    return comments


# 부적절한 댓글 가리기
def conceal_bad_comment(comments):
    for comment in comments:
        if comment.get_property() == '-':
            comment.set_comment('부적절한 댓글입니다.')

    return comments
