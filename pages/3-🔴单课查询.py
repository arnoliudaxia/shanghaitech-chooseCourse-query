import json
import streamlit as st

st.success("在v2.0版本之后，在「所有课程」页面里有的课程基本上都可以一键查询，不用在这里手填了。")
st.success("你需要完整填写下面所有输入框,然后点击「查询」按钮。")
classid=st.text_input("请输入classid", value="")

courseTimeColumn1,courseTimeColumn2 = st.columns(2)

with courseTimeColumn1:
      startT=st.text_input("课程从第几节开始", value="1")
      weekday=st.text_input("星期几的课", value="1")

with courseTimeColumn2:
      endT=st.text_input("课程到第几节结束", value="2")
      skzc=st.text_input("第几周（如果课程第一周就有填1就可以）", value="1")
jasmc=st.text_input("请输入上课地点", value="")

if st.button("「查询」"):
      if classid=="" or startT=="" or weekday=="" or endT=="" or skzc=="" or jasmc=="":
            st.error("请完整填写所有输入框")
            st.stop()
      queryURL=f"https://egate.shanghaitech.edu.cn/publicapp/sys/mykbxt/api/queryCourseMembers.do?classId={classid}&skzc={skzc}&skxq={weekday}&ksjc={startT}&jsjc={endT}&jasmc={jasmc}"
      st.write(queryURL)


"你可以把上面点出来的丑不拉几的代码复制到下面，可以得到一个更清楚的表格"
namelist=st.text_area("namelist12338", placeholder="把课程名单复制到这里", height=300,label_visibility="hidden")
if namelist!="":
      namelistDic=json.loads(namelist)
      namelistForShow=[]
      for teacher in namelistDic["teachers"]:
            namelistForShow.append([teacher["NAME"]+"(老师)",teacher["ID"]])
      for student in namelistDic["students"]:
            namelistForShow.append([student["NAME"],student["ID"]])
      st.table(namelistForShow)