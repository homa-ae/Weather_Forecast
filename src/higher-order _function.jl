# Define a struct to represent weather data
struct WeatherData
    temperature::Float64
    humidity::Float64
    wind_speed::Float64
end

# Higher-order function to apply a weather prediction model
function apply_prediction_model(prediction_model::Function, weather_data::WeatherData)
    return prediction_model(weather_data)
end

# Example prediction models
predict_temperature(weather_data::WeatherData) = weather_data.temperature + 2.0
predict_humidity(weather_data::WeatherData) = weather_data.humidity * 1.1
predict_wind_speed(weather_data::WeatherData) = weather_data.wind_speed * 0.9

# Example weather data
example_weather_data = WeatherData(20.0, 0.6, 10.0)

# Apply prediction models to example weather data
predicted_temperature = apply_prediction_model(predict_temperature, example_weather_data)
predicted_humidity = apply_prediction_model(predict_humidity, example_weather_data)
predicted_wind_speed = apply_prediction_model(predict_wind_speed, example_weather_data)

# Print the predicted weather
println("Predicted Temperature: $predicted_temperature°C")
println("Predicted Humidity: $(predicted_humidity * 100.0)%")
println("Predicted Wind Speed: $predicted_wind_speed m/s")
