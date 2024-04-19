from generate_qr_code import generate_qr_code
from encodeData import encode_data
from constThings import REVIEW_URL
from padding import add_padding
from encoding_mode import determine_encoding_mode
from dynamic_file_naming import save_file


# Determine the encoding mode for the input data
encoded_data = encode_data(REVIEW_URL)

# Calculate the total data capacity of the QR code for version 4 with error correction level 'M'
data_capacity = 640

# for anyone reading this, we can change the above from hardcoding here
# to actually creating a file to which data capacity can match the version and error correction level
# this will make the code more dynamic and flexible, but for now I will just hardcode it

padded_encoded_data = add_padding(encoded_data, data_capacity)

# Generate a QR code image from the padded encoded data
qr_code_image = generate_qr_code(padded_encoded_data)

# Save the QR code image to a file
save_file("qr_code.png")