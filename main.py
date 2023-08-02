import streamlit as st
import plotly.express as px
from backend import get_data

# Add GUI options
st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days.")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))


if place:
    try:
        st.subheader(f"{options} for the next {days} days in {place}")
        # Get data
        filtered_data = get_data(place, days)

        # Create temp plot
        if options == "Temperature":
            temperature = [data_row["main"]["temp"] / 10 for data_row in filtered_data]
            dates = [data_row["dt_txt"] for data_row in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        # Create image
        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [data_row["weather"][0]["main"] for data_row in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=100)
    except KeyError:
        st.write('Entered place is not exist')