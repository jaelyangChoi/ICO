from DAO import *
from DTO import *

dao = DatabaseDAO()
"""
# 데이터 입력 확인 테스트
data = CommentDataForInsert()

text = input('input text : ')
data.setText(text)

propriety = int(input('input propriety : '))
data.setPropriety(propriety)

learning = int(input('input learning : '))
data.setLearning(learning)

URL = input('input URL : ')
data.setURL(URL)

writer = input('input writer : ')
data.setWriter(writer)

dao.insertComment(data)

# url 별 댓글 검색 테스트
url = 'url2'
cnt = 1

dataList = dao.selectCommentsByURL(url)

for i in dataList:
    print(str(cnt) + "번 데이터 :")
    cnt += 1

    print("comment index : " + str(i._index))
    print("text : " + i._text)
    print("propriety level : " + str(i._propriety))
    print("writer index: " + i._writer)
    print(i._time)

    print()

# id의 pw 검색 테스트
id = input('id : ')
pw = dao.selectUserPassword(id)
print('password : ' + pw)
"""

id = input('id : ')
keyword = input('input keyword : ')

"""
# 개인 키워드 입력 테스트
dao.insertPersonalKeyword(id, keyword)
"""

# 개인 키워드 삭제 테스트
dao.deletePersonalKeywords(id, keyword)

# 개인 키워드 검색 테스트
id = input('id : ')
keywordList = dao.selectPersonalKeywordsByUser(id)

cnt = 1
for i in keywordList:
    print(str(cnt) + 'th keyword : ' + i)
    cnt += 1