import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

messages = []

print("跟 Claude 聊天，输入 'quit' 退出\n")

while True:
    user_input = input("你: ")
    if user_input.lower() == 'quit':
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=messages
    )
    
    assistant_reply = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_reply})
    
    print(f"Claude: {assistant_reply}\n")