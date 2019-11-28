import hgtk
from flask import Blueprint, request, render_template, flash, redirect, url_for
from openpyxl import load_workbook, Workbook
from konlpy.tag import Okt
import difflib
import pymysql

def tokenize(comment):
    print("**품사 분리 시작**")
    okt=Okt()
    return [t for t in okt.nouns(comment)]
# 품사분리함수

def StringMatch(comment):

    load_wb = load_workbook("/Users/77520769/Documents/문해긔/공용keyword-3.xlsx", data_only=True)
    load_ws = load_wb['Sheet1']
    block = 0
    _comment = ""
    print("**1차 필터링 시작**")

    for j in range(0, len(comment)):
        # 댓글 길이만큼 for문
        if hgtk.checker.is_hangul(comment[j]) | comment == ' ':
            _comment += comment[j]
        #     코멘트 한글자마다 한글인지 파악
        #     한글일 경우 새 String인자에 추가
        else:
            continue
        #      한글이 아니면 추가X

    print(_comment)

    for i in range(1, 1103):
        # 차단 키워드 갯수만큼 for문
        if _comment.find(str(load_ws['A' + str(i)].value)) != -1:
            block = block + 1
            print("매치된 기본 키워드: " + load_ws['A' + str(i)].value)
            break
    #    한글 이외의 것을 제거한 댓글과 키워드 매치
    if block != 0:
        return load_ws['A' + str(i)].value
    else:
        return "OK"
#String 일치함수


def filteringSynk(comment):
    _comment = ""
    load_wb = load_workbook("/Users/77520769/Documents/문해긔/기본키워드_분리3.xlsx", data_only=True)
    load_ws = load_wb['Sheet']
    block = 0

    print("**2차 필터링 시작**")
    for j in comment:
        _comment = hgtk.text.decompose(j).replace("ᴥ", "")

        for i in range(1,824):
            matchRatio = difflib.SequenceMatcher(None,load_ws['A' + str(i)].value, _comment).ratio()

            if matchRatio > 0.75:
                print("기본 키워드: " + load_ws['A' + str(i)].value)
                print("댓글 내 단어: " + _comment)
                print("일치율: " + str(matchRatio*100) + "%")
                block = block + 1
                break
        if block !=0:
            break
    if block !=0:
        return load_ws['A' + str(i)].value + " & " + _comment + str(matchRatio*100) + "%"
    else:
        return "OK"
#유사도판별함수


load_wb = load_workbook("/Users/77520769/Documents/문해긔/댓글 수집.xlsx", data_only=True)
load_ws = load_wb['시트1']
# 댓글 불러오기
write_wb = Workbook()
write_ws = write_wb.active
# 저장할 새 엑셀

##################엑셀 대신에 DB에서 욕 불러와야함#####################
##################체크도 DB에있는거랑 하기,댓글&키워드#################


for i in range(2,910):
    testComment = load_ws['A' + str(i)].value
    write_ws['A' + str(i)] = testComment
# 새 엑셀에 댓글 저장

    filtering1 = StringMatch(testComment)
    #1차 필터링~String일치로 판별

    if filtering1 == "OK":
        # 1차 성공시 2차 필터링 시작
        print("OK")
        testTokenComment = tokenize(testComment)
        print(testTokenComment)
        # 품사분리(명사만 추출)

        filtering2 = filteringSynk(testTokenComment)
        # 자모음 분리 후 2차 필터링

        if filtering2 == "OK":
            print(testComment)
            write_ws['B' + str(i)] = '2'
        # 2차도 OK면 클린
        else:
            write_ws['B' + str(i)] = '1'
            write_ws['C' + str(i)] = filtering2
            print("차단되었습니다.")

        # 2차에서 걸리면 중간
    else:
        write_ws['B' + str(i)] = '0'
        write_ws['C' + str(i)] = filtering1
        print("차단되었습니다.")

write_wb.save('/Users/77520769/Documents/문해긔/댓글필터링_new.xlsx')

# -----------------필터링메인----------------

