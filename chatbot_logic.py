from flask import Flask, request
from twilio.twiml.messaging_response import , MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['POST'])
# chatbot logic
def bot():
    msg = request.form.get('Body').lower()  # Reading the message from the whatsapp

    print("msg-->", msg)
    resp = MessagingResponse()
    reply = resp.message()
    # Create reply
    if msg == "hi":
        reply.body("hello!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)