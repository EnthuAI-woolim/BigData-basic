' 24 - 08 - 17 강의 자료 '

'
- 데이터 파악 함수
1. head() , tail() - 데이터의 앞 부분, 뒷 부분
2. str() - 데이터의 속성 출력
3. summary() - 요약통계량 출력

- 데이터 가공 (전처리 함수) : dplyr 패키지
1. filter() - 행 추출
2. select() - 열 추출
3. arrange() - 정렬
4. summarise() - 통계치 산출
5. group_by() - 집단별로 나누기
6. left_join() - 데이터 합치기(열)
7. bind_rows() - 데이터 합치기(행)
'

# -----------------------------------------------------------------
' 데이터 정제 - 빠진 데이터, 이상한 데이터 제거 '

'
결측치 (Missing Value)
-> 누락된 값, 비어있는 값
-> 함수 적용 불가, 분석 결과 왜곡
-> 제거 후 분석 실시
'

### 결측치 찾기
df <- data.frame(s = c("M","F", NA, "M","F"),
                 score = c(5,4,3,4,NA))
df

## 결측치 확인
is.na(df)

## 결측치 빈도 출력
table(is.na(df)) 

## 변수 별로 결측치 확인
table(is.na(df$s))

## 결측치 포함된 상태로 분석
mean(df$score)
sum(df$score)

### 결측치 제거
library(dplyr)

## 결측치가 있는 행 제거
df %>% filter(is.na(score)) # score 가 NA 인 데이터만 출력
df %>% filter(!is.na(score)) # score 결측치 제거

df_nomiss <- df %>% filter(!is.na(score))
mean(df_nomiss$score)

## 여러 변수 동시에 결측치 없는 데이터 추출하기
## score , s 동시에 결측치 제외
df_nomiss <- df %>% filter(!is.na(score) & !is.na(s))
df_nomiss

## 결측치가 하나라도 있으면 제거
df_nomiss2 <- na.omit(df) # 모든 변수에 결측치가 없는 데이터 추출
df_nomiss2
df
# -> 분석에 필요한 데이터까지 손실 될 가능성이 있다.

## 함수의 결측치 제외 기능 - na.rm = T
mean(df$score, na.rm = T)

# summarise() 에서 na.rm = T 사용
exam <- read.csv('R_Data/csv_exam.csv')
exam
exam[c(3,8,15), 'math'] <- NA # 3, 8, 15 행의 math에 NA 할당
exam

exam %>% summarise(mean_math = mean(math))
exam %>% summarise(mean_math = mean(math, na.rm = T),
                   sum_math = sum(math, na.rm = T),
                   median_math = median(math, na.rm = T))

### 결측치 대체
# -> 결측치가 많을 경우 모두 제외하면 데이터 손실이 크다.
# -> 대안 : 다른 값 채워넣기
# 결측치 대체법 : 대표값(평균, 최빈값 등)으로 일괄 대체
# 통계분석 기법 적용, 예측값 추정해서 대체

## 평균값으로 결측치 대체

# 1. 평균 구하기
mean(exam$math, na.rm = T)
# 2. 구한 평균으로 대체
exam$math <- ifelse(is.na(exam$math), 55, exam$math)
exam$math <- ifelse(is.na(exam$math), round(mean(exam$math, na.rm = T)), exam$math)
table(is.na(exam$math))
mean(exam$math)

'
이상치(Outlier) - 정상 범주에서 크게 벗어난 값
-> 이상치 포함시 분석 결과 왜곡
-> 결측처리 후 제외하고 분석

1. 존재할 수 없는 값 ex) 성별 변수에 3 -> 결측 처리
2. 극단적인 값 ex) 몸무게 변수에 230 -> 정상 범위 기준 정해서 결측 처리 
'
### 이상치 제거 - 존재할 수 없는 값
outlier <- data.frame(s = c(1,2,1,3,2,1),
                      score = c(5,4,3,4,2,6))
outlier

## 1. 이상치 확인
table(outlier$s)
table(outlier$score)

## 2. 결측 처리 - 성별, 만족도
outlier$s <- ifelse(outlier$s == 3, NA, outlier$s)
outlier
outlier$score <- ifelse(outlier$score == 6, NA, outlier$score)
outlier

