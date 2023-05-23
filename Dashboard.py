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

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Calculate metrics
availability_count = df['availability'].count()
network_performance_percentage = (df['network performances'] == 1).mean() * 100
incidents_count = df['new incidents'].sum()

# Create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# Fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="Availability",
    value=availability_count
)

kpi2.metric(
    label="Network Performances",
    value=f"{network_performance_percentage:.2f}%"
)

kpi3.metric(
    label="New Incidents",
    value=incidents_count
)

selected_kpi = st.session_state.get('selected_kpi', None)

# Define the CSS styles for selected and unselected metrics
kpi_styles = {
    'kpi1': 'background-color: #333333; color: white;',
    'kpi2': 'background-color: #333333; color: white;',
    'kpi3': 'background-color: #333333; color: white;'
}



# Update the selected_kpi session state
st.session_state.selected_kpi = selected_kpi

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
            st.markdown("### Number of Incidents per Cluster")
            figure2 = px.histogram(data_frame=df, x="new incidents", color="clusters")
            st.plotly_chart(figure2)   



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
# Create a new column with the hyperlink
#filtered_df['Details'] = filtered_df.apply(lambda row: f'<a href="/details/{row["Datacenters"]}/{row["Clusters"]}">Details</a>', axis=1)

# Display the table with the hyperlink
#st.write(filtered_df[['Datacenters', 'Clusters', 'Details']].rename(columns={'Datacenters': 'Datacenter', 'Clusters': 'Cluster'}), unsafe_allow_html=True)



st.table(filtered_df)

