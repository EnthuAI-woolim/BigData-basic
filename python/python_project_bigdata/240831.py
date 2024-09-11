''' 24 - 08 - 31 강의 자료 '''
from PyQt5.pylupdate_main import printUsage
from streamlit import header

path = 'W:/Study/BigData/KoreaIT/python/python_project_bigdata/pythonData/'

'''
주석 : 실행 결과에 영향을 미치지 않는 코드
-> 작성자의 코드에 대한 설명을 쓸 때 사용한다.

1. ''' ''' : 장문 주석
2. # : 한 줄 주석 -> 단축키 : Ctrl + /

shift + F10 : 실행 단축키
Shift 두번 : 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색
ctrl + D : 현재 줄을 아래 줄에 복사
ctrl + shift + 방향키 : 현재 줄 이동
'''

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
변수(variable) :  변하는 수

-> 다양한 값을 지닌 하나의 속성
-> 데이터 분석의 대상
'''

a = 1
# print(a)
b = 2
c = 3
d = 3.5

### 변수로 연산
# print( a + b )
# print(d * 5) # 파이썬에서 곱하기 기호는 * 이다.

### 여러 값으로 구성된 변수 생성
var1 = [1,2,3]
# print(var1)
var2 = [4,5,6]
# print(var1 + var2) # [] (리스트) 의 더하기 연산은 리스트를 연결해준다.

### 문자(string)로 된 변수 생성
'안녕하세요'
'문자열'
'he is'
'200' # 따옴표로 감싸진 숫자는 문자열의 기능을 한다.

str1 = 'a'
# print(str1)
str2 = 'text'
str3 = 'Hello World!'
str4 = ['a','b','c']
str5 = ['Hello!', 'World','is','good!']

###  문자 변수 결합
# print(str2 + str3) # 문자 변수의 더하기 연산은 문자열을 합쳐준다.
# print(str3 * 10) # 문자 변수의 곱셈은 문자열의 여러번 반복해준다.
# print(str2 + ' ' + str3) # 파이썬은 공백을 문자열로 인정한다.
# print(str3 + 2) # 문자로 된 변수로는 수치 연산을 할 수 없다.

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
함수(Function) : 값을 넣으면 특정한 기능을 수행해서 처음과 다른 값으로
                만드는 수

-> 입력을 받아서 출력을 내는 수
-> 기능을 수행하는 수
'''

a = [324,657,87]
# print(sum(a))

'''
내장 함수 : 파이썬을 설치하면 기본적으로 파이썬에 존재하는 기본 함수
'''
x = [1,2,3]
# print(sum(x)) # 합계 함수
# print(max(x)) # 최대값 함수
# print(min(x)) # 최소값 함수

x_sum = sum(x)
# print(x_sum)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
패키지(Package) : 여러 함수와 변수들의 꾸러미

패키지 설치 -> 패키지 로드 -> 함수 사용
'''

### 패키지 로드 - import
import seaborn # 시각화(그래프) 패키지
import matplotlib.pyplot as plt # 패키지 별명

var = ['a','a','b','c']

# seaborn.countplot(x=var) # 그래프를 생성하는 코드
# plt.show() # 그래프 출력 함수

### 패키지 약어 - import 패키지명 as 약어
import seaborn as sns

# sns.countplot(x=var)
# plt.show()

### seaborn 의 titanic 데이터로 그래프 생성
df = sns.load_dataset('titanic')
# print(df['class'])

# sns.countplot(data=df, x='class')
# plt.show()


## x축 class, alive 별 색구분 표현
# sns.countplot(data=df, x='class', hue='alive')
# plt.show()
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
모듈(Module) : 여러 패키지 함수들의 모임, .py의 확장자를 가지는 파일
'''

### 패키지명.모듈명.함수명() 으로 함수 사용하기
# import sklearn.metrics
# sklearn.metrics.accuracy_score()

### 모듈명.함수명() 으로 함수 사용하기
# from sklearn import metrics
# metrics.accuracy_score()

### 함수명()으로 함수 사용하기 - 사용할 함수가 정해져 있을 때
# from sklearn.metrics import accuracy_score
# accuracy_score()

