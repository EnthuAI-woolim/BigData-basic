''' 24 - 09 - 28 강의 자료 '''

''' 웹 크롤링 - 특정 사이트에서 원하는 정보를 가져오는 행위 

- HTML : 화면상에 보이는 웹 페이지 어떤 구조인지 브라우저로 알 수 있도록 하는 마크업 언어

- HTML 
<!DOCTYPE html>
<html>
<head>
    <meta charset = "UTF-8">
    <title> 웹 페이지 제목 <title>
<head/>
<body>
    <h1> 안녕하세요. <h1/>
    <div class='container'> HTML <div/>
<body/>
<html/>

- URL : 주소, 어떤 자원의 위치를 표기하는 방법
'''

### 1. 일반 웹 페이지 정보 가지고 오기 ( 전부 다 들고오기 )
# import requests
#
# url = 'https://www.naver.com/'
# response = requests.get(url)
# print(response.text)

### 2. 검색 결과 페이지 가지고 오기
# import requests
#
# url = 'https://search.naver.com/search.naver'
# param = {'query' : '파이썬'}
# response = requests.get(url, params=param)
# print(response.text)

### 3. 영화 기생충 크롤링
# import requests
#
# url = 'https://serieson.naver.com/v2/movie/367270'
# response = requests.get(url)
# print(response.text)
''' 저작권이 부여된 페이지는 크롤링이 어렵다. '''

''' BeautifulSoup 모듈 : 웹 페이지 정보 객체를 생성해주는 모듈 '''

### 1. 객체 생성
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94+%EA%B8%B0%EC%83%9D%EC%B6%A9+%EC%A0%95%EB%B3%B4'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
''' 파싱 : 컴퓨터에서 컴파일러 또는 번역기가 원시 부호를 기계어로 번역하는 과정의 한 단계 '''
'''
BeautifulSoup 메소드 사용법
1. find() : 지정된 태그<>들 중에서 가장 첫 번째 태그만 가져오는 메소드
2. find_all() : 지정한 태그를 전부 가져오는 메소드
3. 클래스 속성 활용
    1) soup.find_all('div', class_='gnd')
4. id 속성 활용
    1) soup.find('div', id='left')
'''

### 영화 바람 감상평 크롤링 - 시네24 - 사용자 리뷰는 크롤링 x
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://watcha.com/contents/mLOP7lW'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup)
#
# review_list = soup.find_all('p')
# print(review_list)


#main_pack > div.sc_new.cs_common_module.case_empasis.color_13._au_movie_content_wrap > div.cm_content_wrap > div > div > div:nth-child(3) > div.lego_review_list._scroller > ul > li:nth-child(1) > div.area_review_content > div > span
# <span class="desc _text">모든영화를 통틀어서 이렇게 많이 본 영화는 없을거다고 생각합니다 </span>
# <div class="area_text_expand _ellipsis" style="max-height:7.2rem;" data-ellipsis-managed="0" data-ellipsis-omitted="false" data-ellipsis-row="1">
# 			      <span class="desc _text">모든영화를 통틀어서 이렇게 많이 본 영화는 없을거다고 생각합니다 </span>
# 			      <button onclick="tCR('a=nco_x0a*A.tabreviewmore&amp;r=1&amp;i=1800009D_0000001AAC25');" type="button" class="story_more _tail" style="display:none;"><span class="blind">펼쳐보기</span></button>
# 			    </div>

### 날씨 요약 프로그래밍 - 네이버 날씨

