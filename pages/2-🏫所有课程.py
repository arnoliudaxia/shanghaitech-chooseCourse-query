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
coursesTable=[]
filtedCoursesTable=[]
queryURLs={}
week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
if 'Authed' not in st.session_state:
    st.session_state['Authed'] = 'None'
if useranswer!="" or st.session_state["Authed"]=="True":
    if challenge == useranswer.upper() or st.session_state["Authed"]=="True":
        st.session_state["Authed"]="True"
        with st.empty():
            st.image("https://i.postimg.cc/VLRsTjSL/v2-a284fb5c84d8e47f2fe6d63a8c47bbfd-r.jpg",width=200)
        if(len(coursesTable)==0):
            data = getData(challenge).replace("\x00","")
            data = json.loads(data)
            for course in data:
                coursesTable.append([course["课程代码"],course["课程名称"],course["课程安排"],course["classid"]])
                timeAndPlace=course["课程安排"].split(" ")
                if timeAndPlace[0]=="尚未排课" or len(timeAndPlace)<3:
                    queryURLs[course["课程代码"]]=None
                    continue
                if "\n" not in timeAndPlace[0]:
                    print(timeAndPlace[0])
                weekinfo=timeAndPlace[0].split("\n")[1]
                jieshuS=timeAndPlace[1][:-1].split("-")
                jieshuE=jieshuS[1]
                jieshuS=jieshuS[0]
                place=timeAndPlace[2]
                if "\n" in place:
                    place=place.split("\n")[0]
                # 构建查询url
                queryURLs[course["课程代码"]]=f'https://egate.shanghaitech.edu.cn/publicapp/sys/mykbxt/api/queryCourseMembers.do?classId={course["classid"]}&skzc=1&skxq={week_list.index(weekinfo)+1}&ksjc={jieshuS}&jsjc={jieshuE}&jasmc={place}'

            filtedCoursesTable=coursesTable.copy()
            
        # 筛选逻辑
        filterInputAera=st.empty()
        fcol1,fcol2 =st.columns(2)
        if "txt_userFilter" not in st.session_state:
            st.session_state["txt_userFilter"]=""
        with fcol1:
            if st.button("筛选"):
                filtedCoursesTable.clear()
                for course in coursesTable:
                    if st.session_state["txt_userFilter"] in course[0]+course[1]:
                        filtedCoursesTable.append(course)

        with fcol2:
            if st.button("清空筛选"):
                filtedCoursesTable=coursesTable.copy()
                st.session_state["txt_userFilter"]=""
        filterInputAera.text_input(label="userFilter",placeholder="筛选课程代号和课程名称，暂不支持正则",label_visibility="hidden",key="txt_userFilter")
        
        # 一键查询逻辑
        userGen=st.text_input(label="userGen",placeholder="你想查询的课程代号",label_visibility="hidden")
        if st.button("查询"):
            if userGen in queryURLs.keys():
                st.success("生成自动查询链接，如果无效请手动查询")
                st.write(queryURLs[userGen])
            else:
                st.error("无法自动查询,请手动查询")
        # 课程数据库or查询结果解析
        tabTable, tabResult = st.tabs(["课程数据库", "查询结果解析"])
        with tabTable:
            st.table(filtedCoursesTable)
        with tabResult:
            namelist=st.text_area("namelist12338", placeholder="把课程名单复制到这里", height=300,label_visibility="hidden")
            if namelist!="":
                namelistDic=json.loads(namelist)
                namelistForShow=[]
                for teacher in namelistDic["teachers"]:
                        namelistForShow.append([teacher["NAME"]+"(老师)",teacher["ID"]])
                for student in namelistDic["students"]:
                        namelistForShow.append([student["NAME"],student["ID"]])
                st.table(namelistForShow)
        
    else:
        st.image("https://i.postimg.cc/brJcRr4g/format-png.png",width=500)

