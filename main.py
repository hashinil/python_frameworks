import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days.")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")


def get_data(days):
    dates = ["2023-01-08", "2023-02-08", "2023-03-08"]
    temperature = [10, 15, 12]
    temperature = [temp * days for temp in temperature]
    return dates, temperature


d_val, t_val = get_data(days)
figure = px.line(x=d_val, y=t_val, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)