# import datetime # 시간 관련
# from bs4 import BeautifulSoup
# import urllib.request
#
# ### 현재 시간을 출력하고 본인 스타일에 맞게 출력문 수정
# now = datetime.datetime.now() # 현재 시각
# nowDate = now.strftime('%Y년 %m월 %H시 %M분 입니다.')
# # print(nowDate)
# print('■'*100)
# print('\t\t\t\t\t\t\t\t ※ 현재 날씨 크롤링 프로그램 ※') # \t : 들여쓰기 1칸을 뜻하는 정규 표현식
# print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ID:ywladmin')
# print('■'*100)
#
# print('반갑습니다,','현재 시간은',nowDate,'\n') # \n : 줄 바꿈을 뜻하는 정규 표현식
# print(" Let Me Summarize Today's Info \n")
#
# print('# 오늘의 # 날씨 # 요약 \n')
# ### 서울 날씨
# url_s = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&tqi=iYPcDsqo15VssjAIXwdssssstF8-158740'
# webpage_s = urllib.request.urlopen(url_s)
# soup_s = BeautifulSoup(webpage_s, 'html.parser')
# temps_s = soup_s.find('strong', '') # 온도
# cast_s = soup_s.find('p', 'summary') # 날씨
# print(' 서울 날씨\n {}\n {}\n'.format(temps_s.get_text(), cast_s.get_text())) # get_text() : 해당 태그안에서 문자열만 가져오는 함수
#
# ### 부산 날씨
# url_b = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=iYP5IlqVN8ossa%2Fiu5Cssssst%2FK-282901'
# webpage_b = urllib.request.urlopen(url_b)
# soup_b = BeautifulSoup(webpage_b, 'html.parser')
# temps_b = soup_b.find('strong','') # 온도
# cast_b = soup_b.find('p','summary') # 날씨
# print(' 부산 날씨\n {}\n {}\n'.format(temps_b.get_text(), cast_b.get_text())) # get_text() : 해당 태그안에서 문자열만 가져오는 함수
#
# ### 제주 날씨
# url_j = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%A0%9C%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&tqi=iYP7Cwqo1awssnVxBSRssssssxl-375275'
# webpage_j = urllib.request.urlopen(url_j)
# soup_j = BeautifulSoup(webpage_j, 'html.parser')
# temps_j = soup_j.find('strong','') # 온도
# cast_j = soup_j.find('p','summary') # 날씨
# print(' 제주 날씨\n {}\n {}\n'.format(temps_j.get_text(), cast_j.get_text())) # get_text() : 해당 태그안에서 문자열만 가져오는 함수


'''
머신 러닝 모델 만들기 = 함수 만들기

    예측 변수(성별, 나이, 음주여부...) -> 모델 -> 타겟 변수(당뇨병 yes/no)

예측변수 : 예측하는 데 활용하는 변수 또는 모델에 입력하는 값
타겟변수 : 예측을 하고자 하는 변수 또는 모델이 출력하는 값

- 의사결정나무 - tree
1. 구조가 단순하다
2. 작동 원리를 이해하기 쉽다. -> 여러 분야에서 사용
3. 규모가 크고 복잡한 모델의 기반이 된다.
'''
import numpy as np
import pandas as pd

path = 'C:/Data/'
df = pd.read_csv(path + 'adult.csv')
# print(df.info())

### 타겟 변수 전처리 - income

# print(df['income'].value_counts(normalize=True)) # normalize : 범주의 비율을 생성해주는 옵션

df['income'] = np.where(df['income'] == '<=50K', 'low', 'high')
# print(df['income'].value_counts(normalize=True))

### 불필요한 변수 제거
df = df.drop(columns='fnlwgt')

### 문자 타입 변수를 숫자 타입으로 바꾸기 -> 모델에 활용하기 위해
'''
원-핫 인코딩 : 변수의 범주가 특정 값이면 1, 그렇지 않으면 0으로 바꾸는 방법 (성별, 결혼 여부, 자가 여부...)

    강아지 고양이 앵무새
    1     0     0
    0     1     0
    0     0     1
'''
df_tmp = df[['sex']]
# print(df_tmp.info())
# print(df_tmp['sex'].value_counts()) # 남자가 여성의 2배 정도

'''
pd.get_dummies() 에 데이터 프레임을 넣어 주면 문자 타입 변수를 원-핫 인코딩으로 적용
'''
df_tmp = pd.get_dummies(df_tmp) # 성별 원-핫 인코딩
# print(df_tmp.info())

a = df_tmp[['sex_Female', 'sex_Male']].head()
# print(a)
target = df['income']

df = df.drop(columns='income') # 타겟 변수인 income 만 제거
df = pd.get_dummies(df) # 모든 문자 타입 변수 원핫 인코딩

df['income'] = target
# print(df.info(max_cols = np.inf))

### 데이터 분할
'''
모델을 만들 때는 가지고 있는 모든 데이터를 사용하는게 아니라 일부만 무작위로 추출해서
사용을 해야 한다.

1. 모든 데이터를 사용해서 모델을 만들면 성능 평가 점수를 신뢰할 수 없다.
2. 크로스밸리데이션(교차 검증) : 신뢰할 수 있는 성능 평가 점수를 얻는 방법
    -> 일부는 모델을 만들때 사용하고, 나머지는 평가할 때 사용하는 방법
    1. 트레이닝 세트 : 훈련용, 모델을 만드는데 사용
    2. 테스트 세트 : 시험용, 성능을 평가하는데 사용
'''