## 3. 결측치 제외하고 분석
outlier %>%
  filter(!is.na(s) & !is.na(score)) %>%
  group_by(s) %>%
  summarise(mean_score = mean(score))

### 이상치 제거 - 극단적인 값
'
- 정상 범위 기준 정해서 벗어나면 결측 처리

1. 논리적 판단 : 성인 몸무게 40kg - 150kg 벗어나면 극단치
2. 통계적 판단 : 상하위 0.3% 극단치 또는 상자 그림 1.5IQR을 벗어나면 극단치 
'

## 상자 그림으로 극단치 기준 정해서 제거

# 1. 상자 그림 생성
install.packages('ggplot2')
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
mpg

boxplot(mpg$hwy)

# 상자그림 통계치 출력법
boxplot(mpg$hwy)$stats
'
[1,]   12 # 아래쪽 극단치 경계
[2,]   18 # 1사분위수
[3,]   24 # 중앙값
[4,]   27 # 3사분위수
[5,]   37 # 위쪽 극단치 경계
'

# 12 ~ 37 벗어나면 이상치로 간주하고 NA 할당 해줘야겠다. 
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)
table(is.na(mpg$hwy))

# 결측치 제외하고 분석
mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy, na.rm = T))

# ------------------------------------------------------------------
'
- R 로 만들 수 있는 그래프
1. 2차원 그래프, 3차원 그래프
2. 지도 그래프
3. 네트워크 그래프
4. 모션 차트
5. 인터랙티브 그래프

- ggplot2 의 레이어 구조
1단계 : 배경 설정 (축)
2단계 : 그래프 추가(점, 막대, 선...)
3단계 : 설정 (축 범위, 색, 표식)
'

'
산점도(Scatter Plot) : 데이터를 x축과 y축에 점으로 표현한 그래프 
-> 나이와 소득 처럼 연속 값으로 된 두 변수의 관계를 표현할 때 사용
'
library(ggplot2) # 패키지 로드

## 1. 배경 설정
# x축 displ(배기량), y축 hwy(고속도로연비)로 지정해 배경 생성
ggplot(data=mpg, aes(x=displ, y=hwy))

## 2. 그래프 추가 - 어떤 그래프로 표현할건지?
# 배경에 산점도 추가
ggplot(data=mpg, aes(x=displ, y=hwy)) + geom_point()

## 3. 축 범위를 조정하는 설정 추가하기
# x 축 범위를 3~6 으로 조정
ggplot(data=mpg, aes(x=displ, y=hwy)) + geom_point() + xlim(3,6)

# x축 범위 3~6, y축 10~30 으로 지정
ggplot(data=mpg, aes(x=displ, y=hwy)) +
  geom_point() +
  xlim(3,6) + 
  ylim(10,30)

'
qplot() : 전처리 단계 데이터 확인용, 문법 간단, 기능 단순
ggplot() : 최종 보고용. 색, 크기, 폰트 등 세부 조작 가능
'

'
막대 그래프 (Bar Chart) : 데이터의 크기를 막대의 길이로 표현
-> 성별 소득 차이 처럼 집단 간 차이를 표현할 때 자주 사용
'

### 막대 그래프 - 평균 막대 그래프 : 각 집단의 평균값을 막대 길이로 표현

# 1. 집단별 평균표 만들기
library(dplyr)
mpg <- as.data.frame(ggplot2 :: mpg)

df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))
df_mpg

# 2. 그래프 생성
ggplot(data=df_mpg, aes(x=drv, y=mean_hwy)) + geom_col()

# 3. 크기 순으로 정렬
ggplot(data=df_mpg, aes(x=reorder(drv, -mean_hwy), y=mean_hwy)) +
  geom_col()

### 막대 그래프 - 빈도 막대 그래프 : 값의 개수(빈도)로 막대의 길이를 표현

# 1. x축 범주 변수, y축 빈도
ggplot(data=mpg, aes(x=drv)) + geom_bar()

# 2. x축 연속 변수, y축 빈도
ggplot(data=mpg, aes(x=hwy)) + geom_bar()

'
평균 막대 그래프 : 데이터를 요약한 평균표를 먼저 만든 후
                  평균표를 이용해서 생성 - geom_col()
