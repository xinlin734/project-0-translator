import streamlit as st

st.title("Hello AI World")
st.write("如果你看到这句话，说明环境装好了。")

name = st.text_input("你叫什么？")
if name:
    st.write(f"你好，{name}！准备好开始 AI 之旅了吗？")