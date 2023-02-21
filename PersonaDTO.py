from PersonaDAO import PersonaDAO
from mysql import connector

class PersonaDTO:

    @staticmethod
    def Conexion():
        conexion = connector.connect(user='root', database='base_registro')
        return conexion

    def insertarPersona(self, Personas:PersonaDAO):
        try:
            sql = "insert into Personas values(%s, %s, %s, %s, %s)"
            conexion = PersonaDTO.Conexion()
            cursor = conexion.cursor()
            cursor.execute(sql,[Personas.Rut, Personas.Nombre, Personas.Direccion, Personas.Correo, Personas.Estado_Civil])
            conexion.commit()
            conexion.close()
        except:
            return 'Algo salio mal.'

    def eliminarPersona(self, Personas: PersonaDAO):
        try:
            sql = 'delete from Personas where rut = %s)'
            conexion = PersonaDTO.Conexion()
            cursor = conexion.cursor()
            cursor.execute(sql,[Personas.Rut])
            conexion.commit()
            conexion.close()
        except:
            return 'Algo salio mal.'

    def actualizarPersona(self, Personas:PersonaDAO):
        try:
            sql = 'update Personas set nombre = %s, direccion = %s, correo_electronico = %s, estado_civil = %s where rut = %s'
            conexion = PersonaDTO.Conexion()
            cursor = conexion.cursor()
            cursor.execute(sql,[Personas.Nombre, Personas.Direccion, Personas.Correo, Personas.Estado_Civil, Personas.Rut])
            conexion.commit()
            conexion.close()
        except:
            return 'Algo salio mal.'

    def listarPersonas(self):
        try:
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
            return filas
        except:
            return 'Algo no esta bien'