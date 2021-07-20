print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

nombreDeUsuario = int(input("Ingrese su usuario: "))

if(nombreDeUsuario == 51636):
   contrasena = int(input("Ingrese su contraseña: "))
   if(contrasena == 63615):
     numero1 = nombreDeUsuario % 1000
     numero2 = int(6/(6 % 5+1))
     suma = int(input("Ingrese la suma de " + str(numero1) + " + " + str(numero2) + " = "))   
     if(suma == 639):   
       print("Sesión iniciada")
     else:
       print("Error")
   else:
      print("Error")
else:
  print("Error")



