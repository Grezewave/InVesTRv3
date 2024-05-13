import tkinter as tk
from tkinter import scrolledtext
from tkinterweb import HtmlFrame
import requests
import markdown2
from os import getenv
from dotenv import load_dotenv
import json
from services.GoogleSheetsService import *
from services.GeminiService import *
from utils.utils import *
import pandas as pd
from utils.constants import *
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv('../../credentials/.env')

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = getenv("SHEET_ID")
SHEET_PAGE_INVESTMENTS = getenv("RANGE_STRING_INVESTMENTS")
SHEET_PAGE_APPLICATIONS = getenv("RANGE_STRING_APPLICATIONS")
SHEET_PAGE_RETURNS = getenv("RANGE_STRING_RETURNS")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")

class ChatBot:
  def __init__(self):
    # Create the main window
    sheetService = GoogleSheetsService(SAMPLE_SPREADSHEET_ID)

    investments = sheetService.get_sheet(SHEET_PAGE_INVESTMENTS).drop('bank', axis=1)
    applications = sheetService.get_sheet(SHEET_PAGE_APPLICATIONS).drop('bank', axis=1)
    returns = sheetService.get_sheet(SHEET_PAGE_RETURNS).drop('bank', axis=1)

    ids = investments['investment_name'].values

    raw_body = {
      'investments': [],
      'applications': [],
      'returns': []
    }
    for id in ids:
      raw_body['investments'].extend(
        restructure_dataframe(
          investments[investments["investment_name"] == id]
        )
      )

      raw_body['applications'].extend(
        restructure_dataframe(
          applications[applications["investment_name"] == id]
        )
      )

      raw_body['returns'].extend(
        restructure_dataframe(
          returns[returns["investment_name"] == id]
        )
      )
    body_string = f'''Take this as base for the following questions: {json.dumps(raw_body)}\nShow me a summary of the data provided'''

    self.chat_bot = GeminiService(GEMINI_API_KEY)
    self.chat_bot.send_message(BASE_PROMPT)
    self.zero_response = self.chat_bot.send_message(body_string)


  def ask_question(self, question: str) -> str:
    # Call your API with the question
    return self.chat_bot.send_message(question)
  def get_history(self) -> dict:
    return self.chat_bot.get_history()
    

chatbot = ChatBot()
app = Flask(__name__)
CORS(app)

# Endpoint to initialize the chatbot (optional)
@app.route('/initialize', methods=['GET'])
def initialize_chatbot():
  return jsonify({'answer': chatbot.zero_response})

# Endpoint to handle questions and provide answers
@app.route('/ask', methods=['POST'])
def ask_question():
  # Get the question from the request body
  question = request.json.get('question')

  if question is None:
    return jsonify({'error': 'Question is missing'}), 400

  answer = chatbot.ask_question(question)

  # Return the answer in the response
  return jsonify({'answer': answer})

if __name__ == '__main__':
  app.run(debug=True)