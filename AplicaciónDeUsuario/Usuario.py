import psycopg2
class User():
    def __init__(self, idUser=None, Username=None, Password=None):
        self.__idUser = idUser
        self.__Username = Username
        self.__Password = Password

    def __str__(self):
        return  f"{self.__idUser} | {self.__Username} | {self.__Password}"

    def GetIdUser(self):
        return self.__idUser

    def GetUsername(self):
        return self.__Username
    def SetUsername(self, User):
        self.__Username = User

    def GetPassword(self):
        return self.__Password
    def SerPassword(self, Password):
        self.__Password = Password

if __name__ == '__main__':
    user1 = User(1, "Daniel", "151201")
    print(user1)

