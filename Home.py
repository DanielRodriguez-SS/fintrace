import streamlit as st
import json
import altair as alt
import pandas as pd

with open("data/budget_data.json", 'r') as file:
    budget = json.loads(file.read())


distribution = budget['distribution']
# Sample data
data = pd.DataFrame(list(distribution.items()), columns=["Category", "Amount"])

custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
# Create a pie chart
base = alt.Chart(data).encode(
    theta=alt.Theta(field="Amount", type="quantitative", stack=True),
    radius=alt.Radius("Amount", scale=alt.Scale(type="sqrt", zero=True, rangeMin=50)),
    color=alt.Color(field="Category", type="nominal", scale=alt.Scale(domain=data['Category'], range=custom_colors)),
    tooltip=["Category", "Amount"]
)

donut = base.mark_arc(innerRadius=20, stroke="#000")

text = base.mark_text(radiusOffset=30).encode(
    text=alt.Text(field="Category", type="nominal")
)

chart = donut + text

st.markdown("<h1>Distribution</h1>", unsafe_allow_html=True)

# Display in Streamlit
st.altair_chart(chart, use_container_width=True)

st.markdown("<h1>Details</h1>", unsafe_allow_html=True)

data['Percent %'] = (data['Amount']*100)/10000

st.dataframe(data, hide_index=True, use_container_width=True)