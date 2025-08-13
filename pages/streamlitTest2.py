#导入对应的库
import streamlit as st

#插入明文输入框
name = st.text_input('请输入您的名字')
if name:
    st.write(f"您好，{name}")
st.divider()

#插入匿文输入框
password = st.text_input('请输入您的密码',type='password')
st.divider()

#插入段落输入框
paragraph = st.text_area('请输入您的自我介绍')
st.divider()

#插入数字输入框，value为默认数字,step为每次加减号增加或减少的值
age = st.number_input('请输入您的年龄',value=20,min_value=0,max_value=100,step=5)
st.write(f"您好，您的年龄是{age}")
st.divider()

#插入单选框
checked = st.checkbox("我同意以上条款")
if checked:
    st.write(f"感谢{name}您的同意")
else:
    st.write(f"{name}请点击同意以上条款")
st.divider()

#插入按钮
submitted = st.button("提交")
if submitted:
    st.write(f"{name}提交成功")
st.divider()

#插入单选按钮,默认选第一个选项，index来修改默认选项(0,1,None)
gender = st.radio("您的性别是什么？",["男性","女性"],index=None)
if gender:
    st.write(f"您的性别为{gender}")
st.divider()

#插入单选下拉框
contact = st.selectbox("您希望通过什么方式联系？",["电话","微信","QQ","邮件","其他"],index=None)
if contact:
    st.write(f"您希望通过{contact}联系")
st.divider()

#插入多选下拉框
fruits = st.multiselect("您喜欢的水果是什么？",["香蕉","苹果","橙子","葡萄","其他"])
for fruit in fruits:
    st.write(f"您喜欢的水果有{fruit}")
st.divider()

#插入滑块
height = st.slider("您的身高是多少厘米？",value=160,min_value=140,max_value=200,step=1)
st.write(f"您的身高是{height}厘米")
st.divider()

#插入文件上传器，type为允许的文件后缀
file = st.file_uploader("上传文件",type=['png','jpg','jpeg','txt'])
if file:
    st.write(f"您上传的文件名是：{file.name}")
    st.write(f"文件内容如下：{file.read()}")
