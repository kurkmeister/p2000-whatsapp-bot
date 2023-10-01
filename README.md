## P2000 Bot

This is a Python Flask app that sends P2000 messages via Twilio.

## Features

* Sends P2000 messages for the entire country or for a specific city.
* Can be triggered by sending a simple SMS message.
* Easy to set up and use.

## Installation

1. Install Python 3 and the following Python packages:
* Flask
* twilio
* python-decouple
* googlemaps
* pandas
* geocode

You can also install them using pip:

```
pip install -r requirements.txt
```


2. Clone this repository:

```
git clone https://github.com/google/twilio-p2000-bot.git
```

Create a .env file in the root of the repository and add your the following information:

```
GOOGLE_GEOCODE_SECRET=''
TWILIO_WHATSAPP_NUMBER=''
TWILIO_PERSONAL_NUMBER=''
TWILIO_ACCOUNT_SID=''
TWILIO_AUTH_TOKEN=''
```

4. Start the Flask app:

```
python app.py
```

Usage
To send P2000 messages, simply send an SMS message with the text "P2000" to the Twilio phone number that you associated with this app.

If you want to send P2000 messages for a specific city, include the city name after "P2000". For example, to send P2000 messages for Amsterdam, you would send the following SMS message:

>P2000 Amsterdam