### 약어 지정
# import sklearn.metrics as m
# m.accuracy_score() # m : metrics
# m.c
# m.get_scorer()

### 패키지 설치 - 파이썬에서 패키지 설치 명령어는 pip 다.
'''
Terminal -> command prompt -> pip install 패키지명 
'''
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
데이터 프레임(Data Frame)
-> 데이터를 다룰 때 가장 많이 사용하는 데이터 형태
-> 행과 열로 구성된 사각형 모양의 표
-> 데이터 크다 -> 행 또는 열이 많다.

1. '열'은 속성이다. -> 컬럼(Column) 또는 변수(Variable)로 불림.
2. '행'은 한 사람의 정보다. -> 로우(Row)또는 케이스(Case)로 불림.
'''
import pandas as pd # 데이터 분석 패키지

'''
딕셔너리(dict) : 중괄호 {} 로 감싸지며 key와 value의 쌍으로 구성되는 자료형
'''

df = pd.DataFrame({
    'name' : ['김지훈','이유진','박동현','김민지'],
    'english' : [90,80,60,70],
    'math' : [50,60,100,20]
})
# print(df)

### 특정 변수의 값 추출
# print(df['english'])

### 변수의 값으로 합계 구하기
# a = sum(df['english'])
# print(a)

### 변수의 값으로 평균 구하기
# eng_mean = sum(df['english'])/4
# eng_mean = a/4
# print(eng_mean)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
''' 외부 데이터 활용 '''
# 데이터가 존재하는 경로를 변수로 생성
path = 'W:/Study/BigData/KoreaIT/python/python_project_bigdata/pythonData/'

### 엑셀 파일 로드
df_exam = pd.read_excel(path + 'excel_exam.xlsx') # 경로 변수 활용
df_exam = pd.read_excel('C:/Data/excel_exam.xlsx')
# print(df_exam)

a = sum(df_exam['science']) / 20
# print('전교생 과학 점수 평균 :', a)

### len() 함수 활용 - 자료형의 길이를 구해주는 함수

x = [1,2,3,4,5,7,8,9,10,11,3,4,5,7,8,9,10,3,4,5,7,8,9,10
     ,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10
     ,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10
     ,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10
     ,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10,3,4,5,7,8,9,10]
# print(len(x)) # 변수 x 의 길이를 구해달라는 코드


### 영어 점수 합계를 행 개수로 나누기 - 영어 평균
a = sum(df_exam['english']) / len(df_exam)
# print(a)

### 엑셀 파일의 첫 번째 행이 변수명이 아닌 경우
df_exam_no = pd.read_excel(path + 'excel_exam_novar.xlsx', header=None)
# print(df_exam_no)

### 엑셀 파일에 시트가 여러개 있다면
df_exam_sh = pd.read_excel(path + 'excel_exam.xlsx', sheet_name='Sheet2')
# print(df_exam_sh)
df_exam_sh = pd.read_excel(path + 'excel_exam.xlsx', sheet_name=1)
'''파이썬에서는 숫자를 0부터 센다'''
# print(df_exam_sh)

### csv 파일 불러오기
df_csv = pd.read_csv(path + 'exam.csv')
# print(df_csv)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
''' 데이터 파악 '''

'''
- 데이터 파악 함수
1. head() : 앞 부분 출력
2. tail() : 뒷 부분 출력
3. shape : 행, 열 개수 출력
4**. info() : 변수 속성 출력
5**. describe() : 요약 통계량 출력 
'''

import pandas as pd
exam = pd.read_csv(path + 'exam.csv')
# print(exam)

### 데이터 앞 부분 확인
# print(exam.head()) # 앞에서부터 5개까지
# print(exam.head(15)) # 앞에서부터 15개까지

### 데이터 뒷 부분 확인
# print(exam.tail()) # 뒤에서부터 5개

### 데이터가 몇 행 몇 열인지 확인
# print(exam.shape)

### 변수 속성 파악
# print(exam.info())
'''
int64 : 정수
float64 : 실수
object : 문자
datetime64 : 날짜 시간(2014-01-06)

