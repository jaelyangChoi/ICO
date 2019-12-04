from DAO.comment import *
from DTO.comment import *
from DAO.default_keyword import *
from DAO.personal_keyword import *
from DAO.user import *

cdao = CommentDAO()
data = Comment()
dkdoa = DefaultKeywordDAO()
pkdao = PersonalKeywordDAO()
udao = UserDAO()
"""
print('댓글 입력')
data.set_comment(input('input comment : '))

data.set_property('+')
data.set_learning(0)
data.set_url('http://localhost:5000/news')
data.set_user_id('any980418')

cdao.insert_comment(data)

print()

print('url 댓글 검색')
url = 'http://localhost:5000/news'

data_list = cdao.select_comments_by_url(url)
for i in data_list:
    print("index : <" + str(i.get_index()) + ">")
    print("text : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id: " + i.get_user_id())
    print(i.get_time())

    print()

print('개인 키워드 입력')
id = 'any980418'
keyword = input('input keyword : ')

pkdao.insert_keyword(id, keyword)

id = 'any980418'

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = pkdao.select_keywords(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()

print('개인 키워드 삭제')
keyword = input('input keyword : ')

pkdao.delete_keyword(id, keyword)

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = pkdao.select_keywords(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1

print("none : " + str(udao.is_existing_email('none')))
print("any980418@naver.com : " + str(udao.is_existing_email('any980418@naver.com')))

print("return -1 : " + str(data.set_property('!')))

keyword_list = dkdoa.select_keywords()
cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1

keyword_list = dkdoa.select_split_keywords()
cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
"""

result = dkdoa.select_all()
for k in result:
    print(k.to_json())