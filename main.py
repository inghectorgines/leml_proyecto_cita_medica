## Descargo y procedo a revisar y calificar.

from registro import acciones_a_realizar


print("""
      ********Bienvenido a mi clinica*********
      Acciones disponibles:
      1.-Registrate en nuestro sistema
      2.-Login,Ingresa a nuestro sistema
      3.-Salir del sistema
      """)

hazEl = acciones_a_realizar.AccionesARealizar()
accion = input("\n*****¿Que quieres hacer:?****")


 
if accion == "1":
    hazEl.registro_doc()
elif accion == "2":
    hazEl.login_doc()
elif accion == "3":
    exit()
        
    
