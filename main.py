import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_size = int(input("Ingrese la longitud de la contraseña"))

password = ""

for i in range (pass_size):
    password += random.choice(characters)
    
print("Contraseña segura:")
print(password)
