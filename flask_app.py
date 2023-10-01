from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from p2000_bot import run_p2000_bot
from decouple import config

# Your Twilio Account SID and Auth Token
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Create a Flask app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming message data from Twilio
    message_body = request.values.get('Body', '')
    sender_number = request.values.get('From', '')

    # Process the incoming message
    # create regex that checks for 'p2000' in message_body

    if message_body == 'P2000' or message_body == 'p':
        run_p2000_bot()
        return 'Standard P2000 messages sent'
    if 'P2000' in message_body:
        # get all characters after 'P2000'
        city = message_body[6:]
        run_p2000_bot(city)
        return f'P2000 messages sent for {city}'
    else:
        response = MessagingResponse()
        response.message('Unknown command. Please send "P2000" to get the latest P2000 messages.')
        return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5005)