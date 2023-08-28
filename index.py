import os
import openai
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return 'Hello! Chatgpt Route'

@app.route('/chatgpt')
def get_chatgpt_response():
    prompt = request.args.get('prompt') or 'AI'
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages=messages,

        temperature=0,

    )

    return response.choices[0].message["content"]
