import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['About Me', 'My Project', 'Contribution'],
        icons=['person', 'code-slash', 'chat-left-text-fill']
    )

# About Me section
if selected == 'About Me':
    st.title("I am :green[Revananda]")
    st.markdown("Hey there! I'm a tech enthusiast studying at Semarang State Polytechnic, diving into the world of backend development. With a toolbox packed with MySQL, Python, HTML, and Tailwinds CSS, I'm on a mission to solve tricky problems and create seamless solutions. Let's innovate and build the future together!")
    st.subheader(":green[Programming Language]")
    image1 = "mysql.png",
    image2 = "python.png"
    image3 = "html.png"
    image4 = "Tailwind CSS.png"
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(image1,width=70,caption="MySQL")
    
    with col2:
        st.image(image2,width=70,caption="Python")
    
    with col3:
        st.image(image3,width=70,caption="HTML")

    with col4:
        st.image(image4,width=70,caption="Tailwind CSS")
    
    st.header(":green[More About Me]")
    st.subheader(":blue[Why did you choose Information Technology as your field of study?]")
    st.markdown("Because I developed an interest in programming since high school, at the beginning of the semester, we were taught about computer mechanisms and beginner programming languages like C++. Since that day, I wanted to delve deeper into programming, and I realized that IT is much broader than I initially thought. Now, I am studying the path to becoming a back-end developer.")

    st.subheader(":blue[Why do you want to become a back-end developer?]")
    st.markdown("While my heart is set on back-end development, I also have a growing interest in front-end technologies. I believe that understanding both sides of development allows for better integration and a more cohesive user experience. I am always eager to learn new things and adapt to the ever-evolving tech landscape.")
    st.caption("Feedback My Portofolio")
    st.feedback("stars")
    
if selected == 'My Project':
    st.subheader(":blue[Project]")
    st.markdown("This is part of the project that I made at the beginning of the semester at polyteknik negeri semarang hopefully you are interested in following the development of projects on my github")
    st.caption("Website Portofolio HTML, Tailwind CSS")
    st.image("Project 1.png")
    st.caption("Software App Python")
    st.image("Project 2.png")
    st.caption("Website Portofolio Python")
    st.image("Project 3.png")
    st.caption("Feedback")
    st.feedback("stars")

if selected == 'Contribution':
    a, b = st.columns(2)
    c, d = st.columns(2)

    a.metric("Contribution", "6", "+1")
    b.metric("Commit", "6", "6")

    c.metric("Online", "Rarely", "-Busy")
    d.metric("Homework", "Too Much", "Always")