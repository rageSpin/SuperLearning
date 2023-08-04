import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="SuperLearning",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### This is SuperLearning. A small collection of Giannini Stefano's university notes."
    }
)

st.title("🎓SuperLearning📚")

# st.write("## Table of Contents")
# st.markdown('[Monte Carlo Modeling](http://localhost:8501/Monte_Carlo_Modeling#monte-carlo-modeling-of-carrier-transport-in-crystalline-materials)')