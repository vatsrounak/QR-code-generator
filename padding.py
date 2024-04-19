def add_padding(encoded_data, data_capacity):
    """
    Adds padding bits to the encoded data to fill the remaining capacity of the QR code.
    
    Args:
        encoded_data (str): The encoded data string.
        data_capacity (int): The maximum capacity of the QR code.
        
    Returns:
        str: The encoded data string with padding bits.
    
    """
    # Calculate the number of bits required to fill the remaining capacity of the QR code
    padding_bits = data_capacity - len(encoded_data)
    
    # Add padding bits to the encoded data
    if padding_bits > 0:
        # Add '0' bits to the end of the encoded data
        encoded_data += '0' * padding_bits

    return encoded_data