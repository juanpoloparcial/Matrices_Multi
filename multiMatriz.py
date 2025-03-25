# Realizar un sistema en JavaScript y Python para consola cmd (terminal) 
# que solicite al usuario cargar el nombre, apellido, dni.
# También se cargaran teléfonos asociados a la persona cargada, que puede 
# ser mas de 1 numero telefónico por persona y que al finalizar muestren los datos en pantalla.

#A modo de ejemplo la matriz tendrá la siguiente forma.     

# ['Juan', 'Perez', '26123456', ['3704112233', '3704321456', '3704122321']]
# ['Andres', 'Acosta', '29123654', ['3704223344', '3704212223']]

print("- CARGA DE DATOS PERSONALES -" '\n')

nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
dni = input("Ingrese su DNI: ") #En caso de querer hacer más detallado, especificaria que sea de tipo INT

print("usted es: ", nombre, apellido, "y su dni es: ", dni)