import google.generativeai as genai

class GeminiService:
  def __init__(self, api_key: str):

    generation_config = {
      "candidate_count": 1,
      "temperature": 0, # creativity rate of model
    }

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-1.0-pro', generation_config=generation_config)

    self.chat = model.start_chat(history=[])

  def send_message(self, message: str) -> str:
    response = self.chat.send_message(message)
    return response.text
  
  def get_history(self) -> dict:
    return self.chat.history
