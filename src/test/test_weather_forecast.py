import unittest 
from unittest.mock import Mock, patch
import datetime
import requests
import json
from main import get_weather, display_air_pollution_chart

class TestWeatherApp(unittest.TestCase):
    @patch('requests.get')
    def test_get_weather(self, mock_requests_get):
        # Mock response from OpenWeatherMap API
        mock_response_weather = Mock()
        mock_response_weather.json.return_value = {
            "weather": [{"main": "Clear", "description": "clear sky"}],
            "main": {"temp": 288.15, "pressure": 1015, "humidity": 50},
            "wind": {"speed": 2.1},
            "dt": 1645122000  # Unix timestamp
        }
        mock_requests_get.side_effect = [mock_response_weather]

        # Mock response from OpenAQ API
        mock_response_airpollution = Mock()
        mock_response_airpollution.json.return_value = {
            "results": [{
                "measurements": [
                    {"parameter": "pm25", "value": 10},
                    {"parameter": "pm10", "value": 20},
                    {"parameter": "o3", "value": 30},
                    {"parameter": "no2", "value": 40}
                ]
            }]
        }
        mock_requests_get.side_effect.append(mock_response_airpollution)

        # Mock geocode response
        with patch('geopy.geocoders.Nominatim') as mock_geolocator:
            mock_geolocator.return_value.geocode.return_value.latitude = 40.7128
            mock_geolocator.return_value.geocode.return_value.longitude = -74.0060

            # Mock timezone response
            with patch('timezonefinder.TimezoneFinder.timezone_at') as mock_timezone_at:
                mock_timezone_at.return_value = 'America/New_York'

                # Patch datetime.now to return a fixed time
                with patch('datetime.datetime') as mock_datetime:
                    mock_datetime.now.return_value = datetime.datetime(2023, 2, 17, 12, 0, 0)

                    # Run get_weather
                    get_weather()

                    # Assertions
                    self.assertTrue(mock_requests_get.called)
                    # Add more assertions as needed

    def test_display_air_pollution_chart(self):
        # Test with valid data
        pm25, pm10, o3, no2 = 10, 20, 30, 40
        # Suppressing plot display using plt.show()
        with patch('matplotlib.pyplot.show'):
            display_air_pollution_chart(pm25, pm10, o3, no2)
            # You can add assertions here to verify the behavior of display_air_pollution_chart function

if __name__ == '__main__':
    unittest.main()
