import openai
import os
from openai import OpenAI
import httpx
promptM = "Hello, World!"

#openai.api_key = 'sk-proj-WX9nM01BekFthXUJ5tx9T3BlbkFJsoT0bZwOErIIpS0810bN'

openai.api_key = 'sk-73FNRJoLYrXeamw317432bC3Ca9c4bE08dB5Aa460a09152f'


client = OpenAI(
    base_url="https://api.xty.app/v1",
    api_key='sk-73FNRJoLYrXeamw317432bC3Ca9c4bE08dB5Aa460a09152f',
)

chat_completion = client.chat.completions.create(
    messages=[{"role": "system", "content": "You are a helpful assistant."}],
    model="gpt-3.5-turbo",
    max_tokens=1,
    temperature=0.5
)




#print(chat_completion.choices[0].message.content)