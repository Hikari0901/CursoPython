import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Bienvenido al genedor de contrasenas PyPassword!')

nr_letras=int(input('¿Cuantas letras quieres en tu contrasena?\n\t'))
nr_simbolos=int(input('¿Cuantos simbolos te gustaria?\n\t'))
nr_numeros=int(input('¿Cuantos numeros quieres?\n\t'))

password_list=[]

for chart in range(1, nr_letras + 1):
    password_list.append(random.choice(letras))
  
    
for chart in range(1,nr_simbolos + 1):
    password_list.append(random.choice(simbolos))

for chart in range(1, nr_numeros + 1):
    password_list.append(random.choice(numeros))
    
random.shuffle(password_list)

password=""
for chart in password_list:
    password+= chart 
    
print(f"Tu contraseña es: {password}")