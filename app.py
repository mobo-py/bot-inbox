import ollama

username = input("Enter your name: ")

emailtypes = ["Complaint", "Request", "Update", "Reminder", "Question", "Follow-up"]
emailtype = ""
for i in emailtypes:
    print(f"{emailtypes.index(i)+1}. {i}")
userchoice = int(input("Choose a theme by entering the corresponding number: ")) - 1
emailtype = emailtypes[userchoice]

emailthemes = ["Professional", "Casual", "Friendly", "Formal", "Concise"]
for i in emailthemes:
    print(f"{emailthemes.index(i)+1}. {i}")
themechoice = int(input("Choose a theme by entering the corresponding number: ")) - 1
usertheme = emailthemes[themechoice]

userprompt = input("Enter the content or prompt for the email: ")
title = input("Enter the subject line for the email: ")
recipientname = input("Enter the recipient's name: ")
recpientemail = input("Enter the recipient's email: ")
prompt = f"""
by giving an answer in the form of an email, please follow these instructions:
. The sender's name is '{username}'.
. The email type is '{emailtype}'.
. Use the theme '{usertheme}'.
. The email should be addressed to '{recipientname}'.
. The subject line should be '{title}'.
. The content should address the following prompt: '{userprompt}'.
. Your answer should be in the form of a complete email, including a greeting, body, and closing.
. Your answer should be the email content only, without any additional text or explanations.
. Your answer shouldn't include any areas for the user to fill in, it should be a complete email.
"""

# Generate a response from the model
response = ollama.chat(model='gemma3:1b', messages=[
    {'role': 'user', 'content': prompt},
])

print(response['message']['content'])