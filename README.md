# Flask Weather App

This is a simple Flask web application that fetches current weather data for a given city using the OpenWeatherMap API. The app displays temperature, weather conditions, and an icon representing the current weather.

## Features

- Search for current weather conditions by city.
- Displays temperature in Celsius, weather description, and "feels like" temperature.
- Dynamically fetches weather data from the OpenWeatherMap API.
- Uses Waitress as the production server for serving the Flask app.
- Custom error handling for invalid city names.


## Project Structure

## Requirements

- Python 3.x
- Flask
- Waitress
- requests
- python-dotenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-weather-app.git
    cd flask-weather-app
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your OpenWeatherMap API key:

    ```bash
    API_KEY=your_openweathermap_api_key
    ```

5. Run the Flask app:

    ```bash
    python app.py
    ```

6. Open the app in a web browser:

    ```
    http://localhost:8000
    ```

## Usage

1. Enter a city name on the homepage to fetch the current weather.
2. The app will display the city's current weather, including temperature, weather conditions, and an icon.
3. If an invalid city name is entered, the app will show an error message.

## Technologies Used

- **Flask**: Python web framework for building the application.
- **OpenWeatherMap API**: For fetching real-time weather data.
- **Waitress**: Production-grade WSGI server.
- **HTML/CSS**: Frontend UI.

## Screenshots

![weather1](https://github.com/user-attachments/assets/598a49c9-84f4-431e-8e32-87e11b44d294)
![weather2](https://github.com/user-attachments/assets/0f43055b-81f8-49a9-9c73-d699bbd60e25)
![weather3](https://github.com/user-attachments/assets/025606dc-ddd0-4fd9-9f1d-3f2d5bb02bea)
![weather4](https://github.com/user-attachments/assets/dd9858e1-80e8-482f-b5de-ebbafe72eff1)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