### adult 데이터 분할
''' scikit-learn 패키지 : 머신 러닝 모델을 만들 때 가장 많이 사용되는 패키지 '''
from sklearn.model_selection import train_test_split # 데이터를 나눌 때 쓰는 함수
df_train, df_test = train_test_split(df,
                                     test_size=0.3, # 테스트 세트의 비율
                                     stratify=df['income'], # 타겟 변수 비율 유지
                                     random_state=1234) # 난수 고정
## train
# print(df_train.shape) # 행과 열의 갯수를 알려줌
# print(df_train['income'].value_counts(normalize=True))

## test
# print(df_test.shape)
# print(df_test['income'].value_counts(normalize=True))

### 의사결정나무 모델 생성

# 1. 모델 설정
from sklearn import tree

clf = tree.DecisionTreeClassifier(random_state=1234,
                                  max_depth=3) # 나무의 깊이
'''
의사결정나무 알고리즘은 타겟 변수를 가장 잘 분리해주는 예측 변수를 선택해서 노드를 분할한다.
그런데 여러 예측변수가 똑같이 타겟변수를 잘 분리하는 경우가 있다. 이럴때는 난수를 이용해서
무작위로 예측변수를 선택하기 때문에 코드를 실행할 때마다 결과가 조금씩 달라진다. 그래서
코드를 여러번 실행해도 항상 같은 결과가 나오게 하려면 난수를 고정해야한다.
'''

# 2. 모델 만들기
train_x = df_train.drop(columns = 'income') # 예측 변수 추출
train_y = df_train['income'] # 타겟 변수 추출

model = clf.fit(X=train_x, y=train_y) # 모델이 트레인 데이터를 받아서 만들어지는 코드

# 3. 모델 구조 확인
import matplotlib.pyplot as plt
plt.rcParams.update({
    'figure.figsize':[12,8],
    'figure.dpi':100
})

tree.plot_tree(model,
               feature_names=train_x.columns, # 예측 변수명
               class_names=['high','low'], # 타겟 변수 클래스, 알파벳 순
               proportion=True, # 비율 표기 여부
               filled=True, # 색칠
               rounded=True, # 둥근 테두리
               impurity=False, # 불순도 표시 여부
               label='root', # lable 표시 위치
               fontsize=15) # 글자 크기
# plt.show()
# 모델 구조도에서 아래쪽에서 고려되는 변수들이 크게 영향을 끼치는 변수들로 분류됨


### 모델을 이용해서 예측
test_x = df_test.drop(columns = 'income') # 테스트 예측 변수
test_y = df_test['income'] # 테스트 타겟 변수

# 1. 예측값 구하기
df_test['pred'] = model.predict(test_x)
# print(df_test)

### 성능 평가

# 1. confusion matrix : 모델이 예측한 값 중 맞는 경우와 틀린 경우의 빈도를 나타낸 혼동 행렬
'''
sklearn.metrix 의 confusion_matrix() 사용
    1) y_true : 타겟 변수
    2) y_pred : 예측 변수
    3) labels : 클래스 배치 순서
'''
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_true=df_test['income'], # 실제 데이터
                            y_pred=df_test['pred'], # 예측 값
                            labels=['high','low']) # 배치 순서
# print(conf_mat)

plt.rcParams.update(plt.rcParamsDefault) # 위에서 설정한 그래프 설정 초기화

from sklearn.metrics import ConfusionMatrixDisplay
p = ConfusionMatrixDisplay(confusion_matrix=conf_mat, # 컨퓨전 메트릭스
                           display_labels=('high','low')) # 타겟 변수 클래스명
p.plot(cmap='Blues') # 컬러맵 적용 출력
plt.show()

### 성능 평가 지표 - Accuracty(정확도) : 모델이 예측해서 맞춘 비율
import sklearn.metrics as metrics
ac = metrics.accuracy_score(y_true=df_test['income'],
                            y_pred=df_test['pred'])
# print('정확도:', ac)

### 성능 평가 지표 - Precision(정밀도) : 모델이 관심 클래스를 예측해서 맞춘 비율
pr = metrics.precision_score(y_true=df_test['income'],
                             y_pred=df_test['pred'],
                             pos_label='high') # 관심 클래스
# print('정밀도 :',pr)

### 성능 평가 지표 - Recall(재현율) : 모델이 실제 데이터에서 관심 클래스를 찾아낸 비율
rc = metrics.recall_score(y_true=df_test['income'],
                          y_pred=df_test['pred'],
                          pos_label='high')
# print('재현율 :', rc)

### 성능 평가 지표 - F1 score : 정밀도와 재현율이 둘 다 중요할 때
f1 = metrics.f1_score(y_true=df_test['income'],
                      y_pred=df_test['pred'],
                      pos_label='high')
# print(f1)

