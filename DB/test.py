from DAO.comment import *
from DTO.comment_ver_dic import *
from DAO.defaultKeyword import *
from DAO.personalKeyword import *
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
<<<<<<< HEAD
    print("index : <" + str(i.get_index()) + ">")
    print("text : " + i.get_comment())
    print("property : " + str(i.get_property()))
    print("user id: " + i.get_user_id())
    print(i.get_time())
=======
    print("<" + str(cnt) + ">" + "번 데이터 :")
    cnt += 1

    print("comment index.html : " + str(i._index))
    print("text : " + i._text)
    print("propriety level : " + str(i._propriety))
    print("writer index.html: " + i._writer)
    print(i._time)
>>>>>>> 90a197fbb809ba11af0865a3321d23bb960b81e7

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
