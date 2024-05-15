# InVesTRv3
Application group to get information from google sheets and use AI to get insights about investments. The project stills under development and some features are incomplete.

## Overview
This project is a chatbot application designed to provide investment insights using integration from Google Sheets and Google Gemini. The application consists of a Python Flask API for backend functionality and a React frontend for the user interface.

The insights provided by Gemini is based in a prompt thats define how flat profit and percentage profit of a investment must be calculated, and how Gemini can provide insights from this definitions. Feel free to modify and test the prompt, located in service/src/utils/constants.py. In current state, it's necessary to reload the service when the sheet is changed, and it´s necessary to configure the conection with Google Sheets by itself. Improves will be implemented soon.

## Features
- **Integration with Google Sheets**: The chatbot fetches investment data from Google Sheets to provide insights to users.
- **Integration with Google Gemini**: Utilizes the Google Gemini API to retrieve detailed investment insights and analytics.
- **Interactive Chat Interface**: Users can interact with the chatbot through a user-friendly interface developed with React.

## Installation
1. Clone the repository:
   ```
   git clone git@github.com:Grezewave/InVesTRv3.git
   ```
2. Navigate to the backend directory:
   ```
   cd InVesTR
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up Google Sheets API credentials following the instructions in [Google Cloud docs](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br). Download credentials, rename to secrets.json and put into credentials folder.
5. Set up Google Gemini API credentials following the instructions in [Google Gemini docs](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br&_gl=1*iiivu*_up*MQ..&gclid=CjwKCAjw9IayBhBJEiwAVuc3fu5nCfvDVWPXbLvhT15etQN7YMyqkDg3NFBbBms5iBUHGEp21nPf6RoCFPAQAvD_BwE). Export your api key to environment variables.
6. Create a .env file inside credentials/ folder, following the below model:
    ```
    SHEET_ID={GoogleSheets sheet ID}
    RANGE_STRING_INVESTMENTS={page name for investments and range, ex: investment!A1:K999}
    RANGE_STRING_APPLICATIONS={page name for applications and range, ex: applications!A1:K999}
    RANGE_STRING_RETURNS={page name for returns and range, ex: returns!A1:K999}
    ```

## How to run
An easy way to test the application is running service/src/run.ipynb. This notebook explains step by step how to configure and test the application, and how it works.

The notebook service/src/sample.ipynb contains a sample application to test without Google Sheets API, using only your Gemini API Key.


## Service sample
An structure of API and frontend is under development an also can be used and tested:

1. Navigate into service/src folder and start the Flask server:
   ```
   python investr.py
   ```
2. Navigate into chatbot directory and install Node.js dependencies:
   ```
   yarn install
   ```
3. Start the React development server:
   ```
   yarn start
   ```
4. Access the application at `http://localhost:3000` in your web browser.

## Usage
- Upon accessing the application, users are greeted with the chatbot interface.
- Users can interact with the chatbot by typing messages and requesting investment insights.
- The chatbot fetches data from Google Sheets and Google Gemini API to provide real-time investment information.
- Users can view investment performance, analytics, and receive personalized recommendations through the chat interface.

## Contributing
Contributions to this project are welcome. If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository's `main` branch.

## Acknowledgements
- This project utilizes the Google Sheets API and Google Gemini API for fetching investment data and analytics.
- Special thanks to the Flask and React.js communities for providing excellent frameworks and tools for building web applications.