빈도 막대 그래프 : 별도로 표를 만들지 않고 원자료를 이용해
                  바로 그래프 생성 - geom_bar()
'

'
선 그래프(Line Chart) : 데이터를 선으로 표현한 그래프

시계열 그래프(Time Series Chart)
: 일정 시간 간격을 두고 나열된 시계열 데이터를 선으로 표현한
그래프. 환율, 주가지수 등 경제 지표가 시간에 따라 어떻게 
변하는지 표현할 때 자주 사용
'
ggplot(data=economics, aes(x=date, y=unemploy)) +
  geom_line()

'
상자 그림 - 집단 간 분포 차이

분포를 알 수 있기 때문에 평균만 볼 때 보다
데이터의 특성을 좀 더 자세히 이해할 수 있다.
'
ggplot(data=mpg, aes(x=drv,y=hwy)) + geom_boxplot()

'
1.5IQR : 사분위 범위(Q1~Q3간 거리)의 1.5배
'

library(ggplot2)

ggplot(mpg, aes(displ, hwy, colour = drv)) + 
  geom_point()

# ---------------------------------------------------------------------
' 한국인의 삶을 파악하자 

한국복지패널데이터
- 한국보건사회연구원 발간
- 가구의 경제활동을 연구해 정책 지원에 반영할 목적
- 2006 ~ 2015년까지 전국에서 7천여 가구를 선정해 매년 추적 조사
- 경제활동, 생활실태, 복지욕구 등 수천 개 변수에 대한 정보로 구성
'
install.packages('foreign')
library(foreign) # SPSS 파일 로드
library(dplyr) # 전처리
library(ggplot2) # 시각화
library(readxl) # 엑셀 파일 로드

### 데이터 준비
raw_welfare <- read.spss(file='Koweps_hpc10_2015_beta1.sav',
                         to.data.frame = T)
### 복사본 만들기
welfare <- raw_welfare

### 데이터 검토
head(welfare)
str(welfare)
summary(welfare)

'
대규모 데이터 같은 경우는 사용할 변수명을 쉬운 단어로 바꾼 후
분석에 사용할 변수들 각각 파악하는게 좋음. 
'

### 변수명 수정
welfare <- rename(welfare,
                  s = h10_g3, # 성별
                  birth = h10_g4, # 태어난 년도
                  marriage = h10_g10, # 혼인 상태
                  religion = h10_g11, # 종교
                  income = p1002_8aq1, # 월급
                  code_job = h10_eco9, # 직종 코드
                  code_region = h10_reg7) # 지역 코드

'
데이터 분석 절차
1단계 : 변수 검토 및 전처리
2단계 : 변수 간 관계 분석 (요약표 만들거나 그래프 생성)
'

' 성별에 따른 월급 차이 - 성별에 따라 월급이 다를까 ? '

## 성별 변수 검토 및 전처리
class(welfare$s)
table(welfare$s) # 이상치 확인

# 전처리 - 이상치 x
table(is.na(welfare$s)) # 결측치 x

welfare$s
# 성별 항목 이름 부여
welfare$s <- ifelse(welfare$s == 1, 'Male', 'Female')
table(welfare$s)
qplot(welfare$s)

## 월급 변수 검토 및 전처리
class(welfare$income)
summary(welfare$income)
qplot(welfare$income) + xlim(0,1000)

# 전처리
summary(welfare$income)

# 이상치 결측 처리
welfare$income <- ifelse(welfare$income %in% c(0, 9999),
                         NA, welfare$income)

# 결측치 확인
table(is.na(welfare$income))

### 성별에 따른 월급 차이 분석
s_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(s) %>%
  summarise(mean_income = mean(income))
s_income

# 그래프 생성
ggplot(data = s_income, aes(x=s, y=mean_income)) +
  geom_col()

' 나이와 월급의 관계 - 몇 살 때 월급을 가장 많이 받을까? '

## 나이 변수 검토 및 전처리
class(welfare$birth)
summary(welfare$birth) # 이상치 확인
qplot(welfare$birth)

# 결측치 확인
table(is.na(welfare$birth))

# 파생변수 생성 - 나이(age)

