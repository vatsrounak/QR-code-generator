import qrcode
import qrcode.image.pil

def generate_qr_code(input_data):
    """
    Generates a QR code image from the encoded data.
    
    Args:
        encoded_data (str): The encoded data string.
        
    Returns:
        PIL.Image: The QR code image.
    
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    
    # Add the encoded data to the QR code
    qr.add_data(input_data)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    qr_code_image = qr.make_image(fill_color="black", back_color="white")
    
    return qr_code_image
