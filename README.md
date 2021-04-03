# ICO Service (Individual Custom cOmments)

개인 맞춤 댓글 필터링 서비스
>인터넷 악성 댓글을 차단하는 기존 서비스에 개인화 기능을 추가
<br>
   
   

## ICO service의 차별점
>기존보다 엄격한 필터링 서비스와 개인 맞춤 기능을 제공한다.  
#### 1. 엄격한 필터링  
 Machine Learning과 String 기반 유사도 알고리즘을 활용하여 보다 엄격한 필터링을 할 수 있도록 하였다.  
#### 2. 개인 맞춤 필터링  
 사용자로부터 키워드를 입력 받아 그를 바탕으로 필터링하는 기능을 제공한다.  
 ![그림3](https://user-images.githubusercontent.com/55947154/113479552-bb343e80-94ca-11eb-895d-408ea0e1d999.png)

<br>
   

## 시스템 전체 구조
![그림2](https://user-images.githubusercontent.com/55947154/113479550-b8d1e480-94ca-11eb-8516-b73b3912c630.png)
- 1차 필터링: 비속어 사전 기반 필터링   
- 2차 필터링: AI 학습 모델 기반 필터링   
- 3차 필터링: 개인 키워드 기반 필터링   

<br> 
   
## contributers
|직책|이름|
|:---:|:---:|
|팀장|최재량|
|팀원|김하경|
|팀원|송윤재|
|팀원|안나연|
|팀원|정혜원|




## 개발 환경
Language: python 3.7.x이상  
IDE: Pycharm  
Python framework: flask  
DB: Mysql  
ML: anaconda package  




### Running the tests

localhost:5000




### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

