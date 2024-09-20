''' 24 - 09 - 07 강의 자료 '''

path = 'W:/Study/BigData/KoreaIT/python/python_project_bigdata/pythonData/'

'''
1. 엑셀 파일 로드 함수 - read_excel(경로 + 파일명.확장자)

2. 경로 변수 -> 변수에 파일의 경로를 뜻하는 문자열을 지정

3. 패키지 로드
import pandas as pd
import numpy as np

4. 데이터 파악 함수
mpg.head()
mpg.tail()
mpg.shape
mpg.info() : 속성
mpg.describe() : 요약 통계량

'''

# ------------------------------------------------------------------------------------
''' 데이터 가공 - 전처리 , 다루기 쉽게 만들기 '''

'''
데이터 가공 함수

1. query() : 행 추출
2. 데이터프레임명[] : 열 추출
3. sort_values() : 정렬
4. groupby() :  집단별로 나누기
5. assign() : 변수 추가 (파생변수추가)
6. agg() : 통계치 구하기
7. merge() : 데이터 합치기 (열)
8. concat() : 데이터 합치기 (행)

- 접속 연산자 : . (도트 연산자)
'''

### 데이터 로드

path = 'W:/Study/BigData/KoreaIT/python/python_project_bigdata/pythonData/'

import pandas as pd
exam = pd.read_csv(path + 'exam.csv')
# print(exam)

### 조건에 맞는 데이터만 추출 : query()

# exam에서 nclass가 1인 경우만 추출
a = exam.query('nclass == 1')
# print(a)

# 1반이 아닌 경우
b = exam.query('nclass != 1')
# print(b)

## 초과, 미만, 이상, 이하 조건 걸기

# 수학 점수가 50점을 초과한 학생만 조회
a = exam.query('math > 50')
# print(a)

# 영어 점수가 50점 이상인 경우
b = exam.query('english >= 50')
# print(b)

## 여러 조건을 충족하는 행 추출

# 1반이면서 수학 점수가 50점 이상인 경우
a = exam.query('nclass == 1 & math >= 50') # & (and, 그리고) : 둘 다 만족할 때
# print(a)

# 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
b = exam.query('math >= 90 | english >= 90') # | (or, 또는) : 둘 중에 하나라도 만족할 때
# print(b)

## 목록에 해당하는 행 추출

# 1, 3, 5 반에 해당하면 추출
a = exam.query('nclass == 1 | nclass == 3 | nclass == 5')
# print(a)

a = exam.query('nclass in [1,3,5]')
# print(a)

### 문자 변수를 이용해서 조건에 맞는 행 추출
df = pd.DataFrame({
    's' : ['F','M','F','M'],
    'country' : ['Korea', 'China', "Japan", 'USA']
})
# print(df)

# 전체 조건에 따옴표, 추출할 문자에 큰 따옴표 사용 - 따옴표 구분 -> 문자열 구분
a = df.query('s == "F" & country == "Korea"')
a = df.query("s == 'F' & country == 'Korea'")
# print(a)

'''
- 파이썬에서 사용하는 기호

1. 논리 연산자
< : 작다
<= : 작거나 같다
== : 같다
!= : 같지 않다
| : 또는
& : 그리고
in : 매칭 확인 (포함 연산자)

2. 산술 연산자
+ , - : 더하기, 빼기
* : 곱하기
** : 제곱
/ : 나누기
// : 나눗셈의 몫
% : 나눗셈의 나머지
'''

### 변추 추출 - df[]
# print(exam['math'])

## 여러 변수 추출
a = exam[['nclass', 'math', 'science']]
# print(a)
# print(exam[['math']])
''' 
변수명을 [] 로 한 번 더 감싸주면 데이터 프레임으로 추출되고
    [] 를 한 번만 감싸주면 시리즈로 추출이 된다.             
'''

## 변수 제거 - drop()
a = exam.drop(columns='math') # 수학 점수 제거
# print(a)
b = exam.drop(columns=['math','science'])
# print(b)

## query와 [] 조합

# 1반인 학생만 추출한 다음 영어점수 추출
a = exam.query('nclass == 1')['english']
# print(a)

# 수학 점수가 50점 이상인 행만 추출한 다음에 id, math 추출
b = exam.query('math >= 50')[['id', 'math']]
# print(b)

# 수학 점수가 60점 이상이고 id, math 만 추출한 다음 앞 부분 5행 까지 추출
c = exam.query('math >= 60')[['id','math']].head()
# print(c)

