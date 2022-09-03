from email.message import EmailMessage   
from otrasCosas import contraseña
# Import ssl and smt libraries
import ssl
import smtplib


emailEmisor = "matiasguarnera@gmail.com"
emailContra =  contraseña
emailReceptor = "solnahirfernandez@gmail.com"

asunto = "Hola2"
cuerpo =    """ 
            chito
            """

em = EmailMessage()
em["From"] = emailEmisor
em["To"] = emailReceptor
em["subject"] = asunto
em.set_content(cuerpo)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(emailEmisor, emailContra)  #Entro con el mail y la contraseña
    smtp.sendmail(emailEmisor, emailReceptor, em.as_string())   #Envío el mail "em" como una string.
