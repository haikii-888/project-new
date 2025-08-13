#导入openai的聊天模型的方法
from langchain_openai import ChatOpenAI
#导入提示模版的方法
from langchain.prompts import ChatPromptTemplate

#定义AI请求的函数
def generate_script(subject, video_length, creativity, api_key):
    # 创建聊天模型
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, temperature=creativity,
                       openai_api_base = "https://api.aigc369.com/v1")

    #创建视频标题生成提示模版
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "请为'{subject}'这个主题的视频想一个吸引人的标题,用中文回答")
        ]
    )

    #创建视频脚本生成提示模版
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本,用中文回答。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。"""
             )
        ]
    )

    #用链串起组件的输入输出,分别是视频标题和视频脚本
    title_chain = title_template | model
    script_chain = script_template | model

    #对提示模版填入对应的值,并获得模型的回复
    title = title_chain.invoke({"subject": subject}).content
    script = script_chain.invoke({"title": title, "duration": video_length}).content

    #返回函数的结果
    return title, script

#测试函数的输入输出是否正确
#print(generate_script("sora模型", 1, 0.7,"sk-0wtpjlf3lFomPHiHhZVTyXwa7DVBPW4EKsA3u2dBD1clxeqq"))