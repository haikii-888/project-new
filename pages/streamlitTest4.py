#导入对应的库
import streamlit as st

#将变量的值储存在会话状态里
if "a" not in st.session_state:
    st.session_state.a = 0
clicked = st.button("加1")
if clicked:
    st.session_state.a = st.session_state.a + 1
st.write(st.session_state.a)
