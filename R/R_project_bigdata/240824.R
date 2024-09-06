' 24 - 08 - 24 강의 자료 '

' -Review
1. 결측치 확인
table(is.na(df$score))

2. 함수의 결측치 제외 기능
mean(df$score, na.rm=T)

3. 이상치 확인
table(outlier$s)

4. ggplot2 함수들
geom_point() : 산점도
geom_col() : 막대그래프 - 요약표
geom_bar() : 막대그래프 - 원자료
geom_line() : 선 그래프
geom_boxplot() : 상자 그림
'
# ---------------------------------------------------------
 
' 
종교 유무에 따른 이혼율
- 종교가 있는 사람들이 이혼을 덜 할까 ? 
'
library(dplyr)
library(ggplot2)

### 종교 변수 검토 및 전처리
class(welfare$religion)
table(welfare$religion)

# 종교 유무에 이름을 부여
welfare$religion <- ifelse(welfare$religion == 1,
                           'YES', 'NO')
qplot(welfare$religion)

### 혼인 상태 변수 검토 및 전처리
class(welfare$marriage)
table(welfare$marriage)

# 이혼 여부 변수 생성
welfare$group_marriage <- ifelse(welfare$marriage == 1, 'marriage',
                                 ifelse(welfare$marriage == 3, 'divorce', NA))
table(welfare$group_marriage)

table(is.na(welfare$group_marriage))
qplot(welfare$group_marriage)

### 종교 유무에 따른 이혼율 표 생성
religion_marriage <- welfare %>%
  filter(!is.na(group_marriage)) %>%
  group_by(religion, group_marriage) %>%
  summarise(n = n()) %>%
  mutate(tot_group = sum(n),
         pct = round(n/tot_group*100, 1))

religion_marriage

### 이혼율 표 생성
# 이혼 추출
divorce <- religion_marriage %>%
  filter(group_marriage == 'divorce') %>%
  select(religion, pct)
divorce

ggplot(data=divorce, aes(x=religion, y=pct)) + geom_col()

' 지역별 연령대 비율 - 노년층이 많은 지역은 어디인가? '

### 지역 변수 검토 및 전처리
class(welfare$code_region)
table(welfare$code_region)

# 지역 코드 목록 생성
list_region <- data.frame(code_region = c(1:7),
                          region = c(
                            '서울',
                            '수도권(인천/경기)',
                            '부산/경남/울산',
                            '대구/경북',
                            '대전/충남',
                            '강원/충북',
                            '광주/전남/전북/제주도'
                          ))

# welfare 에 지역명 변수 추가 - 매칭
welfare <- left_join(welfare, list_region, by='code_region')
welfare %>%
  select(code_region, region) %>%
  head(20)

### 지역별 연령대 비율 분석
# 나이 변수가 없는 경우 새로 생성
welfare$age <- 2015 - welfare$birth + 1
# 연령대 변수가 없는 경우 새로 생성
welfare <- welfare %>%
  mutate(ageg = ifelse(age < 30, 'young',
                       ifelse(age <= 59,'middle','old')))
# 지역별 연령대 비율표 생성
region_ageg <- welfare %>%
  group_by(region, ageg) %>%
  summarise(n=n()) %>%
  mutate(tot_group = sum(n),
         pct = round(n/tot_group*100, 2))

region_ageg

# 그래프 생성
ggplot(data=region_ageg, aes(x=region, y=pct, fill=ageg)) +
  geom_col() +
  coord_flip()

# 막대 정렬 : 노년층 비율 높은 순서
list_order_old <- region_ageg %>%
  filter(ageg == 'old') %>%
  arrange(pct)
list_order_old

# 지역명 순서 변수 생성
order <- list_order_old$region
order
ggplot(data=region_ageg, aes(x=region, y=pct, fill=ageg)) +
  geom_col() +
  coord_flip() +
  scale_x_discrete(limits=order)

# ------------------------------------------------------------------
'
텍스트 마이닝(Text Mining)
- 문자로 된 데이터에서 가치 있는 정보를 얻어 내는 분석 기법
- sns나 웹 사이트에 올라온 글을 분석해서 사람들이 어떤 이야기를 나누고 있는지 
  파악할 때 자주 사용