64 : 64비트
- 1비트로 두 개의 값을 표현이 가능
- int64 : 2^64 개의 정수로 표현이 가능
'''

### 요약 통계량
# print(exam.describe())
'''
std : 표준편차 -> 변수의 값들이 평균에서 떨어진 정도
25% : 1사분위수 -> 하위 25%(1/4) 지점에 위치하는 값
75% : 3사분위수 -> 하위 75%(3/4) 지점에 위치하는 값
'''

### mpg 데이터 파악
mpg = pd.read_csv(path + 'mpg.csv')
# print(mpg)

# print(mpg.info())
# print(mpg.describe())
# print(mpg.describe(include='all')) # 문자 변수 요약통계량 함께 출력

'''
unique : 고유값 빈도 -> 중복을 제거한 범주의 개수
top : 최빈값 -> 개수가 가장 많은 값 (제일 많이 등장한 값)
freq : 빈도 -> 최빈값의 개수
'''

'''
- 함수와 메서드의 차이

내장함수 : sum(), print()

패키지 함수 : pd.read_csv()

메서드(Method) : df.head() - 변수가 지니고 있는 함수 (스킬) 

어트리뷰트 : shape - 변수가 지니고 있는 값 (능력치)
'''

### 데이터 프레임의 변수명 수정
df_raw = pd.DataFrame({
    'var1' : [1,2,1],
    'var2' : [2,3,2]
})
# print(df_raw)

# 1. * 수정이 들어가기 전, 데이터의 복사본 생성
df_new = df_raw.copy()
# print(df_new)

# 2. 변수명 수정
df_new = df_new.rename(columns = {'var2':'v2'}) # var2 를 v2로 수정
# print(df_new)

### 파생변수 : 기존의 변수를 변형해서 만드는 새로운 변수
# print(mpg)
# print(exam)

exam['sum'] = exam['math'] + exam['english'] + exam['science']
# print(exam)
exam['mean'] = exam['sum']/3
# print(exam)

# print(mpg)
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
# print(mpg)

a = sum(mpg['total']) / len(mpg)
# print('미국 자동차의 평균 통합 연비 :',a)
### 파생 변수 - 조건문 활용
a = mpg['total'].describe()
# print(a)
# mpg['total'].plot.hist() # 히스토그램
# plt.show()
# print(mpg)

# 1. 합격 판정 변수 생성
import numpy as np # numpy : 파이썬에서 연산 관련된 함수들을 가지고 있는 패키지
mpg['test'] = np.where(mpg['total'] >= 20,'수입','수입X')
# 파생변수 = np.where(조건, 조건에 부합할 때 부여할 값, 조건에 부합하지 않을 때 부여할 값)
# print(mpg.head(20))

# 2. 빈도표로 합격 판정 자동차 수 확인
a = mpg['test'].value_counts() # 빈도표 생성 함수
# print(a)

### 중첩 조건문 활용 - 연비마다 등급 부여
'''
A 등급 : 통합 연비가 30 이상
B 등급 : 통합 연비가 20~29
C 등급 : 통합 연비가 20~15
D 등급 : 통합 연비가 15 미만
'''

# 1. 연비 등급 변수 생성
mpg['grade'] = np.where(mpg['total'] >= 30, 'A',
                        np.where(mpg['total'] >= 20, 'B',
                                 np.where(mpg['total'] >= 15,'C','D')))
# print(mpg.tail(20))

# 2. 빈도표와 막대그래프로 정리
# c = mpg['grade'].value_counts()
# print(c)

### 목록에 해당하는 행으로 변수 생성 - compact, subcompact, 2seater
'''
| (버티컬 바) -> 또는(or)을 의미하는 기호
'''
# print(mpg)
# print(mpg['category'].value_counts())
# np.where()에 여러 조건을 입력할 때는 각 조건에 괄호를 입력해야한다.
mpg['size'] = np.where((mpg['category'] == 'compact') |
                       (mpg['category'] == 'subcompact')|
                       (mpg['category'] == '2seater'), 'SMALL', 'LARGE')
# print(mpg['size'].value_counts())

## 1. df.isin() 활용
a = ['compact','subcompact','2seater']

mpg['size2'] = np.where(mpg['category'].isin(a), 'small','large')
# print(mpg['size2'].value_counts())