
import streamlit as st

# 设置标题
st.title("简单的 Streamlit 应用")

# 创建输入框
user_input = st.text_input("请输入一些内容:")

# 创建提交按钮
if st.button("提交"):
    # 显示用户输入的内容
    st.write("你输入的内容是:", user_input)