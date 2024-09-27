''' 24 - 09 - 21 강의 자료 '''

'''
1. 산점도
sns.scatterplot(data = mpg, x='displ', y='hwy')
1-1. 축 제한
sns.scatterplot(data = mpg, x='displ', y='hwy') \
.set(xlim = [3,6], ylim = [10,30])
1-2 종류별로 표식 색깔 변경
sns.scatterplot(data = mpg, x='displ', y='hwy', hue = 'drv')

2. 막대 그래프

2-1 평균표 생성
df_mpg = mpg.groupby('drv', as_index = False) \
        .agg(mean_hwy = ('hwy', 'mean'))
2-2 그래프 생성
sns.barplot(data=df_mpg, x='drv', y='mean_hwy')

3. 빈도 막대 그래프
sns.countplot(data=mpg, x='drv')

4. 선 그래프
sns.lineplot(data=economics, x='date', y='unemploy')

5. 상자 그림
sns.boxplot(data = mpg, x='drv', y='hwy')
'''

# ------------------------------------------------------------------------------------------
''' 한국복지패널 데이터 분석 
- 한국보건사회연구원 발간 조사 자료
- 전국 7천여 가구 선정, 2006년부터 매년 추적 조사한 자료
- 변수 개수가 1,000개 정도 (경제활동, 복지욕구, 생활실태 ... )
- 다양한 분야의 연구, 정책 전문가들이 활용
'''

### 데이터 로드 - .sav : 통계 분석 소프트웨어 spss 전용 파일
# 1. 패키지 설치 : pip install pyreadstat

### 사용할 패키지 로드
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

### 데이터 불러오기
path = 'C:/Data/'
raw_welfare = pd.read_spss(path + 'Koweps_hpwc14_2019_beta2.sav')

### 복사본 생성
welfare = raw_welfare.copy()
# print(welfare)
# print(welfare.info())
# print(welfare.describe())
# 규모가 이렇게 큰 데이터는 변수명을 쉬운 단어로 바꾸고 분석할 변수를 하나씩 살펴봐야 한다.

### 변수명 수정 - 코드북 참고
welfare = welfare.rename(columns={'h14_g3' : 's', # 성별
                                  'h14_g4' : 'birth', # 태어난 년도
                                  'h14_g10' : 'marriage_type', # 혼인 유무
                                  'h14_g11' : 'religion', # 종교
                                  'p1402_8aq1' : 'income', # 월급
                                  'h14_eco9' : 'code_job', # 직업 코드
                                  'h14_reg7' : 'code_region'}) # 지역 코드
'''
분석 절차
1단계 - 변수 검토 및 전처리
: 변수 특징 파악, 이상치와 결측치 정제, 변수값 수정,
2단계 - 변수 간 관계 분석
: 데이터 요약표, 그래프 시각화, 분석 결과 해석 (+ 텍스트 마이닝, 머신 러닝활용, 가설 검정....) 
'''

''' 성별에 따른 월급 차이 - 남 녀 누가 많이 벌까 ? '''
### 1. 성별 변수 검토

# 1-1. 검토 함수 적용
# print(welfare['s'].dtypes) # 변수 타입 출력
# a = welfare['s'].value_counts() # 빈도 구하기 - 이상치 x 확인
# print(a)

# 1-2. 성별에 이름을 부여
welfare['s'] = np.where(welfare['s'] == 1, 'Male', 'Female')
a = welfare['s'].value_counts()
# print(a)

# 1-3. 빈도 막대 그래프 생성
# sns.countplot(data=welfare, x='s')
# plt.show()

### 2. 월급 변수 검토 밎 전처리
# 2-1 변수 검토
a = welfare['income'].dtypes
# print(a)
a = welfare['income'].describe()
# print(a)
# sns.histplot(data=welfare, x='income') # 히스토그램 : 집단 확인
# plt.show()

# 2-2 전처리
# a = welfare['income'].describe()
# print(a)

# a = welfare['income'].isna().sum() # 결측치 확인
# print(a)

# 만약에 9999 값이 있다면 ? -> 이상치로 간주하고 결측 처리
# welfare['income'] = np.where(welfare['income'] == 9999, np.nan, welfare['income'])
# b = welfare['income'].isna().sum()
# print(b)

