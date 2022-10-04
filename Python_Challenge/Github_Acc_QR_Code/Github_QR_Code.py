import qrcode

img = qrcode.make("Hi, this is a qr code")
img.save("myqr.png")

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
data = "https://github.com/sethaddie"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("Addie's_Github_QR_Code.png")