import string
import random


# Function for password generator
def generate_password(
    length: int, lowercase=True, uppercase=True, digits=True, symbols=True
) -> str:
    """
    Generates a secure password based on specified criteria.
    """
    char_pool = ""
    if lowercase:
        char_pool += string.ascii_lowercase
    if uppercase:
        char_pool += string.ascii_uppercase
    if digits:
        char_pool += string.digits
    if symbols:
        # Include common symbols without relying on external libraries
        char_pool += "!@#$%^&*()"
    if not char_pool:
        raise ValueError("At least one character type must be chosen")

    password = char_pool[0]
    for _ in range(1, length):
        password += char_pool[random.randrange(len(char_pool))]
    return password


# Function for weather endpoint
def is_valid_lat_long(lat: float, lon: float) -> bool:
    """
    Checks if latitude and longitude values are within valid ranges.
    """
    return -90 <= lat <= 90 and -180 <= lon <= 180