### 성별에 따른 월급 차이 분석 진행
# 1. 성별 월급표 생성
s_income = welfare.dropna(subset='income') \
    .groupby('s', as_index=False) \
    .agg(mean_income = ('income', 'mean'))
# print(s_income)

# 2. 시각화 - 막대
# sns.barplot(data=s_income, x='s', y='mean_income')
# plt.show()

''' 나이와 월급의 관계 - 몇 살에 가장 돈을 많이 버나 ? '''
# a = welfare['birth'].dtypes
# print(a)

a = welfare['birth'].describe()
# print(a)

# sns.histplot(data=welfare, x='birth')
# plt.show()

# 3. 전처리
a = welfare['birth'].describe() # 이상치 확인
# print(a)

a = welfare['birth'].isna().sum() # 결측치 개수 파악
# print(a)
welfare['birth'] = np.where(welfare['birth'] == 9999, np.nan, welfare['birth'])
a = welfare['birth'].isna().sum() # 결측치 개수 파악
# print(a)

# 4. 파생변수 생성 - 나이
welfare = welfare.assign(age = 2019 - welfare['birth'] + 1)
a = welfare['age'].describe()
# print(a)

### 나이와 월급의 관계 분석
# 1. 나이에 따른 월급 평균표 생성
age_income = welfare.dropna(subset='income') \
    .groupby('age') \
    .agg(mean_income = ('income','mean'))
# print(age_income.head(20))

# 2. 선 그래프 생성
# sns.lineplot(data=age_income, x='age', y='mean_income')
# plt.show()

''' 연령대에 따른 월급 차이 - 어떤 연령대의 월급이 가장 많을까 ? '''

### 연령대 변수 생성
welfare = welfare.assign(ageg = np.where(welfare['age'] < 30, 'young',
                                         np.where(welfare['age'] <= 59,'middle','old')))
# 빈도 구하기
a = welfare['ageg'].value_counts()
# print(a)

# 빈도 막대 그래프 생성
# sns.countplot(data=welfare, x='ageg')
# plt.show()

### 연령대에 따른 월급 차이 분석
# 1. 연령대별 월급 평균표 생성
ageg_income = welfare.dropna(subset='income')\
    .groupby('ageg', as_index=False)\
    .agg(mean_income = ('income','mean'))
# print(ageg_income)

# 2. 시각화 - 막대
# sns.barplot(data=ageg_income, x='ageg',y='mean_income')
# plt.show()

# 3. 막대 그래프 초,중,노 정렬
# sns.barplot(data=ageg_income, x='ageg',y='mean_income',
#             order=['young','middle','old'])
# plt.show()

''' 연령대 및 성별 월급 차이 - 성별 월급 차이는 연령대별로 다를까 ? '''
# 연령대 및 성별 평균표 생성
s_income = welfare.dropna(subset='income') \
    .groupby(['ageg', 's'], as_index=False) \
    .agg(mean_income = ('income', 'mean'))
# print(s_income)

# 막대 그래프 생성
# sns.barplot(data=s_income, x='ageg', y='mean_income', hue='s',
#             order=['young','middle','old'])
# plt.show()

''' 직업별 월급 차이 - 어떤 직업이 돈을 많이 벌까 ? '''
### 직업 변수 검토
# print(welfare['code_job'].dtypes)
a = welfare['code_job'].value_counts()
# print(a)

