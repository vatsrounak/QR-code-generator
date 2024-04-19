import os 

def save_file(qr_code_image):
    base_filename = "qr_code"
    counter = 1
    filename = f"{base_filename}.png"
    
    # Check if the file with teh same name already exists
    while os.path.exists(filename):
        # If the file already exists, increment the counter and check again
        filename = f"{base_filename}_{counter}.png"
        counter += 1
        
    # Save the QR code image with the unique filename
    qr_code_image.save(filename)
    print(f"QR code image saved as: {filename}")