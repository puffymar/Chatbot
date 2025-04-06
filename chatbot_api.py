from flask import Flask, render_template, request, jsonify
import requests
import sys

# Initialize Flask app
app = Flask(__name__)

# Simple rule-based chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for the chatbot API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")  # Get user input from the request
    response = chatbot_response(user_input)  # Generate a response using your chatbot logic
    return jsonify({"response": response})  # Return the response as JSON

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)