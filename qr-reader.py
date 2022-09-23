"""This file was converted to a binary using pyinstaller"""

from QR import QR

qr = QR()
qr.grab_screen()
print(qr.read_qr_code())
