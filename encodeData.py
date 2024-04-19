from constThings import REVIEW_URL
from encoding_mode import determine_encoding_mode
from padding import add_padding

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
    
    # Calculate the total data capacity of the QR code for version 4 with error correction level 'M'
    data_capacity = 640
    
    # for anyone reading this, we can change the above from hardcoding here
    # to actually creating a file to which data capacity can match the version and error correction level
    # this will make the code more dynamic and flexible, but for now I will just hardcode it
    
    # A short trivia to understand data_capacity
    # show how it's calculated
    # what formula gave 640?
    # ans. 640 = 16 * 40
    # 16 is the number of words in a row
    # 40 is the number of rows in a column
    # 640 is the total number of words in the QR code
    # each word is 1 bit
    # so the total number of bits in the QR code is 640
    # 640 bits is the data capacity of the QR code
    # 640 bits is the maximum number of bits that can be stored in the QR code
    # are these number predecided or did we calculate them?
    # ans. these numbers are predecided
    # how do we know that the data capacity of the QR code is 640 bits?
    # ans. we know this from the QR code standard
    # the data capacity of the QR code is determined by the version and error correction level
    # the version is the size of the QR code
    # the error correction level determines the number of error correction codewords
    # the data capacity of the QR code is determined by the version and error correction level 
    
    encoded_data = add_padding(encoded_data, data_capacity)        
    return mode, encoded_data
    
    

