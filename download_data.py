import requests

# URL for dataset
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-22-2022.csv"

# Download the file
response = requests.get(url)

# Save it in data folder
with open("data/covid_data.csv", "wb") as file:
    file.write(response.content)

print("✅ Dataset downloaded successfully!")