# 1. 전처리
list_job = pd.read_excel(path + 'Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
# print(list_job.head())

# welfare 에 list_job 을 결합 - 매칭
welfare = welfare.merge(list_job, how='left', on = 'code_job')

# code_job 결측치를 제외하고 code_job, job 출력
a = welfare.dropna(subset=['code_job'])[['code_job','job']].head()
# print(a)

### 직업별 월급 차이 분석
# 직업별 월급 평균표 생성
job_income = welfare.dropna(subset=['job','income']) \
    .groupby('job',as_index=False)\
    .agg(mean_income = ('income','mean'))
# print(job_income.head(10))

# 월급이 많은 직업 - 상위 10개 추출
top10 = job_income.sort_values('mean_income', ascending=False).head(10)
# print(top10)

# 시각화
# 맑은 고딕 폰트 설정 - 파이썬에서 한글을 쓰려면 한글 폰트를 그래프에 지정해줘야 한다.
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family' : 'Malgun Gothic'}) # 한글 폰트 지정

# 막대 그래프 생성
# sns.barplot(data=top10, y='job', x='mean_income')
# plt.show()

# 월급이 적은 직업 - 하위 10개
bottom10 = job_income.sort_values('mean_income').head(10)
# print(bottom10)

# 막대 그래프 생성
# sns.barplot(data=bottom10, y='job', x='mean_income')\
#     .set(xlim=[0,800])
# plt.show()

''' 성별 직업 빈도 분석 - 성별로 직업의 수가 다를까 ? '''
# 남성 top 10
job_male = welfare.dropna(subset=['job'])\
    .query('s == "Male"') \
    .groupby('job', as_index=False)\
    .agg(n = ('job','count'))\
    .sort_values('n', ascending=False)\
    .head(10)
# print(job_male)

# 여성 top 10
job_female = welfare.dropna(subset=['job'])\
    .query('s == "Female"') \
    .groupby('job', as_index=False)\
    .agg(n = ('job','count'))\
    .sort_values('n', ascending=False)\
    .head(10)
# print(job_female)

# 남성 직업 빈도 막대 그래프
# sns.barplot(data=job_male, y='job', x='n')\
#     .set(xlim=[0,500])
# plt.show()

# 여성 직업 빈도 막대 그래프
# sns.barplot(data=job_female, y='job', x='n')\
#     .set(xlim=[0,500])
# plt.show()

''' 지역별 연령대 비율 - 어느 지역이 노인 인구가 많을까 ? '''
### 지역 변수 검토
a = welfare['code_region'].dtypes  # 변수 타입 출력
# print(a)

a = welfare['code_region'].value_counts() # 빈도 구하기
# print(a)

# 전처리 - 지역 코드 목록 생성 후 merge
list_region = pd.DataFrame({'code_region' : [1,2,3,4,5,6,7],
                            'region' : ['서울',
                                        '수도권(인천/경기)',
                                        '부산/울산/경남',
                                        '대구/경북',
                                        '대전/충남',
                                        '강원/충북',
                                        '광주/전남/전북/제주도']})
# print(list_region)

# 지역명 변수 추가
welfare = welfare.merge(list_region, how='left', on='code_region')
# print(welfare[['code_region', 'region']].head(20))

### 지역별 연령대 비율 분석
# 1. 지역별 연령대 비율표 생성
region_ageg = welfare.groupby('region',as_index=False)\
    ['ageg']\
    .value_counts(normalize=True)
# print(region_ageg)

# 2. 백분율로 변경 후 반올림
region_ageg = \
    region_ageg.assign(proportion = region_ageg['proportion']*100) \
    .round(1)
# print(region_ageg)

# 3. 막대 그래프 생성
# sns.barplot(data=region_ageg, y='region', x='proportion', hue='ageg')
# plt.show()

### 누적 비율 막대 그래프 생성하기
# 1. 피벗(pivot) : 행과 열을 재정렬하는 행위
pivot_df = \
    region_ageg[['region', 'ageg','proportion']].pivot(index = 'region',
                                                       columns = 'ageg',
                                                       values = 'proportion')
# print(pivot_df)

# 2. 가로 막대 그래프 생성
# pivot_df.plot.barh(stacked=True)
# plt.show()

# 3. 가로 막대 내부 정렬 - 노년층 비율 기준 정렬, 변수 순서 바꾸기
reorder_df = pivot_df.sort_values('old')[['young','middle','old']]
# print(reorder_df)

# 4. 그래프 생성
# reorder_df.plot.barh(stacked=True)
# plt.show()

# -------------------------------------------------------------------------------------
''' 통계적 분석 기법을 활용한 가설 검정 '''
'''
기술 통계 : 데이터를 요약해 설명하는 통계 분석 기법
추론 통계 : 어떤 값이 발생할 확률을 계산하는 통계 분석 기법

ex) 성별에 따른 월급 차이가 우연히 발생할 확률을 계산

- 이런 차이가 우연히 나타날 확률이 작다면
    -> 성별에 따른 월급 차이가 통계적으로 유의하다 고 결론
- 이런 차이가 우연히 나타날 확률이 크다면
    -> 성별에 따른 월급 차이가 통계적으로 유의하지 않다 고 결론

- 기술 통계 분석에서 집단 간 차이가 있는것으로 나타나더라도 이것은 우연일 가능성이 있다.
- 신뢰할 수 있는 결론을 내리려면 유의확률을 계산하는 통계적 가설 검정 절차를 거칠 필요가 o 

통계적 가설 검정 : 유의확률을 이용해서 가설을 검정하는 방법
유의확률(p-value) : 실제로는 집단 간에 차이가 없는데 우연히 차이가 있는 데이터가
                   추출될 확률

1. 유의확률이 크면
- 집단 간 차이가 통계적으로 유의하지 않다. 고 해석
- 실제로 차이가 없더라도 우연에 의해 이정도의 차이가 관찰될 가능성이 크다.는 의미

2. 유의확률이 작으면
- 집단 간 차이가 통계적으로 유의하다. 고 해석
- 실제로는 차이가 없는데 우연히 이 정도의 차이가 관찰될 가능성이 작다, 우연이라고 보기 힘들다.
'''

''' t-검정 : 두 집단의 평균에 통계적으로 유의한 차이가 있는지 알아볼 때 사용하는 통계 분석 기법 '''
### mpg Data - compact 자동차와 suv 자동차의 도시 연비 t-검정
mpg = pd.read_csv(path + 'mpg.csv')
# print(mpg)

## 기술 통계 분석
# compact, suv 추출 -> category별 그룹화 -> 빈도 구하기 -> cty 평균 생성
a = mpg.query('category in ["compact", "suv"]') \
    .groupby('category', as_index=False) \
    .agg(n = ('category', 'count'),
         mean = ('cty', 'mean'))
# print(a)


## t검정
'''
비교하는 집단의 분산(값들이 퍼져 있는 정도)이 같은지 여부에 따라 적용하는 공식이 틀림
equal_val = True : 집단 간 분산이 같다고 가정
'''
compact = mpg.query('category == "compact"')['cty']
suv = mpg.query('category == "suv"')['cty']

# t-test
from scipy import stats
a = stats.ttest_ind(compact, suv, equal_var=True)
# print(a)
'''
일반적으로 유의확률 5% 를 판단 기준으로 잡는다. **

TtestResult(statistic=11.917282584324107, pvalue=2.3909550904711282e-21, df=107.0)

pvalue 가 0.05 미만이면 집단간 차이가 통계적으로 유의하다. 고 해석 

e-21 : 지수 표현식 -> 앞의 숫자 앞에 소수점 0 이 21개 더 있다. 더 작은 값이라는 얘기
10의 -21승
e+21 : 지수 표현식 -> 앞의 숫자 뒤에 10 이 21개 더 있다. 더 큰 값이라는 얘기
10의 21승

pvalue=2.3909550904711282e-21 : pvalue 가 0.05보다 작기 때문에 'compact와 suv간 평균
                                도시 연비 차이가 통계적으로 유의하다.'고 결론
'''

### 일반 휘발유와 고급 휘발유의 도시 연비 t검정
regular = mpg.query('fl == "r"')['cty']
premium = mpg.query('fl == "p"')['cty']

# t-test
a = stats.ttest_ind(regular, premium, equal_var=True)
# print(a)

''' 해석
- pvlaue 가 0.05보다 큼
- 실제로는 차이가 없는데 우연에 의해 이 정도의 차이가 관찰될 확률이 28.75%
- 일반 휘발유와 고급 휘발유를 사용하는 자동차의 도시 연비 차이가 통계적으로 유의하지 않다. 고 결론
'''
# ---------------------------------------------------------------------------------------
''' 상관 분석 : 두 연속 변수가 서로 관련이 있는지 검정하는 통계 분석 기법 

상관 계수
- 두 변수가 얼마나 관련되어 있는지, 관련성의 정도를 파악할 수 있다.
- 0~1 사이의 값을 가진다. 1에 가까울수록 관련성이 크다는 의미.
- 양수면 정비례, 음수면 반비례 관계
'''

### 실업자 수와 개인 소비 지출의 상관 관계 - economics Data
economics = pd.read_csv(path + 'economics.csv')
# print(economics)

# 1. 상관계수 구하기 - 상관 행렬을 만들기
a = economics[['unemploy', 'pce']].corr()
# print(a)

# 2. 상관분석 진행
a = stats.pearsonr(economics['unemploy'], economics['pce'])
# print(a)
'''
PearsonRResult(statistic=0.6145176141932082, pvalue=6.773527303289964e-61)

- 출력 결과의 첫 번째 값이 상관 계수, 두번째 값이 유의 확률
- 유의확률이 0.05 미만이므로 실업자 수와 개인 소비 지출의 상관관계가 통계적으로 유의하다. 고 결론
'''

### 상관행렬 히트맵 만들기 - 상관분석 시각화
'''
상관행렬 (correlation matrix)
- 모든 변수의 상관관계를 나타낸 행렬
- 여러 변수의 관련성을 한꺼번에 알아보고 싶을 때 사용
- 어떤 변수끼리 관련이 크고 적은지 한 눈에 파악할 수 있다.
'''

# 1. 상관행렬 만들기
mtcars = pd.read_csv(path + 'mtcars.csv')

car_cor = mtcars.corr() # 상관행렬 만들기
car_cor = round(car_cor, 2) # 소수점 둘째 자리까지 반올림
# print(car_cor)

# 히트맵 생성
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.dpi' : '120', # 해상도
                     'figure.figsize' : [7.5, 5.5]}) # 가로 세로 크기 설정
