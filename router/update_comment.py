from flask import Flask, Blueprint, render_template, request, jsonify

update_comment_bp = Blueprint('update_comment', __name__)

#댓글 받아서 필터링 함수 호출->return값을 DB에 전달하고 웹에 전달

#임시 db
comments = [{'userID': 'cjl', 'comment': 'test data'}]

def print_cm(str):
    print(str)

@update_comment_bp.route('/update_comment', methods=['POST'])
def update_comment():
    new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
    print_cm(new_comment) #임시 테스트
    comments.insert(0, new_comment) #이 과정 대신에 DB에 댓글 입력
    #받은 리턴값을 DB에 보냄
    #DB에서 댓글 전체 가져옴
    #만약 개인 필터링 모드가 on 이라면
    global mode
    print(mode, 'in bp')

      #개인 키워드를 DB에서 가져오고
     #3차 필터링 함수 호출하여 comments에 담음

    return jsonify(comments)



# @view_blueprint.route('/googleCallback')
# @view_blueprint.route('/')
# def index():
#     print(view_blueprint.root_path)
#     return render_template('index.html')
#
#
# @view_blueprint.route('/news')
# def news():
#     #posts = Post.query.all()
#     return render_template('news1.html')
#     #return "hello"
