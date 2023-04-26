from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Elishah J Policape Resume (1).pdf"
profile_pic = current_dir / "assets" / "eli_pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Eli Policape"
PAGE_ICON = ":wave:"
NAME = "Eli Policape"
DESCRIPTION = """
Data Analyst & Data Scientist who thoroughly enjoys researching, gathering data, creating graphs, interactive maps and dashboards.
"""
EMAIL = "policapee@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/eli-p-96312163/",
    "GitHub": "https://github.com/theeliad",
}
PROJECTS = {
    "🏆 Geospatial Weather App -  You can search on an U.S Map, NWS weather stations and with just one click show the forecast.": "https://theeliad-geospatial-weather-app-main-rmv7ho.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Experienced extracting actionable insights from data
- ✔️ Moderate hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 💻 Programming: Python (MatPlotLib, Numpy, Pandas, GeoPandas), SQL, VBA
- 📊 Data Visualization: Python (Folium, Plotly, Streamlit, DTale), MS Excel 
- 🌪️ Weather Database: Python (NWSAPy API, NOAA API, NOAA-Coops)
- 📚 Machine Learning Modeling: Neural Network (Temporal Convolution Network (TCN), Long Short-Term Memory (LSTM), Recurrent Neural Network (RNN)
- 🗄️ Databases: PostgreSQL, SQLite, Pycharm, Spyder 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Lead Technical Support Specialist | ERT**")
st.write("08/2017 - 01/2020")
st.write(
    """
- ► Accurately document and monitor help desk tickets/resolutions for compliance and auditing.
- ► Cross functionally collaborates with internal and external partners to review and investigate data trends.
- ► Provide technical assistance, ongoing training, and professional development opportunities by evaluating quality assurance metrics and auditing.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Simplisafe | Sales Technician**")
st.write("08/2015 - 08/2017")
st.write(
    """
- ► Increased departmental sales goals by 26%, leading my team in sales and retention metrics.
- ► Composed detailed call reports, territory sales plans and forecasts in order to expand sales opportunities.
- ► Evaluated client product needs while identifying additional sales opportunities.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**212 Consulting | Account Manager**")
st.write("05/2013 - 10/2014")
st.write(
    """
- ► Forecast and track key account metrics.
- ► Collaborated with key stakeholders to develop business strategies that meet organizational goals.
- ► Overhauled client onboarding processes, which improved client engagement by 25%
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**City of Lowell | Technical Assistant**")
st.write("05/2013 - 10/2014")
st.write(
    """
- ► Completed appropriate paperwork, documentation, and system entry.
- ► Collaborated with peers to promote effective data and technology resource management.
- ► Overhauled client onboarding processes, which improved client engagement by 25%
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Publications")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")