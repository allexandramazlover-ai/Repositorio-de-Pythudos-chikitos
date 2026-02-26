#Se usa la libreria re para trabajar con expresiones regulares
import re
#Abrimos el archivo de texto
with open("preproinsulin-seq.txt", "r") as f:
    #Leemos todo el contenido del archivo
    raw_data = f.read()
#Eliminar el origin//
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags= re.IGNORECASE)
#Eliminar el terminador de registro
clean_data = clean_data.replace("//", "")
#Eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)
#Convertimos todo a minúsculas
clean_data = clean_data.lower()
#Abrir nuevamente el archivo prepoinsulin
with open("preproinsulin-seq.txt", "w") as f:
    #Limpiamos el archivo
    f.write(clean_data)
#Calculamos la longitud de prepoinsulina
print("Longitud prepoinsulina uwu = ", len(clean_data))
#Si la secuencia no tiene 110 caractéres nos salimos del programa
if len(clean_data) != 110:
    print("Error unu, la secuencia no tiene 110 caractéres")
    exit()
#Extraemos los primeros 24 caractéres 
lsinsulin = clean_data[0:24]
#Extraemos del caractér 24 al 54
binsulin = clean_data[24:54]
#Extraemos del caractér 55 al 89
cinsulin = clean_data[54:89]
#Extraemos del caractér 89 al 110
ainsulin = clean_data[89:110]
#Creamos los diferentes archivos
with open("lsinsulin-seq-clean.txt,", "w")as f:
    f.write(lsinsulin)
with open("binsulin-seq-clean.txt,", "w")as f:
    f.write(binsulin)
with open("cinsulin-seq-clean.txt,", "w")as f:
    f.write(cinsulin)
with open("ainsulin-seq-clean.txt,", "w")as f:
    f.write(ainsulin)
#Verificamos el tamaño de caractéres
print("lsinsulin OwO = ", len(lsinsulin))
print("binsulin OwO = ", len(binsulin))
print("cinsulin OwO = ", len(cinsulin))
print("ainsulin OwO = ", len(ainsulin))
insulin= binsulin + ainsulin
#Total de insulina
print("Insulina procesada uwu = ", len(insulin))
#Secuencia de la insulina
print("Secuencia de la insulina ewe = ", insulin)