import seaborn as sns
# sns.heatmap(car_cor,
#             annot=True, # 상관계수 표시
#             cmap = 'RdBu') # 컬러맵
# plt.show()

### 대각 행렬 제거
# 히트맵은 대각선 기준으로 왼쪽 아래와 오른쪽 위의 값이 대칭해서 중복됨.
# sns.heatmap() 의 mask 를 사용해서 중복된 부분을 제거해준다.

# 1. mask 만들기 - 상관행렬의 행과 열의 수 만큼 0으로 채운 배열(array)을 만들어줌
import numpy as np
mask = np.zeros_like(car_cor)
# print(mask)

# 1-1 mask의 오른쪽 위 대각 행렬을 1로 바꿈
mask[np.triu_indices_from(mask)] = 1
# print(mask)

# 2. 히트맵에 적용
# sns.heatmap(data = car_cor,
#             annot = True,
#             cmap = 'RdBu',
#             mask = mask)
# plt.show()

### 히트맵을 보기 좋게 수정하는 옵션들
# sns.heatmap(data=car_cor,
#             annot=True, # 상관 계수 표시
#             cmap=sns.cubehelix_palette(as_cmap=True), # 컬러맵
#             mask=mask, # mask 적용
#             linewidths=.75, # 경계 구분선 추가
#             vmax=1, # 가장 진한 파란색으로 표현할 최대 값
#             vmin=-1, # 가장 진한 빨간색으로 표현할 최대 값
#             cbar_kws={'shrink':.5}) # 범례의 크기를 줄이기
# plt.show()

