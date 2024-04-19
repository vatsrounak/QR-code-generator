import qrcode 
from PIL import Image
from constThings import REVIEW_URL
from encoding_mode import determine_encoding_mode

def encode_data(REVIEW_URL):
    """
    Encodes the input data into binary representation based on the determined encoding mode.
    
    Args:
        REVIEW_URL (str): The input data to be encoded.
        
    Returns:
        tuple: A tuple containing the encoding mode and the encoded data string
    
    """
    # Determine the encoding mode for the input data
    mode = determine_encoding_mode(REVIEW_URL)
    encoded_data = ''
    
    if mode == 'Numeric':
        # Encode each digit as binary using 4 bits per digit
        for char in REVIEW_URL:
            encoded_data += format(int(char), '04b')
    elif mode == 'Alphanumeric':
        # Encode each alphanumeric character as binary using 6 bits per character
        for char in REVIEW_URL:
            if char.isnumeric():
                # Encode the numeric character as binary using 10 bits
                encoded_data += format(int(char) + 45, '06b')
            else:
                # Encode the alphabetic character as binary using 11 bits
                encoded_data += format(ord(char) - 55, '06b')
    elif mode == 'Byte':
        # Encode each byte as binary using 8 bits per byte
        for char in REVIEW_URL:
            encoded_data += format(ord(char), '08b')
    elif mode == 'Kanji':
        # Encode each Kanji character as binary using 13 bits per character
        for char in REVIEW_URL:
            # Encode the Kanji character as binary using 13 bits
            encoded_data += format(char, '013b')
            
    return mode, encoded_data
    
    

