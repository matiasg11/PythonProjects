#1 Install the needed libraries
#2 Create a function to collect a text and convert it to a QR code
#3 Save the QR code as an image. 
#4 Run the function

import qrcode

def generar_QR(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5,
    )
    qr.add_data(text)  
    qr.make(fit=True)
    img = qr.make_image(fill_collor="blue", back_color="yellow")
    img.save("qrcode_img.png")


generar_QR("https://as01.epimg.net/epik/imagenes/2019/05/15/portada/1557912221_652932_1557912409_noticia_normal.jpg")