# Rename `os.environ` to `env` else to call as os.environ['key_name_provided_in_.env_file'] and now env['key_name_provided_in_.env_file']
from os import environ as env

# load env variables defined in .env
from dotenv import load_dotenv
load_dotenv()
import ollama

_ollama_client = None
modelName=env["model_name"]

def _defineOllamaClient():
  client = ollama.Client(env["ollama_server"])
  return client

def _getOllamaClient() -> ollama.Client:
  global _ollama_client
  
  if _ollama_client is None or not _ollama_client.is_session_active():
    _ollama_client = _defineOllamaClient()
  
  return _ollama_client

def chatResponse(role, content):
  response = ""
  try:
    response = _getOllamaClient().chat(model=modelName,
                                messages=[{
                                      'role': role,
                                      'content': content
                                }])
  except Exception as e:
    print(f"Exception occurred while getting response: {e}")
  
  return response