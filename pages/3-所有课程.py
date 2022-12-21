import streamlit as st
import os
import json
from Crypto.Cipher import AES

@st.cache
def getChallenge():
    return os.getenv('CHALLENGE')
challenge = getChallenge()

@st.cache
def getData(key:str):
    key = key.encode("utf-8").ljust(16, b"\0")
    with open("res/courses_en.json", "rb") as file:
        data=file.read()
        cipher = AES.new(key, AES.MODE_ECB)
        AES_de_str = cipher.decrypt(data)
        AES_de_str = AES_de_str.strip()
        AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str


col1,col2 =st.columns(2)
with col1:
    st.warning("想要看我校的课程？请先回答下面的问题。")
with col2:
    st.image("https://i.postimg.cc/3w1kFX3G/3263d58a7a2354e5f04a71a2ecd622bb.jpg")
useranswer=st.text_input("信导的课程代号是啥(大小写不敏感)：")
# if st.button("提交"):
if useranswer!="":
    if challenge == useranswer.upper():
        coursesTable=[]
        with st.empty():
            st.image("https://i.postimg.cc/VLRsTjSL/v2-a284fb5c84d8e47f2fe6d63a8c47bbfd-r.jpg",width=200)
        data = getData(challenge).replace("\x00","")
        data = json.loads(data)
        for course in data:
            coursesTable.append([course["课程代码"],course["课程名称"],course["课程安排"],course["classid"]])
        st.table(coursesTable)
    else:
        st.image("https://i.postimg.cc/brJcRr4g/format-png.png")

