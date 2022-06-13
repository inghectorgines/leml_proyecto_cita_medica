from re import I
import registrar_consulta.consulta as modelo

class Acciones_consultar:
    def crear(self,usuario):
        print(f"{usuario[1]} se procedera a realizar el registro de tu consulta")
        self.id = id
        num_consulta = input("Ingrese su numero de consulta:")
        user = input("Ingrese su nombre por favor:")
        apellidos = input("Ingrese sus apellidos:")
        edad = input("Ingrese su edad:")
        telefono = input("Ingrese su numero de telefono:")
        consulta = modelo.Consulta(id,usuario[0],num_consulta,user,apellidos,edad,telefono)
        guardar = consulta.crear_consulta()
        
        if guardar[0] >= 1:
            print(f"\n*****Perfecto!***** Se ha guardado tu consulta {consulta.user} con el doctor {usuario[1]}")
        else:
            print(f"\nNo se guardado tu consulta {usuario[1]}")    
        
        
    def mostrar_consulta(self,usuario):
        
        print(f"\nDoctor: {usuario[1]} estas son tus consultas")
        self.id = id
        consulta = modelo.Consulta(id,usuario[0])        
        consultas = consulta.mostrar_consulta()
        
        
        for consulta in consultas: 
              print("\n *****************************************************")
              print(f"ID:{consulta[0]}")
              print(f"Numero de consulta:{consulta[2]}")
              print(f"Nombre:{consulta[3]}")
              print(f"Apellidos:{consulta[4]}")
              print(f"Edad:{consulta[5]}")
              print(f"Telefono:{consulta[6]}")
              print(f"Fecha:{consulta[7]}")
              print("************************\n")
    def actualizar_consulta(self,usuario):
        print(f"{usuario[1]} Actualice sus datos:")
       
       
        id = input("Por favor ingrese su ID para poder actualizar su consulta:")
        num_consulta = input("Cambie el numero de su cosulta:")
        user = input("Ingrese el nombre a actualizar:")
        apellidos = input("Ingrese sus apellidos a actualizar:")
        edad = input("Ingrese su edad a actualizar:")
        telefono = input("Ingrese su numero de telefono a actualizar:")
        
        
        actualizar = modelo.Consulta(id,usuario[0],num_consulta,user,apellidos,edad,telefono)
        guardar = actualizar.autualizar_consulta()
            
        if  id != actualizar.id:
            print(f"\nNo se guardado tu consulta {usuario[1]} por que el ID no existe")
        elif guardar[0] != actualizar and id == actualizar.id:
            print(f"\n Se ha actualizado consulta")
            
            
    def borrar(self,usuario):
        print(f"\n{usuario[1]} !!! Borrar tus consultas")
        self.id = id
        num_consulta = input("Introduce el numero de tu consulta:")

        consulta = modelo.Consulta(id,usuario[0],num_consulta)
        eliminar = consulta.eliminar_consulta()

        if eliminar[0] >= 1:
            print(f"Se borro tu consulta: {consulta.num_consulta}")

        else:
            print("No se borro tu consulta, prueba mas tarde.........")    