#Get email
#Slice at the @ and the "."

#example "matias@google.com" => matias, google, com

emailInput = input("Ingrese el correo electrónico ")
(user, domain) = emailInput.split("@")
(domain, ext) = domain.split(".")
print("User: ", user,"\n", "Domain: ", domain, "\n", "Extension: ", ext)

#Is useful for the kata where you have to get the domain of the website.