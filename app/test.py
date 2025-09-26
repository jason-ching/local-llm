from ollama import chat
from ollama import ChatResponse


response: ChatResponse = chat(model='llama3:8b', messages=[
  {
    'role': 'user',
    'content': 'Whats one important lesson when building an LLM app in python for the first time?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
#print(response.message.content)