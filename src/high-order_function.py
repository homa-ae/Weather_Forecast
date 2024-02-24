# Define a class to represent weather data
class WeatherData:
    def __init__(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

# Higher-order function to apply a weather prediction model
def apply_prediction_model(prediction_model, weather_data):
    return prediction_model(weather_data)

# Example prediction models
def predict_temperature(weather_data):
    return weather_data.temperature + 2.0

def predict_humidity(weather_data):
    return weather_data.humidity * 1.1

def predict_wind_speed(weather_data):
    return weather_data.wind_speed * 0.9

# Example weather data
example_weather_data = WeatherData(20.0, 0.6, 10.0)

# Apply prediction models to example weather data
predicted_temperature = apply_prediction_model(predict_temperature, example_weather_data)
predicted_humidity = apply_prediction_model(predict_humidity, example_weather_data)
predicted_wind_speed = apply_prediction_model(predict_wind_speed, example_weather_data)

# Print the predicted weather
print(f"Predicted Temperature: {predicted_temperature}°C")
print(f"Predicted Humidity: {predicted_humidity * 100}%")
print(f"Predicted Wind Speed: {predicted_wind_speed} m/s")