# '''
# 코드 줄 바꿈 - 가독성을 위함
# 1. 명령어가 끝난 부분 뒤에 역슬래시(\) 입력 후에 Enter로 줄 바꿈
# 2. 스페이스바나 탭을 이용해서 간격을 띄우고 다음 명령어 입력
#  -> \ 뒤에 아무것도 입력하면 안됨 (주석x, 띄어쓰기x)
# '''

c_1 = exam.query('math >= 60') \
    [['id','math']] \
    .head()
# print(c_1)

### 순서대로 정렬 - df.sort_values()
a = exam.sort_values('math') # 수학점수 오름차순 정렬
# print(a)
b = exam.sort_values('math', ascending=False) # 수학점수 내림차순 정렬
# print(b)

## nclass, math 오름차순 정렬
a = exam.sort_values(['nclass', 'math'])
# print(a)

## 반은 오름차순, 수학점수는 내림차순으로 정렬
a = exam.sort_values(['nclass','math'], ascending=[True, False])
# print(a)

### 파생 변수 추가 - df.assign()

## 총점 변수 추가
a = exam.assign(total = exam['math'] + exam['english'] + exam['science'])
# print(a)
# print(exam)

## 여러 파생변수 한번에 추가
a = exam.assign(total = exam['math'] + exam['english'] + exam['science'],
                mean = (exam['math'] + exam['english'] + exam['science'])/3)
# print(a)

## df.assign 에 np.where 적용 - 조건
import numpy as np
a = exam.assign(test = np.where(exam['science'] >= 60, 'PASS', 'FAIL'))
# print(a)

## 추가한 변수 바로 활용
a = exam.assign(total = exam['math'] + exam['english'] + exam['science']) \
    .sort_values('total')
# print(a)

### 집단별로 요약 - df.groupby(), df.agg()

## 전체 요약 통계량(평균) 구하기
a = exam.agg(mean_math = ('math', 'mean')) # 맨 끝의 mean은 함수명이다. -> () 쓰지 않음.
# print(a)

## 집단별 요약 통계량 구하기 - 반 별 수학 평균
a = exam.groupby('nclass') \
    .agg(mean_math = ('math', 'mean'))
# print(a)

## 변수를 인덱스로 바꾸지 않기 - as_index = False
a = exam.groupby('nclass', as_index=False) \
    .agg(mean_math = ('math','mean'))
# print(a)

## 여러 요약 통계량 한 번에 구하기
a = exam.groupby('nclass') \
    .agg(mean_math = ('math','mean'), # 수학 평균
         sum_math = ('math','sum'), # 수학 총점
         median_math = ('math', 'median'), # 수학 중앙값
         n = ('nclass','count')) # 빈도 (학생 수)
# print(a)

'''
agg() 에 자주 사용하는 요약 통계량 함수
mean() : 평균
std() : 표준편차
sum() : 합계
median() : 중앙값
min(), max() : 최소값, 최대값
count() : 빈도(개수)
'''

## 집단을 나눈 다음 다시 하위 집단으로 나누기
mpg = pd.read_csv(path + 'mpg.csv')
# print(mpg)
# 제조 회사 및 구동 방식별 그룹화
a = mpg.groupby(['manufacturer', 'drv']) \
    .agg(mean_cty = ('cty','mean'))
# print(a)

'''
Q. 제조 회사별로 'suv' 자동차의 도시 및 고속도로 합산 연비 평균을 구해서 내림차순으로 정렬하고,
1~5위까지 출력
'''
# print(mpg)
result = mpg.query('category == "suv"') \
    .assign(total = (mpg['cty'] + mpg['hwy']) / 2) \
    .groupby('manufacturer') \
    .agg(mean_total = ('total', 'mean')) \
    .sort_values('mean_total', ascending=False) \
    .head()
# print(result)

### 데이터 합치기 - merge() , concat()

## 가로로 합치기
# 중간 고사
t1 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'midterm' : [60,80,70,90,85]
})

# 기말 고사
t2 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'final' : [70,83,65,95,80]
})
# print(t1)
# print(t2)
'''
1. pd.merge() 에 결합할 데이터 프레임명 나열
2. how = : 입력한 데이터 프레임을 어느쪽에 결합할 건지?
3. on : 데이터를 합칠 때 기준으로 삼을 변수명 입력
'''

# tt = pd.merge(t1, t2, how='left', on='id')
# print(tt)

## 다른 데이터를 활용해 변수 추가 - 매칭
name = pd.DataFrame({
    'nclass' : [1,2,3,4,5],
    'teacher' : ['kim', 'lee', 'pack', 'jung', 'choi']
})
# print(exam)
# print(name)