welfare$age <- 2015 - welfare$birth + 1
summary(welfare$age)
qplot(welfare$age)

## 나이와 월급의 관계 분석
age_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(age) %>%
  summarise(mean_income = mean(income))
age_income

# 그래프 생성
ggplot(data=age_income, aes(x=age, y=mean_income)) +
  geom_line(colour = 'skyblue',
            size = 2.0,
            linetype =1.5)

' 연령대에 따른 월급 차이 - 어떤 연령대의 월급이 가장 많을까? '

## 파생변수 - 연령대(ageg)
welfare <- welfare %>%
  mutate(ageg = ifelse(age < 30, 'young',
                       ifelse(age <= 59, 'middle','old')))
table(welfare$ageg)

## 연령대에 따른 월급 차이 분석
ageg_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(ageg) %>%
  summarise(mean_income = mean(income))
ageg_income

ggplot(data=ageg_income, aes(x=ageg, y=mean_income)) +
  geom_col()

## 막대 정렬 
ggplot(data=ageg_income, aes(x=ageg, y=mean_income)) +
  geom_col() +
  scale_x_discrete(limits = c('young','middle','old'))

' 연령대 및 성별 월급 차이 - 성별 월급 차이는 연령대별로 다를까? '

## 연령대 및 성별 월급 평균표 생성
s_income <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(ageg, s) %>%
  summarise(mean_income = mean(income))
s_income

## 그래프 생성
ggplot(data=s_income, aes(x=ageg, y=mean_income, fill=s)) +
  geom_col() +
  scale_x_discrete(limits = c('young','middle','old'))

## 성별 막대 분리
ggplot(data=s_income, aes(x=ageg, y=mean_income, fill=s)) +
  geom_col(position = 'dodge') +
  scale_x_discrete(limits = c('young','middle','old'))

### 나이 및 성별 월급 차이 분석
s_age <- welfare %>%
  filter(!is.na(income)) %>%
  group_by(age, s) %>%
  summarise(mean_income = mean(income))
head(s_age)

## 그래프 생성
ggplot(data=s_age, aes(x=age, y=mean_income, col=s)) +
  geom_line(size=2.0)

' 직업별 월급 차이 - 어떤 직업이 돈을 가장 많이 버는가?'

## 직업 변수 검토 및 전처리
class(welfare$code_job)
table(welfare$code_job)

# 전처리 (직업 분류 시트 불러오기 , left_join())
list_job <- read_excel('Koweps_Codebook.xlsx',
                       col_names = T,
                       sheet = 2)

welfare <- left_join(welfare, list_job, by='code_job')

welfare %>%
  filter(!is.na(code_job)) %>%
  select(code_job, job) %>%
  head(10)

## 직업별 월급 차이 분석
job_income <- welfare %>%
  filter(!is.na(job) & !is.na(income)) %>%
  group_by(job) %>%
  summarise(mean_income = mean(income))
head(job_income)

## 상위 10개 추출
top10 <- job_income %>%
  arrange(desc(mean_income)) %>%
  head(10)
top10

## 그래프 생성
ggplot(data=top10, aes(x=reorder(job, mean_income), y=mean_income, fill=job)) +
  geom_col() +
  coord_flip() # 그래프를 돌려주는 옵션

' 성별 직업 빈도 분석 - 성별로 어떤 직업이 가장 많은가? '

### 성별 직업 빈도표 생성

# 1. 남성 직업 빈도 상위 10개 추출
job_male <- welfare %>%
  filter(!is.na(job) & s == 'Male') %>%
  group_by(job) %>%
  summarise(n = n()) %>%
  arrange(desc(n)) %>%
  head(10)
job_male

# 2. 여성 직업 빈도 상위 10개 추출
job_female <- welfare %>%
  filter(!is.na(job) & s == 'Female') %>%
  group_by(job) %>%
  summarise(n = n()) %>%
  arrange(desc(n)) %>%
  head(10)
job_female

## 그래프 생성
ggplot(data=job_male, aes(x=reorder(job, n), y=n)) +
  geom_col() +
  coord_flip()

ggplot(data=job_female, aes(x=reorder(job, n), y=n)) +
  geom_col() +
  coord_flip()
