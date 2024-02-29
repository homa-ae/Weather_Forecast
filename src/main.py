"""
A simple weather application using tkinter to display weather and air pollution information for a given city.

Dependencies:
    - tkinter
    - messagebox
    - geopy.geocoders
    - timezonefinder
    - datetime
    - requests
    - pytz
    - json
    - matplotlib.pyplot

Functions:
    display_air_pollution_chart(pm25, pm10, o3, no2):
        Display air pollution data in a bar chart.

    get_weather():
        Retrieve weather and air pollution data for a given city, update the GUI with the retrieved information,
        and display a chart.

Usage:
    Run the script to open the Weather App GUI. Enter the city name in the search field and click the search icon
    to fetch and display weather and air pollution information.
"""


import tkinter as tk
from tkinter import messagebox
import geopy.geocoders
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import json
import matplotlib.pyplot as plt


# Function to display air pollution data in a bar chart
def display_air_pollution_chart(pm25, pm10, o3, no2):
    pm25 = 0 if pm25 is None else pm25
    pm10 = 0 if pm10 is None else pm10
    o3 = 0 if o3 is None else o3
    no2 = 0 if no2 is None else no2
    
    pollutants = ['PM2.5', 'PM10', 'O3', 'NO2']
    values = [pm25, pm10, o3, no2]

    plt.figure(figsize=(8, 6))
    plt.bar(pollutants, values, color=['blue', 'green', 'orange', 'red'])
    plt.xlabel('Pollutant')
    plt.ylabel('Concentration (µg/m³)')
    plt.title('Air Pollution Levels')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to retrieve weather and air pollution data for a given city,
# update the GUI with the retrieved information, and display a chart    
def get_weather():
    try:
        city = textfield.get()

        # Geocode the city to get latitude and longitude
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        lat, lng = location.latitude, location.longitude

        # Get timezone information
        obj = TimezoneFinder()
        timezone = obj.timezone_at(lng=lng, lat=lat)
        country_label.config(text=f"{location.address.split(',')[-1].strip()}")
        province_label.config(text=f"{location.address.split(',')[-2].strip()}")
        city_label.config(text=timezone.split("/")[1])   

        # Get local time
        home = pytz.timezone(timezone)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        time_label.config(text="LOCAL TIME")

        # Fetch weather data from OpenWeatherMap API
        api_key = "b31e93c76182bfd9c982dc3dcf4b1323" #"ab6f74b6a7e5f897c2f838d8be15cc98"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}" #f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        response = requests.get(api_url)
        weather_data = response.json()

        # Fetch air pollution data from OpenAQ API  
        api_url_airpollution = f"https://api.openaq.org/v1/latest?coordinates={lat},{lng}"
        response_airpollution = requests.get(api_url_airpollution)
        airpollution_data = response_airpollution.json()

        #
        # Remove duplicates from weather data
        cleaned_weather_data = {}
        # Assuming 'dt' field contains the timestamp
        timestamp = weather_data['dt'] 
        # Only keep the latest entry for each timestamp
        cleaned_weather_data[timestamp] = weather_data
        #

        # # Extract relevant air pollution information 
        # Check if air pollution data is available
        if 'results' in airpollution_data and airpollution_data['results']:
            airpollution_values = airpollution_data['results'][0]['measurements']
            pm25 = next((x['value'] for x in airpollution_values if x['parameter'] == 'pm25'), None)
            pm10 = next((x['value'] for x in airpollution_values if x['parameter'] == 'pm10'), None)
            o3 = next((x['value'] for x in airpollution_values if x['parameter'] == 'o3'), None)
            no2 = next((x['value'] for x in airpollution_values if x['parameter'] == 'no2'), None)
        else:
            pm25 = pm10 = o3 = no2 = "N/A"            

        # Extract relevant weather information
        # Here you would loop over the cleaned_weather_data dictionary and extract the required information
        # This code assumes that the cleaned data structure is the same as the original weather data structure
        for timestamp, data in cleaned_weather_data.items():
            condition = weather_data["weather"][0]["main"]
            #print(condition)
            description = weather_data["weather"][0]["description"]
            # Convert temperature to Celsius
            temp = int(weather_data["main"]["temp"]-273.15)
            pressure = weather_data["main"]["pressure"]
            humidity = weather_data["main"]["humidity"]
            wind = weather_data["wind"]["speed"]

            # Update labels with weather information
            #temp_label.config(text=f"{temp}°C")
            condition_label.config(text=f"{condition} | Feels similar to {temp}°C")
            wind_label_dots.config(text=wind)
            humidity_label_dots.config(text=humidity)
            description_label_dots.config(text=description)
            pressure_label_dots.config(text=pressure)

            # Update labels with air pollution information   
            pm25_label.config(text=f"PM2.5: {pm25} µg/m³")
            pm10_label.config(text=f"PM10: {pm10} µg/m³")
            o3_label.config(text=f"O3: {o3} µg/m³")
            no2_label.config(text=f"NO2: {no2} µg/m³")

            display_air_pollution_chart(pm25, pm10, o3, no2)         
        
    except Exception as error:
        print(error)
        messagebox.showerror("Weather App", "Invalid Entry!")       

