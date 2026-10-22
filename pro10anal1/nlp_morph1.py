# 행태소 분석
# 말뭉치(코퍼스, Corpus)는 자연어 연구, 언어 분석, 인공지능(AI) 학습을 위해 다양한 분야의 언어 자료를 컴퓨터가 읽고 처리할 수 있도록 모아 놓은 대규모 텍스트·음성·영상 데이터 집합
# 언어 자료를 컴퓨터가 읽고 처리할 수 있도록 모아놓은 대규모 텍스트,음성,영상 데이터
# 정의 : 사람이 실제로 쓰고 말한 언어자료를 수집,정제한 데이터.
# 문법연구, 번역시스템, 챗봇 등 다양한 언어 데이터 분석의 기초자료로 활용
# 형태소(Morpheme)는 의미를 가지는 가장 작은 단위를 말함.

# Token : 토큰(Token)이란 컴퓨터가 텍스트를 이해하고 연산할 수 있도록 문장, 단어,
#  형태소, 혹은 글자 단위로 쪼갠 의미를 지닌 최소한의 조각을 뜻합니다
# 토큰의 주요 유형: 단어 토큰(Word Token),형태소 토큰(Morpheme Token),서브워드 토큰(Subword Token),문자/바이트 토큰(Character/Byte Token)

# 영어 토큰(Token)화 
import nltk
from nltk.tokenize import word_tokenize

# 최초 실행 시 필요한 데이터 다운로드
# nltk.download("punkt")
# nltk.download("punkt_tab")

text = "I am studying Python with my friends at room"

# 1. 토큰화
tokens = word_tokenize(text)
print(tokens) # ['I', 'am', 'studying', 'Python', 'with', 'my', 'friends', 'at', 'room']
print()
# 품사 태깅
pos_tags = nltk.pos_tag(tokens)
print(pos_tags) # [('I', 'PRP'), ('am', 'VBP'), ('studying', 'VBG'), ('Python', 'NNP'), ('with', 'IN'), ('my', 'PRP$'), ('friends', 'NNS'), ('at', 'IN'), ('room', 'NN')]


print('\n\n한국어 토큰(Token)화---------------------------')
# pip install JPype1 <== java 컴파일러가 먼저 설치되어야 함
# 대표적인 한글 형태소 분석 라이브러리
from konlpy.tag import Okt, Kkma, Komoran

text = "나는 오늘 아침에 학교에 갔다. 가는 길에 국화가 피어 너무 아름다웠다."

print('okt ---------------')
okt = Okt()
print('형태소: ', okt.morphs(text))
print('품사태깅: ', okt.pos(text))
print('품사태깅(어간 표현):', okt.pos(text, stem=True)) # 원형 출력: 그래요 -> 원형 출력
print('명사 추출 : ', okt.nouns(text))

print('Kkma ---------------')
kkma = Kkma()
print('형태소: ', kkma.morphs(text))
print('품사태깅: ', kkma.pos(text))
print('명사 추출 : ', kkma.nouns(text))

print('Komoran ---------------')
komoran = Komoran()
print('형태소: ', komoran.morphs(text))
print('품사태깅: ', komoran.pos(text))
print('명사 추출 : ', komoran.nouns(text))
