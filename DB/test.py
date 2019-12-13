from DAO.comment import *
from DAO.defaultKeyword import *
from DAO.personalKeyword import *
from DAO.user import *

cdao = CommentDAO()
pkdao = PersonalKeywordDAO()

print('댓글 입력')
data = Comment()

data.set_comment(input('input text : '))
data.set_property('+')
data.set_learning(0)
data.set_url('/news')
cdao.insert_comment(data, 1)
print()

print('url 댓글 검색')
url = '/news'
data_list = cdao.select_comments_by_url(url)

print()

for i in data_list:
    print("<index : " + str(i.get_index()) + ">")
    print("comment : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id : " + i.get_user_id())
    print(i.get_time())

    print()

print('댓글 삭제')
cdao.delete_comment(4)

data_list = cdao.select_comments_by_url(url)
for i in data_list:
    print("<index : " + str(i.get_index()) + ">")
    print("comment : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id : " + i.get_user_id())
    print(i.get_time())

    print()

"""
print('개인 키워드 입력')
id = input('id : ')
keyword = input('input keyword : ')

pkdao.insert_keyword(id, keyword)

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = pkdao.select_keywords(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()

print('개인 키워드 삭제')
id = input('id : ')
keyword = input('input keyword : ')

pkdao.delete_keyword(id, keyword)

print('\n<' + id + '>의 개인 키워드 검색')
keyword_list = pkdao.select_keywords(id)

cnt = 1
for i in keyword_list:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1
print()

url = input("URL : ")
url_dao = UrlDAO()
print("index : " + str(url_dao.select_index(url)))

print()

user = input("Id : ")
user_dao = UserDAO()
print("index : " + str(user_dao.select_index(user)))
"""
