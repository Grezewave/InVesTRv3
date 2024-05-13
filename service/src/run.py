#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import getenv
from dotenv import load_dotenv
import json
from services.GoogleSheetsService import *
from services.GeminiService import *
from utils.utils import *
import pandas as pd
from utils.constants import *


# In[2]:


load_dotenv('../credentials/.env')

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = getenv("SHEET_ID")
SHEET_PAGE_INVESTMENTS = getenv("RANGE_STRING_INVESTMENTS")
SHEET_PAGE_APPLICATIONS = getenv("RANGE_STRING_APPLICATIONS")
SHEET_PAGE_RETURNS = getenv("RANGE_STRING_RETURNS")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")


# In[3]:


sheetService = GoogleSheetsService(SAMPLE_SPREADSHEET_ID)

investments = sheetService.get_sheet(SHEET_PAGE_INVESTMENTS).drop('bank', axis=1)
applications = sheetService.get_sheet(SHEET_PAGE_APPLICATIONS).drop('id', axis=1)
returns = sheetService.get_sheet(SHEET_PAGE_RETURNS).drop('bank', axis=1).drop('id', axis=1)


# In[4]:


ids = investments['investment_name'].values


# In[5]:


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

print(raw_body)
body_string = f'''Take this as base for the following questions: {json.dumps(raw_body)}'''


# In[6]:


chat_bot = GeminiService(GEMINI_API_KEY)
chat_bot.send_message(BASE_PROMPT)
chat_bot.send_message(body_string)


# In[9]:


prompt = "Show me a summary of the data provided"
while prompt.lower() != "thanks":
  response = chat_bot.send_message(prompt)
  print(prompt)
  print(f'**VTR**: {response}')
  prompt = input("Ask to VTR: ")


# In[ ]:




