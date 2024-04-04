import openai
openai.api_key = 'paste-here'

def chatgpt(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

while True:
    user = input("Enter Command >> ")
    if user.lower() in ["quit", "exit", "bye"]:
        break
    print(chatgpt(user))
