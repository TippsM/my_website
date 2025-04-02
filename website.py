import streamlit as st
import main_functions
import requests

url = "https://drive.google.com/uc?export=download&id=1pi6WVdYVrFMtnvr5LoF3bJQUASIicqmF"
response = requests.get(url)

resume = response.content
#---------------------------------------
main_functions.text_container()

st.write("\n" * 2)


home_page, projects, courses, experience = st.tabs(
    ['Home Page 🏠', 'Projects 👨🏻‍💻', 'Courses 📚', 'Experience 🎓'])


with home_page:
    st.title("About Me 🍎")
    st.download_button(label="**Download** Resume 📄", mime="application/pdf",
                       data=resume, file_name="Matthew_Tipps_Resume.pdf")

    st.divider()
    main_functions.message()
    main_functions.skills()
    main_functions.socials()


with projects:
    st.title("Projects 👨🏻‍💻")
    st.subheader("Personal and Group Projects")
    st.divider()
    main_functions.projects()

with courses:
    st.title("Courses 📚")
    st.subheader("Completed Courses Information")

    main_functions.courses()

with experience:
    st.title("Experience 🎓")
    st.divider()
    main_functions.work_experience()
    st.divider()
    main_functions.education()



