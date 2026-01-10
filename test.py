import qrcode
texto = ("Ingrese el texto para generar el codigo QR: ")
img = qrcode.make(texto)
img.save("test2.png")