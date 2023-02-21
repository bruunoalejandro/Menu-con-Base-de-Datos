from mysql import connector
from PersonaDAO import PersonaDAO
from PersonaDTO import PersonaDTO

contador = 0
respuesta = None
while respuesta != 5:
    print("\tMenu de Base de Datos")
    print("1) Insertar Persona")
    print("2) Eliminar Persona")
    print("3) Actualizar Persona")
    print("4) Listar Personas")
    print("5) Salir")
    try:
        respuesta = int(input("Que deseas hacer? "))
        print()
    except:
        print()
        print("La opción debe ser numerica")
        respuesta = int(input("Que deseas hacer? "))
        print()

    if respuesta == 1:
        sql = "insert into Personas values (%s, %s, %s, %s, %s)"
        Rut = str(input("Ingrese rut: "))
        Nombre = str(input("Ingrese nombre: "))
        Direccion = str(input("Ingrese direccion: "))
        Correo = str(input("Ingrese correo: "))
        Estado_Civil = str(input("Ingrese estado civil: "))
        
        
        conexion = connector.connect(user='root', database='base_registro')
        cursor = conexion.cursor()
        cursor.execute(sql,[Rut, Nombre, Direccion, Correo, Estado_Civil])
        conexion.commit()
        conexion.close()
        contador = contador + 1
        print()
        print("Datos ingresados correctamente. Que deseas hacer ahora?")
        print()
        
    if respuesta == 2:
        Rut = str(input("Ingrese rut a ser eliminado: "))
        sql = 'delete from Personas where rut = %s'
        conexion = PersonaDTO.Conexion()
        cursor = conexion.cursor()
        cursor.execute(sql,[Rut])
        conexion.commit()
        conexion.close()
        contador = contador - 1
        print("Datos eliminados correctamente. Que deseas hacer ahora?")
        print()
    
    if respuesta == 3:
        if contador == 0:
            print("Primero debes ingresar una persona. ")
            print()

        else:
            Rut = str(input("Ingrese rut de la persona que quieres actualizar los datos: "))
            sql = 'update Personas set Nombre = %s, Direccion = %s, Correo = %s, Estado_Civil = %s where Rut = %s'
            Nombre = str(input("Ingrese nombre a ser actualizado: "))
            Direccion = str(input("Ingrese direccion a ser actualizada: "))
            Correo = str(input("Ingrese correo a ser actualizado: "))
            Estado_Civil = str(input("Ingrese estado civil a ser actualizado: "))
            conexion = PersonaDTO.Conexion()
            cursor = conexion.cursor()
            cursor.execute(sql,[Nombre, Direccion, Correo, Estado_Civil, Rut])
            conexion.commit()
            conexion.close()
            print("Datos actualizados correctamente. Que deseas hacer ahora?")
            print()

    if respuesta == 4:
        if contador == 0:
            print("No hay personas para ser listadas, intente ingresar una.")
            print()
        else:
            sql = 'select * from Personas'
            conexion = PersonaDTO.Conexion()
            cursor = conexion.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            conexion.commit()
            conexion.close()
            filas = list()
            for registro in resultados:
                per = PersonaDAO(registro[0],registro[1], registro[2], registro[3],registro[4])
                filas.append(per)
            print(filas)
            print()
            print("Datos listados correctamente. Que deseas hacer ahora?")
            print()

    if respuesta == 5:
        print("Encerrando tu sesion... Hasta luego :)")
        print()
        break
    
    if respuesta <= 0 or respuesta >= 6:
        print("Numero invalido, ingrese un numero de 1 a 5")
        print()