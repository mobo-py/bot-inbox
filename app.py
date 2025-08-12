import ollama

    # Generate a response from the model
response = ollama.chat(model='deepseek-r1:32b', messages=[
    {'role': 'user', 'content': 'Explain the concept of quantum entanglement in simple terms.'},
])

print(response['message']['content'])