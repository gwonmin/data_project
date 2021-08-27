#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("아이펠리/20년 10월.xlsx")

region_df = pd.read_excel("지역정보리스트.xlsx")

region_df = region_df.drop([0, 1], axis = 0)

a = set()

시_list = region_df['전국행정동리스트'].str.extract('(\w*시)').dropna(subset = [0])

군_list = region_df['전국행정동리스트'].str.extract('(\w*군)').dropna(subset = [0])

df_region = df["주소"].str.extract('(\w*시)|(\w*군)')

df_a = df_region[df_region[1].isna() == True]

df_a[df_a[0].isna() == True]

df.iloc[1368]

시_list = [i for i in df_region.dropna(subset = [0])[0]]

군_list = [i for i in df_region.dropna(subset = [1])[1]]

#hi





