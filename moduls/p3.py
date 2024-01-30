import sys
sys.path.append('C:\\users\\priyanka\\appdata\\roaming\\python\\python311\\site-packages')
# print(sys.path)
import qrcode
img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")