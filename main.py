
import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
st.write(f"Based on {len(df['country'])} countries")

# Columns for dropdowns
columns = df.columns.tolist()
columns.remove('country')
formatted_columns = [col.replace("_", " ").title() for col in columns]

# X and Y Axis Selection for Scatter Plot
st.header("Scatter Plot Analysis")
option_x = st.selectbox("Select the data for the X-axis", formatted_columns)
option_y = st.selectbox("Select the data for the Y-axis", formatted_columns)

x_array = df[option_x.lower().replace(" ", "_")]
y_array = df[option_y.lower().replace(" ", "_")]

if 'Corruption' in [option_x, option_y]:
    color = df['corruption']
    st.subheader(f"{option_x} and {option_y} (with Corruption Levels)")
    st.write("More is the score, more the corruption is")
    figure1 = px.scatter(x=x_array, y=y_array, color=color, 
                         labels={"x": option_x, "y": option_y, "color": "Corruption"})
else:
    st.subheader(f"{option_x} and {option_y}")
    figure1 = px.scatter(x=x_array, y=y_array, 
                         labels={"x": option_x, "y": option_y})

st.plotly_chart(figure1)

# Country Comparison
st.header("Country Comparison")
selected_countries = st.multiselect("Select countries to compare", df['country'].tolist())

if selected_countries:
    comparison_data = df[df['country'].isin(selected_countries)].set_index('country')
    st.write(comparison_data)

# Trend Analysis (Dummy Implementation for Static Data)
st.header("Trend Analysis (Hypothetical)")
st.write("Note: Since we lack time-series data, this is a placeholder for future implementation.")
trend_x = st.selectbox("Choose a variable for trend analysis", formatted_columns)
trend_figure = px.line(df, x='country', y=trend_x.lower().replace(" ", "_"), title=f"Trend of {trend_x} across Countries")
st.plotly_chart(trend_figure)