- 형태소 분석(Morphology Analysis) : 문장을 구성하는 어절들이 어떤 품사로 되어
                                     있는지 분석
- 분석절차
1. 형태소 분석
2. 명사, 동사 형용사 등의 의미를 지닌 품사 단어를 추출
3. 빈도표 만들기
4. 시각화

- 텍스트 마이닝을 하려면 JAVA 설치가 필요하다.

1. 정형 데이터 : 여러 행과 열로 이루어진 표준 테이블 형식
                분석 및 머신러닝 알고리즘에 적합하고 처리에 용이하다.
                
2. 비정형 데이터 : 사전에 정의된 데이터 형식이 없는 데이터
                소셜 미디어나 제품 리뷰같은 소스의 텍스트,
                데이터베이스의 요구사항을 충족하기에는 정형성이 부족
                ex) 텍스트, 댓글, 리뷰, 비밀번호 데이터
                
3. 반정형 데이터 : 정형 데이터 비정형 데이터의 형식이 혼합된 데이터,
                  어느정도 체계화는 되어 있지만, 관계형 데이터베이스의
                  요구사항을 충족하기에는 정형성이 부족한 데이터
                  ex) XML, JSON, HTML
                  
-> 전 세계에서 데이터의 약 80%가 비정형 데이터 형식이므로 텍스트 마이닝은
  현업에서 매우 중요한 프로세스
'
### 텍스트 마이닝 환경 설정법
## 1. JAVA 설치
## 2. 시스템 환경 변수 편집
## 3. Konlp 패키지 설치 - 한글어 처리 패키지
## 4. 그 외 의존성 패키지 설치
install.packages('rJava')
install.packages('memoise')
install.packages('Konlp') # 설치x 

## 5. git 에서 konlp 가지고 오기
install.packages('devtools')
devtools :: install_github('haven-jeon/KoNLP')

Sys.setenv(JAVA_HOME = 'C:/Program Files/Java/jdk-11.0.12')
install.packages('rJava')
library(rJava)
library(KoNLP)

## 6. 3번 과정이 안된다면 Konlp 수동 설치 후 확인
useNIADic() # 사전 로드
extractNoun('안녕하세요 R을 공부중입니다.') # 형태소 분석기

### 예제 데이터 로드
txt <- readLines('sung.txt')
txt

### 특수문자 제거
install.packages('stringr')
library(stringr)

txt <- str_replace_all(txt, '\\W',' ') # \\W : 특수문자
txt

### 가장 많이 사용된 단어를 확인

# 1. 명사 추출
library(KoNLP)
nouns <- extractNoun(txt)
nouns

# 2. 추출한 명사 list를 문자열 벡터로 전환, 단어별로 빈도 생성
wordcount <- table(unlist(nouns))
wordcount

df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word

# 3. 변수명 수정
library(dplyr)
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)
head(df_word)

# 4. 자주 사용된 단어 빈도표 생성 ( 두 글자 미만은 제외 )
df_word <- filter(df_word, nchar(word) > 2)
head(df_word)
tail(df_word)

# 5. 빈도 기준으로 정렬 후 상위 20개 추출
top20 <- df_word %>%
  arrange(desc(freq)) %>%
  head(20)
top20

### 워드 클라우드 - 단어 구름 시각화
install.packages('wordcloud')
library(wordcloud)
library(RColorBrewer) # 글자 색 표현 패키지

# 1. 단어 색상 목록 코드
a <- brewer.pal.info # 팔렛트 확인
a

pal <- brewer.pal(8, 'Dark2') # Dark2 색상 목록에서 8개 색상 추출

# 2. 난수 고정 - 워드 클라우드가 실행될 때마다 동일한 워드 클라우드 생성
set.seed(1234)

# 3. 워드 클라우드 생성
wordcloud(words=df_word$word, # 단어 입력
          freq = df_word$freq, # 빈도 입력
          min.freq = 2, # 최소 단어 빈도
          max.words = 200, # 표현 단어 수
          random.order = F, # 고빈도 단어를 중앙에 배치
          scale=c(5, 0.5), # 단어 크기 범위
          colors = pal) # 색상

