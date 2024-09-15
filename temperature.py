import json

# 从文件中读取 JSON 数据
with open('weather.json', 'r') as f:
    data = json.load(f)

# 提取温度信息
temperature_data = data.get('temperature', {}).get('data', [])

# 打印不同位置的温度信息
for location in temperature_data:
    place = location.get('place')
    value = location.get('value')
    unit = data.get('temperature', {}).get('unit')
    print(f"Location: {place}, Temperature: {value} {unit}")
    