from langchain_community.tools import DuckDuckGoSearchRun
import ollama


search = DuckDuckGoSearchRun()

print(search.invoke("what is evaporation"))

# response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Current complaints of the citizens for government of india'}])
# print(response['message']['content'])