# nclass 기준으로 합쳐서 exam_new 에 할당
exam_new = pd.merge(exam, name, how='left', on = 'nclass')
# print(exam_new)

## 세로로 합치기
# 1. 오전 면접자 데이터 생성
group_a = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'test' : [60,80,70,90,80]
})

# 2. 오후 면접자 데이터 생성
group_b = pd.DataFrame({
    'id' : [6,7,8,9,10],
    'test' : [70,80,83,65,95]
})
# print(group_a)
# print(group_b)

## 데이터 합쳐서 group_all 에 할당
group_all = pd.concat([group_a, group_b])
# print(group_all)
''' 인덱스 중복이 보기 싫다면 ignore_index = False '''
group_all = pd.concat([group_a, group_b], ignore_index=True)
# print(group_all)

# ---------------------------------------------------------------------------------------
''' 데이터 정제 - 빠진 데이터, 이상한 데이터 제거 '''

'''
결측치 (Missing Value) : 누락된 값, 비어있는 값
- 데이터 수집 과정에서 발생할 오류로 포함될 가능성
- 함수가 적용되지 않거나 분석 결과가 왜곡되는 문제가 발생
- 데이터 분석 시 결측치 확인, 제거 후 분석
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    's' : ['M','F',np.nan,'M','F'],
    'score' : [5,4,3,4,np.nan]
})
# print(df) # 파이썬에서 결측치는 NaN 으로 표시가 된다.

# print(df['score'] + 1) # NaN 값이 있는 상태로 출력하면 출력 결과도 NaN

### 결측치 확인
# print(pd.isna(df))

### 결측치 빈도 확인
a = pd.isna(df).sum()
# print(a)

### 결측치 제거

# 1. 결측치가 있는 행을 제거
a = df.dropna(subset='score')
# print(a)

# 2. 여러 변수에 결측치가 없는 데이터 추출
a = df.dropna(subset=['s','score'])
# print(a)

# 3. 결측치가 하나라도 있으면 제거
'''
1. df.dropna() 에 아무 변수도 지정하지 x
2. 모든 변수에 결측치가 없는 행만 남김

-> 간편하긴 하지만 분석에 사용할 수 있는 데이터까지 제거가 될 수 있다.
-> 분석에 사용한 변수를 직접 지정해서 결측치 제거하는 방법 권장
'''
df_nomiss = df.dropna()
# print(df_nomiss)

### 결측치 대체
'''
- 결측치 적고 데이터가 크면 결측치 제거 후 분석 가능
- 데이터가 작고 결측치가 많다면 데이터 손실로 인해서 분석 결과 왜곡
- 결측치 대체법을 이용하면 보완 가능

-> 결측치 대채법 : 결측치를 제거하는 대신 다른 값을 채워넣는 방법
--> 대표값(평균, 최빈값 ..) 을 구해서 일괄 대체 
--> 통계 분석 기법으로 결측치의 예측값 추정 후 대체
'''

### 평균값으로 결측치 대체하기
exam = pd.read_csv(path + 'exam.csv')
exam.loc[[2,7,14], ['math']] = np.nan # 2,7,14 행의 math 에 NaN 할당
# print(exam)
# print(exam['math'].mean()) # 55.23529411764706

# df.fillna()로 결측치를 평균값으로 대체
exam['math'] = exam['math'].fillna(55)
# print(exam)
# print(exam.isna().sum()) # 대체 후 결측치 빈도 확인

'''
이상치 : 정상 범위를 크게 벗어난 값
- 실제 데이터 대부분 이상치 들어있다.
- 제거하지 않으면 분석 결과 왜곡되므로 분석 전에 제거가 필요
'''

### 이상치 제거 - 존재할 수 없는 값
# 논리적으로 존재할 수 없는 값이 있을 경우 결측치로 변환 후 제거
# ex) 성별 변수 1, 2 외에 3 이 있다면 3을 NaN 으로 변환

# 이상치가 있는 데이터 생성
df = pd.DataFrame({
    's' : [1,2,1,3,2,1],
    'score' : [5,4,3,4,2,7]
})
# print(df)

## 이상치 확인 - 빈도표 만들어서 존재할 수 없는 값이 있는지 확인
a = df['s'].value_counts(sort=False).sort_index()
# print(a)
a = df['score'].value_counts(sort=False).sort_index()
# print(a)

## 결측 처리 - NaN 부여 -> 성별이 3 이면 NaN 부여
df['s'] = np.where(df['s'] == 3, np.nan, df['s'])
# print(df)

# 만족도가 5점 이상이면 NaN을 부여
df['score'] = np.where(df['score'] > 5, np.nan, df['score'])
# print(df)

## 결측치를 제거 후 분석
result = df.dropna(subset=['s', 'score']) \
    .groupby('s') \
    .agg(mean_score = ('score', 'mean'))
# print(result)

### 이상치 제거 - 극단적인 값
'''
극단치(Outlier) : 논리적으로는 존재할 수 있지만 극단적으로 크거나 작은 값
- 극단치 존재하면 분석 결과 왜곡되기에 제거를 함
- 기준 정하기
    1. 논리적 판단(ex: 성인 몸무게 40 ~ 150 kg 벗어나면 매우 드물므로 극단치로 간주)
    2. 통계적 기준(ex: 상하위 0.3% 또는 +-표준편차 벗어나면 극단치로 간주)
    3. 상자 그림(Box plot) 을 사용해서 중심에서 크게 벗어난 값을 극단치로 간주

