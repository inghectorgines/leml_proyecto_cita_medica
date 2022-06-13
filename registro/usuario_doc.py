import datetime
import hashlib
import registro.conexion as conexion

#llamar la clase conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario_doc:
    
    def __init__(self,nombre,apellidos,email,password,num_consultorio,num_cedula):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.num_consultorio = num_consultorio
        self.num_cedula = num_cedula
        
    def registrar(self):
        fecha = datetime.datetime.now()
        cifrado_password = hashlib.sha256()#cifrado de contraseña
        cifrado_password.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO registro_doc VALUES(null, %s, %s, %s, %s, %s, %s , %s)"
        usuario = (self.nombre, self.apellidos,self.email, cifrado_password.hexdigest(), self.num_consultorio, self.num_cedula, fecha)
        
        try:
            cursor.execute(sql,usuario)
            database.commit()
            return [cursor.rowcount,self]
        
        except:
            resultado = [0, self]
        return resultado
    
    def identificar_doc(self):
        sql = "SELECT * FROM registro_doc WHERE email = %s AND password = %s" 
        cifrado_password = hashlib.sha256() 
        cifrado_password.update(self.password.encode('utf8'))
        
        usuario = (self.email,cifrado_password.hexdigest())
        
        cursor.execute(sql,usuario)
        resultado = cursor.fetchone()
        
        return resultado   