#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')


# In[3]:


import glob
import sys


# In[6]:


review=pd.DataFrame()

for f in glob.glob("C:\\Users\\82109\\Desktop\\4-2\\산공종설\\review*.xlsx"):
    data=pd.read_excel(f)
    
    columns =['구매자평점','리뷰상세내용']
    df = pd.DataFrame(data, columns=columns)
    review = review.append(df,ignore_index=True)
    
print(review.shape)

review.head()
    
#데이터 통합


# In[7]:


review.to_excel("C:\\Users\\82109\\Desktop\\4-2\\산공종설\\review_merge.xlsx",header=True,index=False)


# In[5]:


review_merge=pd.read_excel("C:\\Users\\82109\\Desktop\\4-2\\산공종설\\review_merge.xlsx")
review_merge.head()


# In[6]:


review_merge.rename(columns={review_merge.columns[0]:'rating',review_merge.columns[1]:'text'},inplace=True)
review_merge.head()#결과에 보면 중복 있는듯


# In[7]:


review_merge.isnull().sum()#결측치 확인 good


# In[8]:


review_merge.drop_duplicates(subset=['text'],inplace=True)#그래서 리뷰 중복제거


# In[9]:


print(review_merge.shape)#처음보다 많이 데이터가 줄어든거 봐서는 중복이 좀 있었던듯


# In[10]:


review_merge.head()


# In[45]:


review_merge.hist()#평점이 높은게 많긴 많은듯 일단


# In[11]:


print(review_merge.isnull().values.any())#null 값있는지 혹시 확인


# In[12]:


import re

def korean_extract(text):
    korean = re.compile('[^ ㄱ-ㅣ 가-힣]')#한글,공백 제외 제거
    result =korean.sub('',text)#text에 적용
    return result


# In[13]:


review_merge['text'][3]


# In[14]:


korean_extract(review_merge['text'][3])#적용 잘되는듯 good


# In[15]:


from konlpy.tag import Okt
from collections import Counter


# In[16]:


okt = Okt()
nouns = okt.nouns(korean_extract(review_merge['text'][0]))
nouns #형태소 분석인데 이거 저반사는 인식을 못해버리네 반사라는 명사로만 분석을 하니까 일단 skip


# In[17]:


all = "".join(review_merge['text'].tolist())#모든 리뷰를 묶어서 형태소 분석을 해보겠음
all


# In[18]:


nouns=okt.nouns(korean_extract(all))
print(nouns)#일단 역시나 쓸때없는것 엄청 나옴


# In[19]:


counter=Counter(nouns)#빈도수 제일 높은거 20개만체크 해보겠음
counter.most_common(20)


# In[20]:


counter1=Counter({x:counter[x] for x in counter if len(x)>1}) #것,때,감,더 이런 필요없는 1글자는 지워보도록
counter1.most_common(20)#지우고 다시 20개 체크


# In[21]:


stopwords=pd.read_csv("C:\\Users\\82109\\Desktop\\4-2\\산공종설\\불용어.csv",encoding="cp949")
#불용어 csv파일인데 여기에 계속 쓸만한게 아닌 단어들을 추가하는 방향으로 가면 좋을듯
stopwords


# In[22]:


nouns = [x for x in nouns if len(x)>1]
review_word = [x for x in nouns if x not in stopwords]
review_word


# In[51]:


from sklearn.feature_extraction.text import CountVectorizer#이제 요즘 배우는 정보검색론  bag of words 이걸 진짜 할줄은 몰랐네
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split


# In[31]:


#위에서 한것을 함수로 저장
def preprocessing(text):
    korean = re.compile('[^ ㄱ-ㅣ 가-힣]') 
    result = korean.sub('', text)
    okt = Okt()  
    nouns = okt.nouns(result)
    nouns = [x for x in nouns if len(x) > 1]  
    nouns = [x for x in nouns if x not in stopwords] 
    return nouns

vect = CountVectorizer(tokenizer = lambda x:preprocessing(x))
bow_vect = vect.fit_transform(review_merge['text'].tolist())
word=vect.get_feature_names()#단어 리스트
count=bow_vect.toarray().sum(axis=0)#단어 전체리뷰중 빈도수


# In[37]:


word_count=dict(zip(word,count)) #벌써 위에 가가 가각 가나다 이런 말도 안되는것들이 계속 나옴 이건 불용어 사전에 계속 추가해서 없애든 해야할듯
word_count#단어-빈도수 dictionary


# In[34]:


bow_vect.toarray()#단어들 리뷰별 등장횟수임 0 이 엄청 보이는걸로 봐서 리뷰들이 다 제각각일 확률이 있을듯


# In[36]:


print(vect.vocabulary_)#'싸용화따뽀뮨': 2546'미뀰먜뀰햬쪄쎠': 1577 이렇게 리뷰 쓰는건 왜 그러는 거냐 ㅋㅋㅋ


# In[42]:


tfidf=TfidfTransformer()
tfidfv=tfidf.fit_transform(bow_vect)#text에서 단어 등장 횟수와 등장한 text로 단어들마다 가중치 주는 것


# In[49]:


def rating_sort(rating):#일단 4,5점이 그래프 보면 많으니 이렇게 나눠보니까 차이가 확실히 많긴 많음
    if rating >3:
        return 1
    else:
        return 0

review_merge['y']=review_merge['rating'].apply(lambda x: rating_sort(x))
review_merge['y'].value_counts()


# In[52]:


x = tfidfv
y = review_merge['y']
x_train, x_valid, y_train, y_valid = train_test_split(x,y, test_size=0.3, random_state=1)


# In[53]:





# In[ ]:




