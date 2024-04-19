def determine_encoding_mode(input_data):
    """_summary_

    Args:
        input_data (_anything_): _to determine which  encoding mode to be used_
    """
    if not input_data:
        return None
    
    numeric_chars = set("0123456789")
    alphanumeric_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$%*+-./:")   
    # kanji_chars = set("漢字") 
    # rather lets use the range here, because there are lots of kanji characters
    kanji_chars_range = set(chr(i) for i in range(0x4E00, 0xA000))
    
    if all(char in numeric_chars for char in input_data):
        return "Numeric"
    elif all(char in alphanumeric_chars for char in input_data):
        return "Alphanumeric"
    elif any(char in kanji_chars_range for char in input_data):
        return "Kanji"
    else:
        return "Byte"