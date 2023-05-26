# Training App

This is a training app that helps users create personalized workout routines based on their Garmin workout data. The app analyzes past workout performances, diet, and sleep data to prescribe a weekly workout routine aimed at weight loss and improving marathon times.

## Features

- Personalized workout routine generation based on user's Garmin workout data
- Support for running, cycling, cross-training, and strength training activities
- Integration with Garmin Connect to fetch workout data
- Customizable for multiple users with different goals and preferences

## Getting Started

To run the Training App locally, follow the instructions below:

### Prerequisites

- Python 3.7 or higher installed on your system
- Flask framework (`pip install flask`)

### Installation

1. Clone the repository:
git clone https://github.com/phillips4100/trainingcalculator.git


2. Navigate to the project directory:
cd TrainingApp


3. Install the required dependencies:
pip install -r requirements.txt


### Running the App

1. Set the Flask app environment variable:
- For Windows Command Prompt:
  ```
  set FLASK_APP=app.py
  ```
- For macOS/Linux Terminal:
  ```
  export FLASK_APP=app.py
  ```

2. Start the Flask development server:
flask run


3. Open your web browser and visit `http://localhost:5000` to access the Training App.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This app is developed using Flask, a micro web framework for Python.
- We thank Garmin for providing the workout data and API integration.