# Create main application window
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.configure(bg="lightblue")  # Set background color to light blue

# Create search image label
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(root, image=search_image, bg="lightblue")
search_image_label.pack(pady=20, side=tk.TOP)

# Create widgets
textfield = tk.Entry(root, justify="center", width=14,
                    font=("poppins", 25, "bold"),
                    bg="lightblue", fg="#000000", border=0) 
textfield.place(x=300, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(root, image=search_icon, border=0,
                               cursor="hand2", bg="lightblue", command=get_weather)
search_icon_button.place(x=620, y=22)

# Create logo image label
logo_image = tk.PhotoImage(file="logo.png")
logo_image_label = tk.Label(root, image=logo_image, bg="lightblue")
logo_image_label.pack(side=tk.TOP)

# Create frame image label
frame_image = tk.PhotoImage(file="box.png")
frame_image_label = tk.Label(root, image=frame_image, bg="lightblue")
frame_image_label.pack(pady=10, side=tk.BOTTOM)

country_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
country_label.place(x=120, y=120)

province_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
province_label.place(x=120, y=150)

city_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
city_label.place(x=120, y=180)

time_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
time_label.place(x=120, y=230)

clock = tk.Label(root, font=("Helvetica", 15, "bold"), fg="#4b4bcc", bg="lightblue")
clock.place(x=120, y=270)

pm25_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
pm25_label.place(x=590, y=150)

pm10_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
pm10_label.place(x=590, y=180)

o3_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
o3_label.place(x=590, y=210)

no2_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
no2_label.place(x=590, y=240)

# Create labels for weather information
wind_label = tk.Label(root, text="WIND", font=("Helvetica", 15, "bold"),
                  fg="White", bg="#1ab5ef")
wind_label.place(x=120, y=400)

humidity_label = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"),
                  fg="White", bg="#1ab5ef")
humidity_label.place(x=280, y=400)

description_label = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"),
                  fg="White", bg="#1ab5ef")
description_label.place(x=450, y=400)

pressure_label = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"),
                  fg="White", bg="#1ab5ef")
pressure_label.place(x=670, y=400)

# Define labels for displaying weather information
#temp_label = tk.Label(root, font=("arial", 15, "bold"), fg="#e355cd")
#temp_label.place(x=590, y=170)

condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", bg="lightblue")
condition_label.place(x=590, y=270)

wind_label_dots = tk.Label(root, text="...", font=("arial", 20, "bold"),
                      bg="#1ab5ef", fg="#404040")
wind_label_dots.place(x=120, y=430)

humidity_label_dots = tk.Label(root, text="...", font=("arial", 20, "bold"),
                      bg="#1ab5ef", fg="#404040")
humidity_label_dots.place(x=280, y=430)

description_label_dots = tk.Label(root, text="...", font=("arial", 20, "bold"),
                      bg="#1ab5ef", fg="#404040")
description_label_dots.place(x=450, y=430)

pressure_label_dots = tk.Label(root, text="...", font=("arial", 20, "bold"),
                      bg="#1ab5ef", fg="#404040")
pressure_label_dots.place(x=670, y=430)

# Run the application
root.mainloop()
