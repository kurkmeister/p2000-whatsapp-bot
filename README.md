## P2000 Bot

This is a Python Flask app that sends P2000 messages via Twilio.

Note: You need a Twilio account and Google Cloud Geocoding API.

Twilio has a free sandbox for testing, which you can read about here:
https://www.twilio.com/docs/whatsapp/sandbox

Google Cloud Geocoding has free requests up to $200 a month. This is sufficient for 40,000 requests per month.
https://developers.google.com/maps/documentation/geocoding/overview
https://developers.google.com/maps/documentation/geocoding/usage-and-billing

## Features

* Sends 3 most recept P2000 messages for given city (default is Amsterdam)
* Can be triggered by a simple WhatsApp Message
* Easy to set up and use.

## Example usage

Message sent:
>P2000 Sijkenisse

Messages recieved

>**Tijd**: 13:31:07

>**Bericht**: A2 (DIA: ja) AMBU 17161 Gerard Fonkertsingel 3201MA Spijkenisse SPIJKN bon 137097

>**Eenheden opgeroepen**:

>🚒 Brandweer - Groepscode Group-1

>🚑 Ambulance - Monitorcode 🚑 Ambulancepos

>🚑 Ambulance - 🚑 Ambulance 17-161

A WhatsApp location message with the geocoded location will also be sent.



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
To send P2000 messages, simply send a WhatsApp message with the text "P2000" to the Twilio phone number that you associated with this app.
Note: You need to activate the sandbox, and associate your own phone number with the sandbox first. See the Twilio documentation:
https://www.twilio.com/docs/whatsapp/sandbox

If you want to send P2000 messages for a specific city, include the city name after "P2000". For example, to send P2000 messages for Amsterdam, you would send the following SMS message:

>P2000 Amsterdam

or

>P2000 Haarlem



