import streamlit as st
import json

st.success("先在下面选择学期，然后点击再下面的链接（注意看主页的注意事项），再把网页的所有内容粘贴到下面的文本输入区里。")
choiceSemester=(
      '2021-2022-1',
      '2021-2022-2',
      # '2021-2022-3',
      '2022-2023-1',
      '2022-2023-2',)
semester = st.selectbox(
     '选择学期(默认最新学期)',choiceSemester,index=len(choiceSemester)-1)

"**查询课表请求网址**"
st.write(f"https://egate.shanghaitech.edu.cn/publicapp/sys/mykbxt/api/getMyTimeTableList.do?weekOfTerm=1&schoolYearTerm={semester}")

coursesinput=st.text_area("fni3e3", placeholder="请把结果粘贴到这里", height=500,label_visibility="hidden")
#json prase
if(coursesinput!=""):
      # st.success("课表读取成功,在下面可以预览（太长可以点🔻收起来）")
      st.success("课表读取成功")
      jCon = json.loads(coursesinput)
      # st.json(jCon)
      courses = []
      coursesFlags = []
      for _,unknown in jCon["timeTable"].items():
            for _,courseInfor in unknown.items():
                  # print("====="+courseInfor["name"])
                  if courseInfor!=None and not courseInfor["name"] in coursesFlags:
                        coursesFlags.append(courseInfor["name"])
                        courses.append({
                  "name": courseInfor["name"],
                  "startT": courseInfor["section"].split("-")[0],
                  "endT": courseInfor["section"].split("-")[1],
                  "weekday": courseInfor["weekday"],
                  "classid": courseInfor["classId"],
                  "room": courseInfor["classroom"]
                  })

      # coursesURLShow=[]
      st.table(courses)

      for course in courses:
            courseName = course["name"];
            startT = course["startT"];
            endT = course["endT"];
            weekday = course["weekday"];
            classid = course["classid"];
            room = course["room"];

            courseURL = f"https://egate.shanghaitech.edu.cn/publicapp/sys/mykbxt/api/queryCourseMembers.do?classId={classid}&skzc=1&skxq={weekday}&ksjc={startT}&jsjc={endT}&jasmc={room}";
            # coursesURLShow.append([courseName,courseURL])
            st.write(f'<a href="{courseURL}" target="_blank">{courseName}</a>', unsafe_allow_html=True)
            # coursesURLShow.append([courseName,"<a>dw</a>"])

      "同样的，你可以把上面点出来的丑不拉几的代码复制到下面，可以得到一个更清楚的表格"
      namelist=st.text_area("namelist12338", placeholder="把课程名单复制到这里", height=300,label_visibility="hidden")
      if namelist!="":
            namelistDic=json.loads(namelist)
            namelistForShow=[]
            for teacher in namelistDic["teachers"]:
                  namelistForShow.append([teacher["NAME"]+"(老师)",teacher["ID"]])
            for student in namelistDic["students"]:
                  namelistForShow.append([student["NAME"],student["ID"]])
            st.table(namelistForShow)
