from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)


def send_location_message(coordinates, body_message: str, label: str):
    message = client.messages.create(
    from_=config('TWILIO_WHATSAPP_NUMBER'),
    body=body_message,
    persistent_action=[f'geo:{coordinates[0]},{coordinates[1]}|{label}'],
    to=config('TWILIO_PERSONAL_NUMBER'),
    )
    print(f"Message sent\n{message.sid}")
    return message.sid

def send_body_message(message: str):
    message = client.messages.create(
    from_=config('TWILIO_WHATSAPP_NUMBER'),
    body=message,
    to=config('TWILIO_PERSONAL_NUMBER'),
    )
    print(f"Message sent\n{message.sid}")
    return message.sid