#导入对应的库
import streamlit as st

#插入侧边栏
with st.sidebar:
    name = st.text_input('请输入您的名字')
    if name:
        st.write(f"您好，{name}")
    password = st.text_input('请输入您的密码', type='password')

#插入布局并分成3列,参数值代表列宽
column1,column2,column3 = st.columns([1,2,1.5])
with column1:
    age = st.number_input('请输入您的年龄', value=20, min_value=0, max_value=100, step=5)
    st.write(f"您好，您的年龄是{age}")
with column2:
    paragraph = st.text_area('请输入您的自我介绍')
with column3:
    address = st.text_area('请输入您的住址')
    st.write(f"您好，您的住址是{address}")

#插入选项卡
tab1,tab2,tab3 = st.tabs(["性别","联系方式","喜好水果"])
with tab1:
    gender = st.radio('您的性别是', ["男","女"],index=None)
    if gender:
        st.write(f"您的性别为{gender}")
    st.divider()
with tab2:
    contact = st.selectbox("您希望通过什么方式联系？", ["电话", "微信", "QQ", "邮件", "其他"], index=None)
    if contact:
        st.write(f"您希望通过{contact}联系")
    st.divider()
with tab3:
    fruits = st.multiselect("您喜欢的水果是什么？", ["香蕉", "苹果", "橙子", "葡萄", "其他"])
    for fruit in fruits:
        st.write(f"您喜欢的水果有{fruit}")
    st.divider()

#插入折叠展开卡片
with st.expander("身高信息"):
    height = st.slider("您的身高是多少厘米？", value=160, min_value=140, max_value=200, step=1)
    st.write(f"您的身高是{height}厘米")