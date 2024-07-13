from flask import Flask, jsonify, request, send_file
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello1():
    return jsonify({'message': 'Hello, this is your REST API!'})

@app.route('/api/hello/<question>', methods=['GET'])
def hello(question):
  ans = apirespoinse(question)
  return jsonify({'message': ans})

def apirespoinse(prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant"},
      {"role": "user", "content": prompt}
    ]
  )
  return (completion.choices[0].message.content)

# print(apirespoinse("president of taiwan"))

# print(completion.choices[0].message.content)

app.run(host='0.0.0.0', port=5000)
