from PIL import ImageGrab
import cv2
import os
import numpy as np
import time
import io
import xerox
from qrcode import QRCode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import (HorizontalGradiantColorMask, 
                                            SquareGradiantColorMask, 
                                            RadialGradiantColorMask, 
                                            SolidFillColorMask, 
                                            VerticalGradiantColorMask)


class QR:
    def __init__(self):
        self._im = None

    @staticmethod
    def grab_screen_to_file(filename=f"screenshot-{time.strftime('%Y%m%d-%H%M%S')}"):
        im = ImageGrab.grab()
        im.save(filename + ".png")

    def grab_screen(self):
        self._im = np.asarray(ImageGrab.grab())

    def read_qr_code(self, copy_to_clipboard=True):

        if self._im is None:
            print("Please run .grab_screen() first")
            return

        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(self._im)

        if copy_to_clipboard:
            xerox.copy(value)

        return value

    @staticmethod
    def read_qr_code_from_image(filename, copy_to_clipboard=True):
        
        if os.path.exists(filename):
            img = cv2.imread(filename)
        else:
            raise FileNotFoundError

        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)

        if copy_to_clipboard:
            xerox.copy(value)

        return value

    def generate_qr_code(self, 
                            data, 
                            random_style=False,
                            save_to_file=True, 
                            filename=f"qrcode-{time.strftime('%Y%m%d-%H%M%S')}"):
        qr = QRCode()
        qr.add_data(data)

        # Print to stdout
        f = io.StringIO()
        qr.print_ascii(out=f)
        f.seek(0)
        print(f.read())

        # Save to file
        if not random_style:
            img = qr.make_image(fill_color="black", back_color="white")
        else:
            styles = [HorizontalGradiantColorMask, 
                        SquareGradiantColorMask, 
                        RadialGradiantColorMask, 
                        SolidFillColorMask, 
                        VerticalGradiantColorMask]

            chosen_style = np.random.choice(styles)
            chosen_colours = [
                                tuple(np.random.choice(range(256), 3)),
                                tuple(np.random.choice(range(256), 3)),
                                tuple(np.random.choice(range(256), 3))
                            ]

            img = qr.make_image(image_factory=StyledPilImage, 
                                color_mask=chosen_style(chosen_colours[0], 
                                                        chosen_colours[1], 
                                                        chosen_colours[2]))

        if save_to_file:
            img.save(filename + ".png")
