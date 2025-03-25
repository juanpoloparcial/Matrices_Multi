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
        
    personas.append([nombre,apellido, dni,"Teléfonos: ", telefonos])

    #Se le consulta al usuario si desea seguir agregando más personas a la lista
    agregar_persona = input("Quiere Agregar otra persona ?  (SI/NO): ").upper()
    if agregar_persona != "SI":
        break
    #Cualquier respuesta que el usuario ingrese que no se "SI", se tomara como un "NO"
    # y se finalizara la carga de otra persona a la lista. En caso de que responda de forma
    # correcta, se habilita a que pueda ingresar una nueva persona a la lista.
    
print('\n'"Lista de Personas: ")
for i in personas:
    print(i)
    #Realizamos un ciclo For para que muestre por pantalla 
    #Cada persona ingresada a la lista. Siendo "i", cada persona en la misma

