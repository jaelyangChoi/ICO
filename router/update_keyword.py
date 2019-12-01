from flask import Flask, Blueprint, render_template, request, jsonify

update_keyword_bp = Blueprint('update_keyword', __name__)

keywords = ['sibal', 'byungsin']

#이런 형식으로 함수 호출
def print_kw(str):
    print(str)

@update_keyword_bp.route('/update_keyword', methods=['POST'])
def update_keyword():
    keywords.append(request.form['keyword'])
    keywords_str = ', '.join(keywords)

    print_kw(keywords_str)

    return jsonify(keywords_str)