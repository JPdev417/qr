import qrcode
import argparse
import os

# Set up argument parsing
parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
parser.add_argument('-d', '--data', type=str, help="Data (URL) to encode in the QR code.", required=True)
parser.add_argument('-p', '--path', type=str, help="Path to save the QR code image. Defaults to Desktop.", default=os.path.expanduser("~/Desktop"))

# Parse the arguments
args = parser.parse_args()

# Get the URL from the command-line argument
data = args.data

# Get the file save path, default is Desktop
save_path = args.path

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # version 1 is a 21x21 grid
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Set the file name and full path to save
file_name = "qr_code.png"
full_path = os.path.join(save_path, file_name)

# Save the QR code as an image
img.save(full_path)

# Print the path where the QR code is saved
print(f"QR code saved at: {full_path}")

# Show the QR code
img.show()

