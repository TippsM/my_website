import streamlit as st
import streamlit_extras.stylable_container as ste
import pandas as pd

def courses():

    st.divider()

    with st.expander("COP 2210 - Programming 1"):
        st.write("More Info...")

    with st.expander("COP 3337 - Programming 2"):
            st.write("More Info...")

    with st.expander("COP 3530 - Data Structures"):
            st.write("More Info...")

    with st.expander("COP 4338 - Systems Programming"):
            st.write("More Info...")

    with st.expander("COP 4710 - Database Management"):
            st.write("More Info...")

    with st.expander("CDA 3102 - Computer Architecture"):
            st.write("More Info...")

    with st.expander("CAP 4104 - Human-Computer Interaction"):
            st.write("More Info...")

    with st.expander("CEN 4010 - Software Engineering 1"):
            st.write("More Info...")

    with st.expander("CAP 4770 - Introduction to Data Mining"):
            st.write("More Info...")

    with st.expander("CAP 4630 - Introduction to Artificial Intelligence"):
            st.write("More Info...")

    with st.expander("MAD 2104 - Discrete Mathematics"):
            st.write("More Info...")

    with st.expander("MAD 3512 - Theory of Algorithms"):
            st.write("More Info...")

    with st.expander("CGS 3095 - Technology in the Global Arena"):
            st.write("More Info...")

    with st.expander("CJE 4694 - Cyber Crime"):
            st.write("More Info...")

    with st.expander("ISS 3613 - Issues in Global Cybersecurity Policy"):
            st.write("More Info...")


    st.divider()

def projects():

    with st.expander("Currency Exchange App"):
        st.write("More Info...")

    with st.expander("Event Discovery App"):
        st.write("More Info...")

    with st.expander("Password Management System"):
        st.write("More Info...")

    with st.expander("Spotify Recommender App"):
        st.write("More Info...")

    with st.expander("Bank System"):
        st.write("More Info...")

    with st.expander("QR Code Generator"):
        st.write("More Info...")

def message():
    st.markdown("Welcome to my page, my name is Matthew Allen Tipps! I’m a **Computer Science** student \n"
                "at Florida International University, aspiring to become a **Software Engineer**. \n"
                "Passionate about code, software, innovation, data, and integrity, I thrive on \n"
                "solving complex problems and pushing the boundaries of technology.")

    st.markdown("Currently, working as a **Research Learning Assistant**, conducting studies on student\n"
                "preferences for an online data science course, with **60+ students**, and exploring the impact\n"
                "of AI chatbots in virtual classrooms. My research aims to improve digital learning experiences\n"
                "by understanding how students engage with different class modalities.")

    st.markdown("I’m eager to contribute to the future of technology through impactful software solutions.\n"
                "Through courses I've taken, I’ve built a strong foundation in software development and problem-solving.")

    st.divider()

def socials():
    st.title("Socials 💬")
    st.write("\n")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button(label="GitHub 📁", url="https://github.com/TippsM/Portfolio")
    with col2:
        st.link_button(label="Linkedin 💼", url="https://www.linkedin.com/in/matthewtipps/")
    with col3:
        email = "mtipp001@fiu.edu"
        email_link = f"mailto:{email}"
        st.link_button(label="Send Email 📩", url=email_link)

    st.divider()

def text_container():

    with ste.stylable_container(
            key="container_with_border",

            css_styles= """ {
                background-color: #E5E4E2; 
                height: 600px;
                width: 800px;
                border: 1px solid rgba(0, 0, 0, 1);
                border-radius: 1rem;
                padding: 15px
            } """,
    ):

        col1, col2 = st.columns([2, 10])
        with col2:
            st.markdown("### **Matthew Allen Tipps**")
            st.markdown("#### **Computer Science Student (FIU)**")
            st.markdown("###### Miami, Florida")


        with col1:
            st.image("MT.png", width=100, use_container_width=False)

def skills():

    st.title("**Skills** 🛠️")
    soft_skills = ['Attention To Detail\Organization', 'Adaptability/Initiative',
                   'Teamwork', 'Problem-Solving']
    programming = ['Python', 'Java', 'C', 'SQL']
    tools = ['Microsoft Word/Excel', 'Google Collab', 'Notion', 'draw.io']

    images = ["MT.png", "java.jpeg", "c.jpeg", "sql.jpeg"]  # Image filenames



    technical_skills = {
        "Programming Languages": programming,
        "Tools": tools,
        "Soft Skills": soft_skills
    }

    df = pd.DataFrame(technical_skills)
    st.dataframe(df, hide_index=True)

    st.divider()

def education():

    st.subheader("Education 🎓")
    st.divider()

    with st.expander("Florida International University **(FIU)**"):
        st.divider()
        col1, col2, col3 = st.columns([4, 5, 3])
        with col1:
            st.write("2023 - 2025")
        with col2:
            st.write("**B.A in Computer Science**")
        with col3:
            st.write("Miami, Fl")

    with st.expander("Miami-Dade College **(MDC)**"):
        st.divider()
        col1, col2, col3 = st.columns([4, 5, 3])
        with col1:
            st.write("2020 - 2023")
        with col2:
            st.write("**A.A in Computer Science**")
        with col3:
            st.write("Miami, Fl")

    st.divider()

def work_experience():

    st.subheader("Work Experience 💼")
    st.divider()
    with st.expander("Florida International University **(FIU)**"):
        st.divider()
        st.write("""
        Explained and helped students understand fundamental concepts in Data Science operating Python programming and
Google Collab; in a class of 60+ students.
Conduct research on learning preferences, analyzing how students engage with different teaching formats in a data
science course.
Collect and evaluate student feedback, by way of surveys, identifying trends to improve course structure and
instructional methods.""")
        st.divider()
        col1, col2, col3 = st.columns([4, 6, 3])
        with col1:
            st.write("2023 - Present")
        with col2:
            st.write("**Research Learning Assistant**")
        with col3:
            st.write("Miami, Fl")

    with st.expander("BJ's Wholesale Club"):
        st.divider()
        st.write("More Info")
        st.divider()
        col1, col2, col3 = st.columns([4, 5, 1.5])
        with col1:
            st.write("2020 - 2021")
        with col2:
            st.write("**Produce Clerk**")
        with col3:
            st.write("Miami, Fl")

    with st.expander("Winn-Dixie"):
        st.divider()
        st.write("More Info")
        st.divider()
        col1, col2, col3 = st.columns([4, 6, 3])
        with col1:
            st.write("2019 - 2020")
        with col2:
            st.write("**Cashier/Produce Clerk**")
        with col3:
            st.write("Miami, Fl")

