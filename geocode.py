import googlemaps
from decouple import config

gmaps = googlemaps.Client(key=config('GOOGLE_GEOCODE_SECRET'))

def get_coordinates_from_string(message: str) -> list:
    """
    Geocodes a given address string using Google Maps API and returns the latitude, longitude, and formatted address.

    Args:
        message (str): The address string to geocode.

    Returns:
        list: A list containing the latitude and longitude as floats in the first element, the formatted address as a string in the second element,
        and the location type as a string in the third element.
        
        If the address is not found, the latitude and longitude will be 0, and the formatted address will be "No address found".
    """
    print(f"*****Geocoding {message}, API called...*****")
    try:
        geocode_result = gmaps.geocode(message)
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
        address = geocode_result[0]['formatted_address']
        location_type = geocode_result[0]['geometry']['location_type']
    except:
        latitude = 0
        longitude = 0
        address = "No address found"
        location_type = "No address found"

    return [[latitude, longitude], address, location_type]