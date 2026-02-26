#Se va a  crear un validador para saber si podemos o no podemos entrar a una fiesta, es importante agregar que para entrar a la fiesta debe ser mayor de edad
#Se crea la variable edad y en ella se va a guardar lo que escriba el usuario
edad = input("Holi OwO ke edad tienezzz: ")
#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)
#Vamos a comprobar si la edad es mayor o igual a 18 años
if edad >= 18:
    #imprime que lo deja entrar
    print("Puedes entrar wuuuu UwU")
else:
    #Si no se cumple la condición de ser mayor de 18 años, imprimer "no puede entrar"
    print("Ñooo, tas muy chikito, vuelve despues UnU")
#Ahora se va a validar si la persona es mayor de edad y ademas tiene más de $600
#Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Holi OwO ke edad tienezzz: ")
#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)
#Se crea la variable dinero y en ella se guarda lo que escriba el usuario
dinero = input("MMM aver kuanto varo traes ewe: ")
#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
dinero = int(dinero)
#Vamos a comprobar si la edad es mayor o igual a 18 años - versión 2
if edad >= 18: 
    #Verificamos si cuenta con el dinero
    if dinero >= 600:
        #imprime que lo deja entrar
        print("Puedes entrar wuuuu UwU")
    else:
        #Como no tiene el dinero no puede entrar
        print("ÑOOO , ni varo traes :C")
else:
    #Como no tiene la edad no puede entrar
    print("Ñooo, tas muy chikito, vuelve despues UnU")
#Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Holi OwO ke edad tienezzz: ")
#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)
#Se crea la variable dinero y en ella se guarda lo que escriba el usuario
dinero = input("MMM aver kuanto varo traes pa la peda we ewe: ")
#Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
dinero = int(dinero)
#Vamos a comprobar si la edad es mayor o igual a 18 años - versión 3
if edad >= 18 and dinero >=600:
    print("Bienvenidooo OwO")
else:
    print("Hijole Hoy nooo unu")
    
#------------------------------------------------
#Condicional con multiple comparaciones
#Creamos la variable llamada dinero
dinero =input("Kuanto varo traezzz: ")
#Convertimos la variable str a entero
dinero =int(dinero)
if dinero < 100:
    print("te compro galletitas owo")
elif dinero >= 100 and dinero <= 200:
    print("Te compre unos pockys uwu")
elif dinero > 200 and dinero <= 300:
    print("Te compre un ramo buchoncito")
else:
    print("Te compre unos copic")
#------------------Laboratorio---------------------
#Creamos la variable userReply y en ella guardamos lo que escriba el usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")
#Si lo que hay dentro de la variable userReply es exactamente igual a "yes"
if userReply == "yes":
    #Imprime que nos puede ayudar
    print("We can help you ship that package!")
#De lo contrario dice que vuelva pronto:
else:
    print("Please come back when you need to ship a package. Thank you.")
#En la variable userReply vamos a guardar una de estas opciones (stamps, envelope, or copy) que deben ser escritas en la consola. Si no se escribe ninguna de ellas se imprime un mensaje de despedida
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
#Si la variable es exactamente igual a "stamps" imprime el mensaje con stamps
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
#Si la variable es exactamente igual a "stamps" imprime el mensaje con envelope
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
#Si la variable es exactamente igual a "stamps" imprime el mensaje con copy
elif userReply == "copy":
    #Se crea la variable copies y se almacena el número de copias que desea crear el usuario
    copies = input("How many copies would you like? (Enter a number) ")
    #Imprime el numero de copias:
    print("Here are {} copies.".format(copies))
else:
    #Se imprime el mensaje de despedida
    print("Thank you, please come again.")