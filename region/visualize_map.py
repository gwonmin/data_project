#!/usr/bin/env python
# coding: utf-8

import folium
import region
import json
import webbrowser


#region.py 에서 불러온 데이터
seoulgu_dict = region.seoul_dict

#folium이 지원하는 데이터 타입에 맞추기 위해 DataFrame으로 변환
data = region.pd.DataFrame(list(seoulgu_dict.items()),
                          columns = ['지역', '판매량'])


#한국 시, 군, 구별 지리정보 json 파일 불러오기

with open('TL_SCCO_SIG_WGS84.json', encoding='UTF8') as f:
    geo_data = json.load(f)


#서울시 행정구별 판매량 히트맵으로 시각화

m = folium.Map(location = [37.5642135, 127.0016985], tiles = "OpenStreetMap", zoom_start = 11)

m.choropleth(geo_data = geo_data,
            name = 'choropleth',
            data = data,
            columns = ['지역', '판매량'],
            key_on = 'feature.properties.SIG_KOR_NM',
            fill_color = 'YlGn',
            fill_opacity = 0.7,
            line_opacity = 0.5,
            legend_name = '지역별 판매량')

folium.LayerControl().add_to(m)

#html에서 열고 싶은 경우 아래 코드 활성화
#m.save('folium_kr.html')
#webbrowser.open_new("folium_kr.html")




