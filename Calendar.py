import streamlit as st
st.markdown("#Calendar")
import calendar

# Get current year and month
current_year = calendar.datetime.datetime.now().year
current_month = calendar.datetime.datetime.now().month

# Create a calendar for the current month
cal = calendar.monthcalendar(current_year, current_month)

# Convert calendar to HTML table
html_table = "<table style='width: 100%;'>"
html_table += "<tr><th colspan='7'>{}</th></tr>".format(calendar.month_name[current_month])
html_table += "<tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>"

for week in cal:
    html_table += "<tr>"
    for day in week:
        if day == 0:
            html_table += "<td></td>"
        else:
            html_table += "<td>{}</td>".format(day)
    html_table += "</tr>"

html_table += "</table>"

# Display the calendar in Streamlit
st.markdown(html_table, unsafe_allow_html=True)
