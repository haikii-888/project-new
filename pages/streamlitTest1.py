#导入对应的库
import streamlit as st
import pandas as pd

#添加网页标题
st.title("我的个人网页❤")

#添加分割线
st.divider()

#添加图片
st.image("qiuqiu.jpg",width=300)

#添加表格
excel = pd.DataFrame({'学号':[1001,1002,1003], '班级':['一班','二班','三班'],'成绩':[92,67,80]})
#打印交互式表格
st.dataframe(excel)
#打印普通表格
st.table(excel)

#可以直接使用markdown格式的文字
st.write("## 这里是用了write")

#可以不写write直接写字符串
"# 这里是不用write的文字"
#可以不写write直接写数字
a = 345*567
a
#可以不写write直接写列表
[11,22,33]
#可以不写write直接写字典
{"a":1,"b":2,"c":3}
