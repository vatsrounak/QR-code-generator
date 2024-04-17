def determine_encoding_mode(input_data):
    """_summary_

    Args:
        input_data (_anything_): _to determine which  encoding mode to be used_
    """
    if not input_data:
        return None
    
    numeric_chars = set("0123456789")
    alphanumeric_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")   
    kanji_chars = set("漢字")
    
    if all(char in numeric_chars for char in input_data):
        return "numeric"
    elif all(char in alphanumeric_chars for char in input_data):
        return "alphanumeric"
    elif all(char in kanji_chars for char in input_data):
        return "kanji"
    else:
        return "byte"