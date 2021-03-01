import pyqrcode

url = pyqrcode.create("https://github.com/m3m0K")
url.png('qr_kod_.png',scale = 6)