- 상자 그림 : 데이터의 분포를 상자모양으로 표현한 그래프
    1. 중심에서 멀리 떨어진 값을 점으로 표현 -> 이 점이 이상치가 되는 것.
    2. 상자 그림을 통해서 극단치 기준을 구할 수 있다.
'''

### 상자 그림
# print(mpg)

import seaborn as sns
import matplotlib.pyplot as plt
# sns.boxplot(data=mpg, y='hwy')
# plt.show()

## 1. 극단치 기준값 구하기
# 1-1. 1사분위수, 3사분위수 구하기
pct25 = mpg['hwy'].quantile(.25) # 1사분위수
# print('1사분위수 :',pct25)
pct75 = mpg['hwy'].quantile(.75) # 3사분위수
# print('3사분위수 :',pct75)

# 1-2. IQR 구하기 - 3사분위수에서 1사분위수 까지의 거리
iqr = pct75 - pct25
# print('IQR :',iqr)

# 1-3 하한, 상한 구하기 - 위 아래 1.5IQR 값을 더하거나 빼준 것
h = pct25 - 1.5*iqr # 하한
s = pct75 + 1.5*iqr # 상한
# print('하한 :', h)
# print('상한 :', s)

## 2. 극단치를 결측 처리
# 2-1. 고속도로 연비에서 4.5 ~ 40.5 를 벗어나면 NaN 부여
mpg['hwy'] = np.where((mpg['hwy'] < 4.5) | (mpg['hwy'] > 40.5),
                      np.nan, mpg['hwy'])
# 2-2 결측치 빈도 확인
a = mpg['hwy'].isna().sum()
# print(a) # 결측 처리가 3개가 되었다.

## 3. 결측치 제거하고 분석
result = mpg.dropna(subset=['hwy']) \
    .groupby('drv') \
    .agg(mean_hwy = ('hwy','mean'))
# print(result)

# -------------------------------------------------------------------------------------
'''
그래프 : 데이터를 보기 쉽게 그림으로 표현한 것
- 추세와 경향이 드러나 데이터의 특징을 쉽게 이해할 수 있다.
- 새로운 패턴 발견, 데이터의 특징을 잘 전달
- 다양한 그래프
    -> 2차원, 3차원 그래프
    -> 지도 그래프
    -> 네트워크 그래프
    -> 모션 차트
    -> 인터렉티브 그래프
    
seaborn 패키지 : 그래프를 만들 때 자주 사용되는 패키지
- 코드가 쉽고 간결함
'''

'''
산점도(Scatter Plot) : 데이터를 x축과 y축에 점으로 표현한 그래프
-> 나이와 소득처럼 연속값으로 된 두 변수의 관계를 표현할 때 사용
'''

mpg = pd.read_csv(path + 'mpg.csv')

# x축은 displ(배기량), y축은 hwy(고속도로 연비)를 나타낸 산점도 만들기
import seaborn as sns
# sns.scatterplot(data=mpg, x='displ', y='hwy')
# plt.show() # 배기량이 높으면 고속도로 연비가 안 좋은 경향이 있다.

# 축 범위를 설정 - x축 범위를 3-6 으로 제한
# sns.scatterplot(data=mpg, x='displ', y='hwy') \
#     .set(xlim=[3,6])
# plt.show()

# y축 범위도 10-30으로 제한
# sns.scatterplot(data=mpg, x='displ', y='hwy') \
#     .set(xlim=[3,6], ylim=[10,30])
# plt.show()

# 종류별로 표식 색깔 바꾸기 - 구동방식(drv) 별로 표식 색깔 다르게
# sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
# plt.show()

'''
막대 그래프(Bar Chart) : 데이터의 크기를 막대의 길이로 표현한 그래프
-> 성별 소득 차이처럼 집단 간 차이를 표현할 때 사용

