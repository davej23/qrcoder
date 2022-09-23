from QR import QR

# Instantiate object
qr = QR()

# Grab current screen (screenshot)
qr.grab_screen()

# Save screenshot
qr.grab_screen_to_file()
qr.grab_screen_to_file("myscreenshot")

# Read QR code from latest screen grab
print(qr.read_qr_code())  # Copies to clipboard by default
print(qr.read_qr_code(save_to_clipboard=False))

# Read QR code from image
print(qr.read_qr_code_from_image(filename="myimage.jpeg"))  # Copies to clipboard by default
print(qr.read_qr_code_from_image(filename="myimage.jpeg", copy_to_clipboard=False))

# Generate QR code
qr.generate_qr_code(data="hello world", save_to_file=False)  # Prints to stdout
qr.generate_qr_code(data=[1, 2, 3, 4, 5, 6, 7, 8, 9], save_to_file=True)  # Prints to stdout and saves to file
qr.generate_qr_code(data=100, save_to_file=True, filename="myqrcode")  # Prints to stdout and saves to specified filen
