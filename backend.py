import requests

API_KEY = "XXXXXXXXXX"


def get_data(city, n_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_items = 8 * n_days
    filtered_data = filtered_data[:no_items]
    return filtered_data


if __name__ == "__main__":
    print(get_data(city="colombo", n_days=2))
