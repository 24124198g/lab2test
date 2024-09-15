
import json

# 读取 JSON 文件
with open('student.json', 'r') as file:
    data = json.load(fisle)

# 获取学生列表
students = data['students']

# 列出所有学生
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

#print the second student's name
print(students[1]['name'])