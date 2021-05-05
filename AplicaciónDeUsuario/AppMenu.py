from DAOUser import DAOuser
from Usuario import User

def ListarUsuario():
    users = DAOuser.select()
    for user in users:
        print(f'Usuario: {user}\n')
def AnyadirUsuario(Username, Password):
    user = User(Username=Username, Password=Password)
    DAOuser.insert(user)
    print("Usuario añadido de forma correcta")
def ActualizarUsuario(Username, Password, ID):
    user = User(ID,Username,Password)
    DAOuser.update(user)
def EliminarUsuario(ID):
    user = User(ID)
    DAOuser.delete(user)

print("Bienvenido al programa")


bucle = True

while bucle != False:
    print(f'Presiona 1 para listar los usuarios\n'
          f'Presiona 2 para añadir un usuario\n'
          f'Presiona 3 para actualizar un usuario\n'
          f'Presiona 4 para eliminar un Usuario\n'
          f'Presiona 5 para salir')

    selection = input("1-5 : \n")
    if selection == "1":
        ListarUsuario()
    if selection == "2":
        username = input("Inserta el usuario: ")
        password = input("Inserta la contraseña: ")
        AnyadirUsuario(username, password)
    if selection == "3":
        id_user = input("Inserta la llave de usuario: ")
        username = input("Inserta el usuario: ")
        password = input("Inserta la contraseña: ")
        ActualizarUsuario(username, password, id_user)
    if selection == "4":
        id_user = input("Inserta la llave del usuario a eliminar: ")
        EliminarUsuario(id_user)
    if selection == "5":
        bucle = False
        print("Saliendo del programa")


