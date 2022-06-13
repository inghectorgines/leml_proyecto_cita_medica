import registro.usuario_doc as modelo
import registrar_consulta.acciones_consulta


class AccionesARealizar:
    def registro_doc(self):
        print("procederemos a realizar su registro, en nuestra clinica")
        
        #creamos las variables, para guardar lo que dijite el usuario
        nombre = input("¿Cual es su nombre doctor?:")
        apellidos = input("¿Cuales son tus apellidos?:")
        email = input("¿Cuales son tu correo electronico?:")
        password = input("¿Introduce tu contraseña?:")
        num_consultorio = input("¿Introduce el numero de tu consultorio?:")
        num_cedula = input("¿Introduce el numero de tu cedula?:")
        
        usuario = modelo.Usuario_doc(nombre,apellidos,email,password,num_consultorio,num_cedula)
        registro = usuario.registrar()
        
        if registro[0] >= 1:#verificamos si el registro es mayor a 1
            print(f"\nPerfecto Doctor: {registro[1].nombre} {registro[1].apellidos} te has registrado con tu correo: {registro[1].email} el numero de tu consultorio es: {registro[1].num_consultorio} y tu cedula es:{registro[1].num_cedula}")
        else:
            print(f"\nTu registro no se realizo correctamente, Usuario existente, pruebe con otro")    
                
        
    def login_doc(self):
        print("\n*****CLINICA LUIS, indentificate*****")
        
        try:
            email = input("Introduce tu email doctor:")
            password = input("Introduce tu password:")
            # num_cedula = input("Introduce tu numero de cedula:")
            
            usuario = modelo.Usuario_doc('', '', email, password,'','')
            login = usuario.identificar_doc()
            
            if email == login[3]:
                print(f"\nBienvenido DOCTOR: {login[1]} {login[2]} te has registrado en el consultorio:{login[5]} en la fecha {login[7]}")
                self.registrar_consulta(login)
        except Exception as e:
            print("\n Login incorrecto, intentelo de nuevo")    
               
    def registrar_consulta(self,usuario):
        print("""
              vamos a registrar tu consulta medica:
              1-Crear consulta medica
              2-Mostrar consulta medica
              3-Editar consulta medica
              4-Eliminar consulta medica  
              5-Salir del sistema                           
              """)
        
        accion = input("Que quieres hacer:")
        hazEl = registrar_consulta.acciones_consulta.Acciones_consultar()
        
        if accion == "1":
            hazEl.crear(usuario)
            self.registrar_consulta(usuario)
        elif accion == "2":
            hazEl.mostrar_consulta(usuario)
            self.registrar_consulta(usuario)
        elif accion == "3":
            hazEl.actualizar_consulta(usuario)
            self.registrar_consulta(usuario)
        elif accion == "4":
            hazEl.borrar(usuario)
            self.registrar_consulta(usuario)
        elif accion == "5":
            exit()      
        