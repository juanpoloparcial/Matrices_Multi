# Realizar un sistema en JavaScript y Python para consola cmd (terminal) 
# que solicite al usuario cargar el nombre, apellido, dni.
# También se cargaran teléfonos asociados a la persona cargada, que puede 
# ser mas de 1 numero telefónico por persona y que al finalizar muestren los datos en pantalla.

#A modo de ejemplo la matriz tendrá la siguiente forma.     

# ['Juan', 'Perez', '26123456', ['3704112233', '3704321456', '3704122321']]
# ['Andres', 'Acosta', '29123654', ['3704223344', '3704212223']]

print('\n'"- CARGA DE DATOS PERSONALES -" '\n')

# Utilizaremos una lista para almacenar 
# los datos de las personas y los telefonos de igual 
# manera.
personas = []

while True:
    
    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    dni = input("Ingrese su DNI: ") #En caso de querer hacer más detallado, especificaria que sea de tipo INT
    # o también se podria agregar alguna condición para que el mismo sea un valor cercano a la realidad.
    telefonos = []
    while True:
        tel = input ("Ingrese su num de Teléfono (para continuar presione ENTER): ")
        #En caso de que el usuario no Ingrese ningun tel, no se mostrará ningun num
        # para eso nos sirve esta condición, la cual frena la carga de datos 
        # para los num de telefono
        if tel == "":
            break
        telefonos.append(tel) #En caso de que si haya numero, se agrega a los datos
        #de la persona. 
        
    personas.append([nombre,apellido, dni,telefonos])
    
print("usted es: ", nombre, apellido, "y su dni es: ", dni)
