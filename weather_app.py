import streamlit as st
import requests
import json
import pandas as pd

# 固定的天气数据 URL
url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en'

# 获取天气数据
result = requests.get(url)

# 解析 JSON 字符串为字典对象
result_dict = result.json()

# 提取温度数据
temperature_data = result_dict["temperature"]["data"]

# 创建 DataFrame
df = pd.DataFrame(temperature_data)

# 在侧边栏中添加选择框
location = st.sidebar.selectbox('选择地点', df['place'])

# 显示状态码
st.write("Status Code:", result.status_code)

# 显示选定地点的温度数据
st.write(f"Temperature data for {location}:")
temperature = df[df['place'] == location]['value'].values[0]
st.write(f"{temperature} °C")
st.write("Temperature data:")
st.bar_chart(df.set_index('place')['value'])
