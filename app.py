
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Client setup
client = genai.Client(api_key="Gemini_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"You are a medical assistant. Give simple advice: {user_input}"
        )

        return jsonify({'reply': response.text})

    except Exception as e:
        return jsonify({'reply': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
