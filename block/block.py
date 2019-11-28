import hgtk
from flask import Blueprint, request, render_template, flash, redirect, url_for
from openpyxl import load_workbook, Workbook
from konlpy.tag import Okt
import difflib


def tokenize(comment):
    print("**품사 분리 시작**")
    okt = Okt()
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
        if hgtk.checker.is_hangul(comment[j]):
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


# String 일치함수

def filteringSynk(comment):
    _comment = ""
    load_wb = load_workbook("/Users/77520769/Documents/문해긔/기본키워드_분리3.xlsx", data_only=True)
    load_ws = load_wb['Sheet']
    block = 0

    print("**2차 필터링 시작**")
    for j in comment:
        _comment = hgtk.text.decompose(j).replace("ᴥ", "")
        for i in range(1, 824):
            matchRatio = difflib.SequenceMatcher(None, load_ws['A' + str(i)].value, _comment).ratio()

            if matchRatio > 0.75:
                print("기본 키워드: " + load_ws['A' + str(i)].value)
                print("댓글 내 단어: " + _comment)
                print("일치율: " + str(matchRatio * 100) + "%")
                block = block + 1
                break
        if block != 0:
            break
    if block != 0:
        return load_ws['A' + str(i)].value + " & " + _comment + str(matchRatio * 100) + "%"
    else:
        return "OK"
