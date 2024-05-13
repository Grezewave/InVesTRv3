import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


class GoogleSheetsService:
  def __init__(self, SAMPLE_SPREADSHEET_ID: str):
    
    self.SAMPLE_SPREADSHEET_ID = SAMPLE_SPREADSHEET_ID

    # Authentication processes
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("tokens.json"):
      creds = Credentials.from_authorized_user_file("tokens.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "../../credentials/secrets.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("tokens.json", "w") as token:
        token.write(creds.to_json())

    self.creds = creds

  def get_sheet(self, SHEET_RANGE_STRING: str) -> pd.DataFrame:
    df = pd.DataFrame()
    try:
      service = build("sheets", "v4", credentials=self.creds)

      # Call the Sheets API
      sheet = service.spreadsheets()
      result = (
          sheet.values()
          .get(
            spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
            range=SHEET_RANGE_STRING
          ) 
          .execute()
      )
      values = result.get("values", [])

      if not values:
        print("No data found.")

      headers = values.pop(0)
      df = pd.DataFrame(values, columns=headers)
      
    except HttpError as err:
      print(err)

    return df