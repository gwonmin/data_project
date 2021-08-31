#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("20년 10월.csv", encoding = 'cp949')

#구매자 지역 정보 데이터에서 ~시, ~군만 추출한 리스트

df_sigun = df["주소"].str.extract('(\w*시)|(\w*군)')

si_list = [i for i in df_sigun.dropna(subset = [0])[0]]

gun_list = [i for i in df_sigun.dropna(subset = [1])[1]]

sell_list = si_list + gun_list


#국내 시, 군 지역 리스트

df_region = pd.read_excel("전국행정동리스트.xlsx")

region_list = [i for i in df_region['Unnamed: 1']]

region_set = set(region_list)

region_set.remove('시 / 군')

region_set.update(['광주광역시', '대구광역시', '대전광역시', '부산광역시',
                  '세종특별자치시', '서울특별시', '울산광역시', '인천광역시', '제주시'])

sigun_list = list(region_set)


def count_dict(key_list, target_list): # key_list를 기준으로 target_list를 비교하여 카운트
    result = {}
    
    for key in range(len(key_list)):
        count = 0

        for target in target_list:
            if key_list[key] == target:
                count += 1
            else:
                pass

        result[key_list[key]] = count
        
    return result

def descending_order(dic): # Value값을 기준으로 내림차순 정렬
    return dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))

def drawbar_top10(dic): #상위 10개 값만 차트로 출력
    x, y = zip(*dic.items()) #key, value 튜플 형식으로 나누기 리턴값은 리스트

    plt.bar(x[:10], y[:10])
    plt.rcParams['figure.figsize'] = [10, 5]

    

final_dict = descending_order(count_dict(sigun_list, sell_list))

del final_dict['서울특별시']                              

drawbar_top10(final_dict)

#서울시에 속하는 행정구 리스트

seoulgu_list = [i for i in df_region[df_region['전국행정동리스트'] == '서울특별시']['Unnamed: 2']]

seoulgu_set = set(seoulgu_list)

seoulgu_list = list(seoulgu_set) 

#구매자 지역 정보 데이터에서 ~구만 추출한 리스트

df_seoulgu = df["주소"].str.extract('(\w*구)')

sell_list = [i for i in df_seoulgu.dropna(subset = [0])[0]] 



seoul_dict = descending_order(count_dict(seoulgu_list, sell_list))

drawbar_top10(seoul_dict)





