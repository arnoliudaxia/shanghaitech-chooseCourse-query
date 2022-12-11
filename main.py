import streamlit as st

st.warning("注意所有跳转到egate的链接打开后，需要你手动点一下地址栏在按一下回车（手机点击跳转）才会正常显示页面。这是egate系统本身的限制。(如果还不行就手动复制地址打开)")

"""
## 前言
笔者在22年9月选课的时候发现了很久以来的一个痛点有了解决方案：一直以来在egate里都无法看到谁选了什么课程，有时候知道课程名单是很有用的一件事情，如果有你认识的人选了你想选的课，
那么你就更有可能和他（她）一起上。\\
然后我在使用今日校园APP的时候，发现里面的接口可以去看到有谁选了这门课（只有一小部分），欣喜了一下然后赶紧抓包，果然抓到了egate的API😝。\\
在当时笔者写了一个小笔记记录原理，感兴趣的朋友可以[点这里](https://flowus.cn/share/105777d6-200e-460f-8c4d-7db16599dab9)。
"""

"## 食用方法"
st.write(r"既然是获取课程名单，当然要知道获取什么课啦，如果你想找你课程表里的某个课那非常简单直接跳转到「🔍课表查询」页面。反之，如果这课你没有选(不在你的课程表里)，那么请参照上面的笔记然后前往 「🔴单课查询」页面。")
st.error("声明：本服务仅仅模拟今日校园访问egate，不会上传任何数据，本项目的源代码已经开源在[GitHub](https://github.com/arnoliudaxia/shanghaitech-chooseCourse-query.git)，欢迎大家:star:。")