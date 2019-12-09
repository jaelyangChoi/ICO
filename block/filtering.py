from flask import Blueprint, session

from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block import block

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
        comments = block.privateKeywordMatch(comments, keywords)  # 딕셔너리 리스트 받음
    # 부적절한 댓글 가리기
    conceal_bad_comment(comments)
    return comments


# 부적절한 댓글 가리기
def conceal_bad_comment(comments):#딕셔너리 리스트
    for comment in comments:
        if comment['property'] == '-':
            comment['comment'] = '부적절한 댓글입니다.'