# ---------------------------------------------------------------------------------------------
''' 텍스트 마이닝 
형태소 분석
- 문장을 구성하는 어절들의 품사를 분석
- 텍스트 마이닝을 할 때 가장 먼저 하는 작업
- 명사, 동사, 형용사 등 의미를 지닌 품사를 추출해서 빈도를 확인

KoNLPy 패키지 설치하기
1. JAVA 설치 
2. KoNLPy 의존성 패키지 설치 : pip install jpype1
3. KoNLPy 설치 : pip install konlpy
'''

### 가장 많이 사용된 단어 알아보기 - 연설문에서
# 1. 연설문 로드 - 텍스트 파일 로드
# 파이썬에서 텍스트파일은 open() 로 파일을 열고 read() 로 불러온다.
moon = open(path + 'speech_moon.txt', encoding='UTF-8').read()
# print(moon)

# 2. 불필요한 문자 제거
# 특수문자, 한자, 공백은 분석 대상이 x - 제거
# re.sub() 사용해서 한글이 아닌 모든 문자를 공백으로 바꿔준다.
# [^가-힣] : 한글이 아닌 모든 문자를 의미하는 정규 표현식

import re
moon = re.sub('[^가-힣]', ' ', moon)
# print(moon)

# 3. 명사 추출
# hannanum 만들기
import konlpy
hannanum = konlpy.tag.Hannanum()

