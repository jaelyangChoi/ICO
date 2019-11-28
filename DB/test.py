from DAO.keyword import *
from DAO.comment import *
from DTO.comment import *
"""
cdao = CommentDAO()
kdao = KeywordDAO()

print('댓글 입력')
data = Comment()

text = input('input text : ')
data.set_text(text)

propriety = int(input('input propriety : '))
data.set_propriety(propriety)

learning = int(input('input learning : '))
data.set_learning(learning)

URL = input('input URL : ')
data.set_url(URL)

writer = input('input writer : ')
data.set_writer(writer)

cdao.insert_comment(data)
print()

print('url 댓글 검색')
url = input('input URL : ')
cnt = 1

data_list = cdao.select_comments_by_url(url)

print()

for i in data_list:
    print("<" + str(cnt) + ">" + "번 데이터 :")
    cnt += 1

    print("comment index.html : " + str(i._index))
    print("text : " + i._text)
    print("propriety level : " + str(i._propriety))
    print("writer index.html: " + i._writer)
    print(i._time)

    print()

print('개인 키워드 입력')
id = input('id : ')
keyword = input('input keyword : ')

kdao.insert_personal_keyword(id, keyword)

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = kdao.select_personal_keywords_by_user(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()

print('개인 키워드 삭제')
id = input('id : ')
keyword = input('input keyword : ')

kdao.delete_personal_keyword(id, keyword)

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = kdao.select_personal_keywords_by_user(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()
"""

url = input("URL : ")
url_dao = UrlDAO()
print("index : " + str(url_dao.select_index(url)))

print()

user = input("Id : ")
user_dao = UserDAO()
print("index : " + str(user_dao.select_index(user)))

