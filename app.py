import ollama


# Generate a response from the model
response = ollama.chat(model='gemma3:1b', messages=[
    {'role': 'user', 'content': 'hello, how are you?'},
])

print(response['message']['content'])