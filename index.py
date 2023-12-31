import os
from flask import Flask, request
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return 'Hello! Chatgpt Route'

@app.route('/chatgpt')
def get_chatgpt_response():
    while True:
        prompt = request.args.get('prompt') or 'AI'
        messages = [{"role": "user", "content": prompt}]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        return chat.choices[0].message.content    
