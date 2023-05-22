import pandas as pd
import plotly.express as px
import streamlit as st

import numpy as np  # np mean, np random




#st.set_page_config(page_title="Observability Monitoring Tool", page_icon=":bar_chart:", layout="wide")

st.title("Observability - Dashboard")


st.markdown(
    """
    <style>
    .sidebar {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #f6f6f6;
        border-radius: 20px;
        padding: 10px;
        width: 50px;
        margin-right: 20px;
    }
    .sidebar a {
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        color: #444444;
        margin-bottom: 10px;
        height: 75px;
        width: 500px;
        border-radius: 10px;
    }

    .sidebar .sidebar-content {
        width: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation icons
def main():
    # Add CSS styles to adjust icon width
    st.markdown(
        """
        <style>
        .sidebar {
            width: 200px; /* Adjust the width of the sidebar as per your requirements */
        }

        .sidebar a i {
            width: 100%; /* Set the width of the icons to 100% of their parent container */
            text-align: center; /* Center the icons horizontally */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add the sidebar with icons
    st.sidebar.markdown(
        """
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
        <div class="sidebar">
            <a href="/"><i class="fas fa-bars"></i></a>
            <a href="/"><i class="fas fa-search"></i></a>
            <a href="/"><i class="fas fa-home"></i></a>
            <a href="/"><i class="fas fa-flag"></i></a>
            <a href="/"><i class="fas fa-chart-pie"></i></a>
            <a href="/"><i class="fas fa-envelope"></i></a>
            <a href="/"><i class="fas fa-image"></i></a>
            <a href="/"><i class="fas fa-users"></i></a>
            <a href="/"><i class="fas fa-cog"></i></a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add the content of your app here

if __name__ == "__main__":
    main()

df = pd.read_csv("data.csv").rename(columns=str.lower)

 #Get unique datacenters for dropdown
datacenters = df['datacenters'].unique().tolist()


# top-level filters
selected_datacenter = st.selectbox("Select the Datacenter", pd.unique(datacenters))
#dc_filter = st.selectbox("Select the datacenter", pd.unique(df["Datacenters"]))



# creating a single-element container
placeholder = st.empty()

# dataframe filter
filtered_df = df[df['datacenters'] == selected_datacenter].copy()

# create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="Availability",
    value=("Availability"),
    
)

kpi2.metric(
    label="Network Performances",
    value="Network Performance",
)

kpi3.metric(
    label="New Incidents",
    value="New Incidents ",
    
)


#charts for observability
 # create two columns for charts

df = pd.read_csv("data.csv").rename(columns=str.lower)
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
            st.markdown("### Availability per cluster")
            fig = px.density_heatmap(
                data_frame=df, y="clusters", x="availability"
            )
            st.write(fig)
            
with fig_col2:
            st.markdown("### Availability Count")
            fig2 = px.histogram(data_frame=df, x="availability")
            st.write(fig2)            



# Define the symbols for different percentages
symbols = {0: "❌", 50: "🟡", 100: "✅"}

# Convert Availability, CPU, and Memory columns to symbols
filtered_df['availability'] = filtered_df['availability'].apply(lambda x: symbols.get(int(x.strip('%')), ""))
filtered_df['cpu'] = filtered_df['cpu'].apply(lambda x: symbols.get(int(x.strip('%')), ""))
filtered_df['memory'] = filtered_df['memory'].apply(lambda x: symbols.get(int(x.strip('%')), ""))

# Display cluster count, network performance, and new incidents count
cluster_count = filtered_df.shape[0]
network_performance_avg = filtered_df['cpu'].str.extract('(\d+)').astype(float).mean().item()  # Extract scalar value
new_incidents_count = filtered_df[filtered_df['availability'] != ""].shape[0]

filtered_df = filtered_df.drop(columns=['datacenters'])

st.markdown("### Detailed Data View")


#adding hyperlink

st.table(filtered_df)

