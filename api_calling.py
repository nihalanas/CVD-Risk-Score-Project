# from langchain_community.llms import Ollama
# ollama = Ollama(base_url='http://localhost:11434',
# model="dolphin-mistral")
# print(ollama("why is the sky blue"))

from fastapi import FastAPI, Body
import requests
app = FastAPI()

@app.post("/generate_text")
async def generate_text(prompt: str = Body(...), model: str = "default_model"):
  # Prepare data for the API request
  data = {
      "prompt": prompt,
      "model": model,
      "stream": "false"
  }
  # Send the request using libraries like requests
  try: # Timeout should be increased to 30 seconds
      response = requests.post("http://127.0.0.1:11434/api/generate", json=data)
      response.raise_for_status()  # Raise an exception for non-2xx status codes
  except requests.exceptions.RequestException as e:
      # Handle errors here, return appropriate error message
      return {"error": f"Error connecting to API: {str(e)}"}
  # Process the response
  response_data = response.json()
  generated_text = response_data["generated_text"]
  # Further process or format the generated text (optional)
  # ...
  return {"generated_text": generated_text}