# ------------------------------------------------------------------
### 국정원 트윗 텍스트 마이닝
'
국정원 계정 트윗 데이터
-> 국정원 대선 개입 사실이 밝혀져서 논란이 되었던
 2013년 6월, 독립 언론 뉴스타파 인터넷을 통해 공개한 데이터
'

# 1. 데이터 로드

twitter <- read.csv('twitter.csv',
                    header = T,
                    stringsAsFactors = F,
                    fileEncoding = 'UTF-8') # cp949, EUC-KR
head(twitter, 5)

# 2. 변수명 수정
twitter <- rename(twitter,
                  no = 번호,
                  id = 계정이름,
                  date = 작성일,
                  tw = 내용)

# 3. 특수문자 제거
twitter$tw <- str_replace_all(twitter$tw, '\\W',' ')
head(twitter$tw)

# 4. 단어 빈도표 생성
nouns <- extractNoun(twitter$tw)

# 5. 추출한 명사 list 를 문자열 벡터로 변환, 단어별 빈도표
wordcount <- table(unlist(nouns))
wordcount

# 6. 데이터 프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word

# 7. 변수명 수정
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)

# 8. 두 글자 이상으로 된 단어 추출, 빈도 기준 상위 20 추출
df_word <- filter(df_word, nchar(word) >= 2)

top20 <- df_word %>%
  arrange(desc(freq)) %>%
  head(20)
top20

# 9. 워드 클라우드 생성
pal <- brewer.pal(9, 'Blues')[5:9]
set.seed(1234)

wordcloud(words = df_word$word,
          freq = df_word$freq,
          min.freq = 10,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(11, 0.2),
          colors = pal)

# -------------------------------------------------------------------
' 인터렉티브 그래프 - 움직이는 그래프 '

### 패키지 준비
install.packages('plotly')
library(plotly)

# 1. ggplot으로 그래프 생성
library(ggplot2)
p <- ggplot(data=mpg, aes(x=displ, y=hwy, col=drv)) +
  geom_point()
p
ggplotly(p)

p <- ggplot(data=diamonds, aes(x=cut, fill=clarity)) +
  geom_bar(position = 'dodge')
ggplotly(p)

## 인터렉티브 시계열
install.packages('dygraphs')
library(dygraphs)

economics

# 시간 순서 속성을 지니는 xts 타입으로 변경
library(xts)
eco <- xts(economics$unemploy, order.by = economics$date)
head(eco)

# 인터렉티브 시계열 그래프 생성
dygraph(eco)

#-------------------------------------------------------------------
' 
지도 시각화 

단계 구분도
- 지역별 통계치를 색깔의 차이로 표현한 지도
- 인구나 소득 같은 특성이 지역별로 얼마나 다른 이해하기가 쉽다.
'
install.packages('ggiraphExtra')
library(ggiraphExtra)

### 미국 주별 범죄 데이터 준비
str(USArrests)

library(tibble)

head(USArrests)
# 1. 행 이름을 state 변수로 바꿔서 데이터 프레임 생성
crime <- rownames_to_column(USArrests, var='state')
crime

# 1-2. 지도 데이터와 동일하게 맞추기 위해 state 값을 소문자로 수정
crime$state <- tolower(crime$state)
str(crime)

# 2. 미국 주 지도 데이터 준비
library(ggplot2)
states_map <- map_data('state')
str(states_map)

# 3. 단계 구분도 생성
ggChoropleth(data=crime, # 지도에 표시할 데이터
             aes(fill=Murder, # 색깔로 표현할 변수
                 map_id=state), # 지역 기준 변수
             map = states_map) # 지도 데이터

# 4. 인터렉티브 단계 구분도 생성
ggChoropleth(data=crime,
             aes(fill=Murder, 
                 map_id=state), 
             map = states_map,
             interactive = T)

### 대한민국 시도별 인구, 결핵 환자 수 단계 구분도
install.packages('stringi')
devtools::install_github('cardiomoon/kormaps2014')
library(kormaps2014)

