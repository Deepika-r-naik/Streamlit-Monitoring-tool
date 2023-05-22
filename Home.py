import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

import numpy as np  # np mean, np random

st.set_page_config(page_title="Observability Monitoring Tool", page_icon=":bar_chart:", layout="wide")




# Add menu bar options
st.markdown("---")


menu_options = ["Home", "Dashboard", "Search", "Settings", "Contact"]

# Create a div container for the menu options
menu_container = st.empty()
with menu_container:
    st.markdown(
        '<style>div.row-widget.stButton > div{display:flex; flex-direction:row; margin-top: -20px;}</style>',
        unsafe_allow_html=True
    )
    cols = st.columns(len(menu_options))

    for i, col in enumerate(cols):
        if col.button(menu_options[i]):
            if menu_options[i] == "Home":
                st.title("Home Page")
                # Add your home page content here

            elif menu_options[i] == "Dashboard":
                st.title("Dashboard Page")
                # Add your dashboard page content here

            elif menu_options[i] == "Search":
                st.title("Search Page")
                # Add your search page content here

            elif menu_options[i] == "Settings":
                st.title("Settings Page")
                # Add your settings page content here

            elif menu_options[i] == "Contact":
                st.title("Contact Page")
                # Add your contact page content here


#st.title("Observability Monitoring Tool")

st.markdown("---")




df = pd.read_csv("data.csv").rename(columns=str.lower)




#charts for observability
 # create two columns for charts

df = pd.read_csv("data.csv").rename(columns=str.lower)
fig_col1, fig_col2 = st.columns(2)
fig_col3, fig_col4 = st.columns(2)
with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="clusters", x="availability"
            )
            st.write(fig)
            
with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="availability")
            st.write(fig2) 

with fig_col3:
    st.markdown("### Third Chart")
    fig3 = px.histogram(data_frame=df, x="availability")
    st.write(fig3) 