# 추출
h = hannanum.nouns('대한민국의 영토는 한반도와 그 부속도서로 한다.')
# print(h)

# 연설문에서 추출
nouns = hannanum.nouns(moon)
# print(nouns)

# 4. 리스트를 다루기 쉽게 데이터 프레임으로 변환
import pandas as pd
df_word = pd.DataFrame({'word' : nouns})
# print(df_word)

# 5. 단어 빈도표 만들기
# str.len() : 글자 수 세기
df_word['count'] = df_word['word'].str.len()
# print(df_word)

# 6. 두 글자 이상 단어만 남기기
df_word = df_word.query('count >= 2')
a = df_word.sort_values('count')
# print(a)


# 7. 단어 빈도 구하기
df_word = df_word.groupby('word', as_index=False) \
    .agg(n = ('word', 'count')) \
    .sort_values('n', ascending=False)
# print(df_word)

# 8. 단어 빈도 막대 그래프
# 단어 빈도 상위 20개 추출
top20 = df_word.head(20)
# print(top20)

# 그래프 옵션 조정
plt.rcParams.update({'font.family' : 'Malgun Gothic',
                     'figure.dpi' : '120',
                     'figure.figsize' : [6.5, 6]})

# 막대 그래프 생성
# sns.barplot(data=top20, y='word', x='n')
# plt.show()

''' 워드 클라우드 : 단어의 빈도를 구름 모양으로 표현한 그래프 
- 단어의 빈도에 따라 글자의 크기와 색깔을 다르게 표현
- 어떤 단어가 얼마나 많이 사용됐는지 한 눈에 파악할 수 있다.
'''

# 워드 클라우드 패키지 설치 : pip install wordcloud

# 1. 워드 클라우드에 사용한 한글 폰트 지정
font = 'H2SA1M.TTF'

# 2. 단어와 빈도를 담은 딕셔너리 만들기 - 단어가 key, 빈도가 value 로 구성
# 2-1 데이터 프레임을 딕셔너리로 변환
dic_word = df_word.set_index('word').to_dict()['n']
# print(dic_word)

# 3. wc 만들기
# from wordcloud import WordCloud
# wc = WordCloud(random_state=1234, # 난수 고정
#                font_path=font, # 폰트 설정
#                width=400, # 가로 크기
#                height=400, # 세로 크기
#                background_color='white') # 배경색

# 4. 워드 클라우드 생성
# img_wordcloud = wc.generate_from_frequencies(dic_word)

# 출력
# plt.figure(figsize=(10,10)) # 그래프의 가로, 세로 크기 설정
# plt.axis('off') # 테두리 선 없애기
# plt.imshow(img_wordcloud) # 워드 클라우드 출력 함수
# plt.show()

### 워드 클라우드 모양 바꾸기

# 1. mask 만들기
import PIL
icon = PIL.Image.open(path + 'cloud.png')

import numpy as np
img = PIL.Image.new('RGB', icon.size, (255,255,255))
img.paste(icon, icon)
img = np.array(img)

# 2. 워드 클라우드 만들기
from wordcloud import WordCloud
# wc = WordCloud(random_state=1234,
#                font_path=font,
#                width=400,
#                height=400,
#                background_color='black',
#                mask = img) # mask 설정
# img_wordcloud = wc.generate_from_frequencies(dic_word)
# plt.figure(figsize=(10,10))
# plt.axis('off')
# plt.imshow(img_wordcloud)
# plt.show()

# 3. 워드 클라우드 글자 색깔 바꾸기
# colormap = 'inferno' 컬러맵(색상목록) 입력만 해주면 가능
wc = WordCloud(random_state=1234,
               font_path=font,
               width=400,
               height=400,
               background_color='white',
               mask = img,  # mask 설정
               colormap='cividis') # 컬러맵 설정
img_wordcloud = wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()