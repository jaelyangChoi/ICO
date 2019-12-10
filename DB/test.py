from DAO.comment import *
from DAO.defaultKeyword import *
from DAO.personalKeyword import *
from DAO.user import *

cdao = CommentDAO()
pkdao = PersonalKeywordDAO()
"""
print('댓글 입력')
data = Comment()

data.set_comment(input('input text : '))
data.set_property('+')
data.set_learning(0)
data.set_url('/news')
cdao.insert_comment(data, 1)

print('\nurl 댓글 검색')
url = '/news'
data_list = cdao.select_comments_by_url(url)

print()

for i in data_list:
    print("\n<index : " + str(i.get_index()) + ">")
    print("comment : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id : " + i.get_user_id())
    print(i.get_time())

print('\n댓글 삭제')
cdao.delete_comment(4)

data_list = cdao.select_comments_by_url(url)
for i in data_list:
    print("\n<index : " + str(i.get_index()) + ">")
    print("comment : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id : " + i.get_user_id())
    print(i.get_time())

print('\n개인 키워드 입력')
pkdao.insert_keyword(1, input('input keyword : '))

print('\n개인 키워드 검색')
keyword_list = pkdao.select_keywords(1)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()

print('개인 키워드 삭제')
pkdao.delete_keyword(1, input('input keyword : '))

print('\n개인 키워드 검색')
keyword_list = pkdao.select_keywords(1)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()
"""

user = UserDAO()
print(user.is_existing_email('any980418@gmail.com'))
