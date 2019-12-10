import numpy as np  # 행렬, 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import pandas as pd
import time

ML_FILE_PATH = "../../dataset_pumsa_ml/"

df=pd.read_csv(ML_FILE_PATH+"compare_correct.csv")
answer=df['answer'].tolist()
tensor1=df['tensor1'].tolist()
tensor2=df['tensor2'].tolist()
tensor3=df['tensor3'].tolist()
tensor4=df['tensor4'].tolist()
tensor5=df['tensor5'].tolist()
tensor6=df['tensor6'].tolist()
tensor7=df['tensor7'].tolist()
tensor8=df['tensor8'].tolist()
tensor9=df['tensor9'].tolist()
i=0
count=0
print("1000개중 일치 개수")
while i<len(answer):
    if answer[i]==tensor1[i]:
        count=count+1
    i+=1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor2[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor3[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor4[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor5[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor6[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor7[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor8[i]:
        count=count+1
    i += 1
print(count)
i=0
count=0
while i<len(answer):
    if answer[i]==tensor9[i]:
        count=count+1
    i += 1
print(count)