1. 평균 막대 그래프
2. 빈도 막대 그래프
'''

### 평균 막대 그래프

# 1. 집단별 평균표 생성 (선행)
df_mpg = mpg.groupby('drv', as_index=False)\
    .agg(mean_hwy = ('hwy','mean'))
# print(df_mpg)
''' seaborn 으로 그래프를 만들려면 변수가 값으로 들어가야함.'''

# 2. 그래프 생성
# sns.barplot(data=df_mpg, x='drv',y='mean_hwy')
# plt.show()

# 3. 크기순으로 정렬
# 3-1. 데이터 프레임 정렬
# df_mpg = df_mpg.sort_values('mean_hwy', ascending=False)
# print(df_mpg)

# 3-2. 막대 그래프 생성
# sns.barplot(data=df_mpg, x='drv',y='mean_hwy')
# plt.show()

### 빈도 막대 그래프  : 값의 빈도를 막대 길이로 표현한 그래프
df_mpg = mpg.groupby('drv', as_index=False)\
    .agg(n = ('drv','count'))
# print(df_mpg)
''' 빈도 막대 그래프를 그릴때 빈도표를 만드는 작업을 생략 가능하다. '''

# 그래프 생성 - sns.countplot()
# sns.countplot(data=mpg, x='drv')
# plt.show()

### 선 그래프(Line Chart) : 데이터를 선으로 표현한 그래프
# -> 시간에 따라 달라지는 데이터를 표현할 때 사용
'''
시계열 데이터(time series data) : 일별 환율처럼 일정 시간을 간격을 두고 나열된 데이터
시계열 그래프 : 시계열 데이터를 선으로 표현한 그래프
'''
# economics 데이터 로드
economics = pd.read_csv(path + 'economics.csv')
# print(economics.head())

# 그래프 생성
# sns.lineplot(data=economics, x='date', y='unemploy')
# plt.show() # '연월일'을 나타낸 문자가 x 축에 여러번 겹쳐 표시되기 때문에 굵은 선으로 보임

## x축에 연도만 표시
# 1. 날짜 시간 타입 변수 생성 - datetime64
economics['date2'] = pd.to_datetime(economics['date'])

# 2. 변수 타입 확인
# print(economics.info())
# print(economics[['date', 'date2']])

# 3. 연, 월, 일 추출
# print(economics['date2'].dt.year)
# print(economics['date2'].dt.month)
# print(economics['date2'].dt.day)

# 4. 연도만 추출해서 새로운 연도 변수 생성
economics['year'] = economics['date2'].dt.year
a = economics.head()
# print(a)

# 5. x 축에 연도 표시
# sns.lineplot(data=economics, x='year', y='unemploy')
# plt.show()

# 6. 신뢰구간 제거
# sns.lineplot(data=economics, x='year', y='unemploy', errorbar=None)
# plt.show()

### 상자 그림 (Box plot) : 데이터의 분포 또는 퍼져있는 형태를 직사각형 상자 모양으로 표현한 그래프
# - 데이터가 어떻게 분포가 되어있는지 알 수 있다.
# - 평균값만 볼 때보다 데이터의 특징을 더 자세히 알 수 있다.

## 상자 그림 생성
# sns.boxplot(data=mpg, x='drv', y='hwy')
# plt.show()
'''
전륜구동(f)
- 26 ~ 29 사이의 좁은 범위에 자동차가 모여있다.
- 수염의 위아래에 점 표식이 있으므로 연비가 
  극단적으로 높거나 낮은 자동차들이 있다.

4륜구동(4)
- 17 ~ 22 사이에 자동차가 대부분 모여있다.
- 중앙값이 상자 밑면에 가까우므로 낮은 값 쪽으로
  치우친 형태의 분포
'''

'''
Q . category(자동차 종류)가 'compact', 'subcompact', 'suv' 인 자동차들의 cty(도시연비)가
    어떻게 다른지 비교하는 상자그림을 만들어 보세요.
'''
# compact, subcompact, suv 차종 추출
df = mpg.query('category in ["compact","subcompact","suv"]')
# print(df.tail(20))

# 상자 그림 만들기
sns.boxplot(data=df, x='category', y='cty')
plt.show()


