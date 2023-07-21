
import json
import re
import random
import streamlit as st
import os

st.title('填词游戏')
st.markdown('一个简单的文字游戏')

files = []
for root,ds,fs in os.walk('./'):
    for f in fs:
        if f.endswith('.json'):
            files.append(os.path.join(root,f))


file=st.radio("选择题库文件",files,key='file')
#st.write(file)
assign=st.radio('是否指定文章标题',['是','否'],key="assign")

def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
        data=json.load(f)
    
    return data

data = read_articles(file)
articles = data["articles"]

passages = []
for p in articles:
    passages.append(p["title"])

passage=st.radio('选择文章标题',passages,disabled=not (st.session_state.assign=='是'),key="passage")

index = 0


if(assign=='是'):
    for i in range(len(articles)):
        if articles[i]["title"]==passage:
            index = i

article = articles[index]["article"]
hints = articles[index]["hints"]

for i in range(len(hints)):
    st.text_input(label=hints[i],key="ans"+str(i))

    # for i in range(len(keys)):
    #     # TODO: 将 article 中的 {{i}} 替换为 keys[i]
    #     # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换
    #     article = re.sub("\{\{"+str(i+1)+"\}\}",keys.loc[i,"填入"],article)

save=st.radio("保存文件",['是','否'])

path=st.text_input(label="文件名称",disabled=(save=='否'))

if st.button(label="我写完了！"):
    for i in range(len(hints)):
        article = re.sub("\{\{"+str(i+1)+"\}\}",st.session_state.get("ans"+str(i)),article)
    st.write(article)
    if save=='是':
        fd = os.open("./logs/"+path,os.O_RDWR|os.O_CREAT)
        os.write(fd,bytes("\nOutput:\n"+article+"\n","utf-8"))


    

if __name__ == "__main__":
    pass


    


