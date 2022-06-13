import registro.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consulta:
    def __init__(self,id,usuario_id,num_consulta="",user="",apellidos="",edad="",telefono=""):
        self.id = id
        self.usuario_id = usuario_id
        self.num_consulta = num_consulta
        self.user = user
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        
    def crear_consulta(self):
        sql = "INSERT INTO registrar_consult VALUES(null,%s,%s,%s,%s,%s,%s,NOW())"
        consulta = (self.usuario_id,self.num_consulta,self.user,self.apellidos,self.edad,self.telefono)
        
        cursor.execute(sql,consulta)
        database.commit()
        
        return [cursor.rowcount,self]
    
    def mostrar_consulta(self):
        sql = f"SELECT * FROM registrar_consult"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        
        return resultado
    
    def autualizar_consulta(self):
        sql = "UPDATE registrar_consult SET num_consulta=%s, user=%s, apellidos=%s,edad=%s,telefono=%s WHERE id=%s"
        consulta = (self.num_consulta,self.user,self.apellidos,self.edad,self.telefono,self.id)

        cursor.execute(sql,consulta)
        database.commit()
        
        return [cursor.rowcount,self]
    
    def eliminar_consulta(self):
        sql = f"DELETE FROM registrar_consult WHERE usuario_id = {self.usuario_id} AND num_consulta  LIKE '%{self.num_consulta}%'"

        cursor.execute(sql)
        database.commit() 

        return [cursor.rowcount,self]