str(korpop1)

library(dplyr)
korpop1 <- rename(korpop1,
                  pop = 총인구_명,
                  name = 행정구역별_읍면동)

# 단계 구분도 생성
library(ggiraphExtra)
library(ggplot2)
ggChoropleth(data=korpop1,
             aes(fill=pop,
                 map_id = code,
                 tooltip = name),
             map=kormap1)

# 시도별 결핵 환자 수 단계 구분도 생성
str(tbc)
ggChoropleth(data=tbc,
             aes(fill=NewPts,
                 map_id = code,
                 tooltip = name),
             map=kormap1,
             interactive = T)

# -----------------------------------------------------------------
' 
통계적 분석 기법을 활용한 가설 검정

- 기술 통계
  : 데이터를 요약해서 설명하는 통계 기법
  ex) 사람들이 받는 월급을 집계해 전체 월급 평균 구하기
  
- 추론 통계
  : 단순히 숫자를 요약하는 것을 넘어서 어떤 값이 발생할 확률을
    계산하는 통계 기법
  ex) 수집된 데이터에서 성별에 따라 월급 차이가 있는것으로
      나타났을때, 이런 차이가 우연히 발생할 확률까지 계산
      
  1) 이런 차이가 우연히 나타날 확률이 작다
   -> 성별에 따른 월급차이 통계적으로 유의하다고 결론
   
  2) 이런 차이가 우연히 나타날 확률이 크다
   -> 성별에 따른 월급차이가 통계적으로 유의하지 않다고 결론
   
  3) 기술 통계 분석에서 집단간 차이가 있는것으로 나타났더라도
     이는 우연의 의한 차이일 수 있음.
     -> 데이터를 이용해서 신뢰할 수 있는 결론을 내리려면
        유의확률을 계산하는 통계적 가설 검정 절차를 거쳐야한다.
        
- 통계적 가설 검정 : 유의확률을 이용해서 가설을 검정하는 방법

- 유의확률
  : 실제로는 집단 간 차이가 없는데 우연히 차이가 있는 데이터가
    추출될 확률
  
  1) 분석 결과 유의확률이 크게 나타났다면
    -> 집단 간 차이가 통계적으로 유의하지 않다고 해석
    -> 실제로는 차이가 없더라도 우연에 의해 이 정도의 차이가
        관찰될 가능성이 크다는 의미
  
  2) 분석 결과 유의확률이 작게 나타났다면
    -> 집단 간 차이가 통계적으로 유의하다고 해석
    -> 실제로는 차이가 없는데 우연히 이 정도의 차이가 관찰될 가능성이
      작다, 우연이라고 보기 힘들다는 의미
'

### t검정(t-test) - 두 집단의 평균 비교
## 두 집단의 평균에 통계적으로 유의한 차이가 있는지 알아볼 때 사용하는 기법

## compact 자동차와 suv 자동차의 도시 연비 t 검정

mpg <- as.data.frame(ggplot2::mpg)
library(dplyr)
mpg_diff <- mpg %>%
  select(class, cty) %>%
  filter(class %in% c('compact','suv'))
head(mpg_diff)
table(mpg_diff$class)

## t-test
t.test(data=mpg_diff, cty ~ class, var.equal = T)

' 해석법
유의확률 0.05 기준

p-value < 2.2e-16 
-> compact와 suv 차량의 도심 연비 차이가 통계적으로 유의하다.
                
mean in group compact     mean in group suv 
             20.12766              13.50000 
-> compact 차는 평균 도심 연비가 20인 반면, suv 는 13이므로
  compact 차가 도심연비가 더 높다.
'

### 일반 휘발유와 고급 휘발유의 도시연비 t 검정
mpg_diff2 <- mpg %>%
  select(fl, cty) %>%
  filter(fl %in% c('r','p'))

table(mpg_diff2$fl)

t.test(data=mpg_diff2, cty~fl, var.equal=T)
'
p-value = 0.2875

일반 휘발유와 고급 휘발유에 따른 도심 연비 차이가 통계적으로
유의하지 않다.
'