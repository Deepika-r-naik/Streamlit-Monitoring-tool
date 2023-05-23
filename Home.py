import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import altair as alt

import numpy as np  # np mean, np random

st.set_page_config(page_title="Observability Monitoring Tool", page_icon=":bar_chart:", layout="wide")


# Add menu bar options
st.markdown("---")


menu_options = ["Home", "Dashboard", "Search", "Settings", "Contact"]

#  menu options
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


# Create columns for arranging the charts
fig_col1, fig_col2 = st.columns(2)

# Display the third chart (Network Performance per Cluster)
with fig_col1:
    st.markdown("### Network Performance per Cluster")
    fig1 = px.density_heatmap(data_frame=df, y="clusters", x="network performances")
    st.plotly_chart(fig1)

# Display the fourth chart (Number of Incidents per Cluster)
with fig_col2:
    st.markdown("### Number of Incidents per Cluster")
    fig2 = px.histogram(data_frame=df, x="new incidents", color="clusters")
    st.plotly_chart(fig2)

# Display the fifth chart (Memory and Storage per Cluster)
st.markdown("### Memory and Storage per Cluster")
chart_data = pd.DataFrame({
    'Clusters': df['clusters'],
    'Metric': np.random.choice(['Memory', 'Storage'], size=len(df)),
    'Value': np.random.randint(0, 100, size=len(df))
})

c = alt.Chart(chart_data).mark_bar().encode(
    x='Clusters',
    y='Value',
    color='Metric',
    tooltip=['Clusters', 'Metric', 'Value']
).interactive()

st.altair_chart(c, use_container_width=True)

