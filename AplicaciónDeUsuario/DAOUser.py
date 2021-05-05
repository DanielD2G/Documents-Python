from logger import logger
from Usuario import User
from cursorPool import poolCursor


class DAOuser:
    '''User DAO'''
    __SELECT = 'SELECT * FROM users'
    __INSERT = 'INSERT INTO users(username,password) VALUES(%s,%s)'
    __UPDATE = 'UPDATE users SET username=%s, password=%s WHERE id_user=%s'
    __DELETE = 'DELETE FROM users WHERE id_user=%s'

    @classmethod
    def select(cls):
        with poolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            registers = cursor.fetchall()
            usersData = []
            for register in registers:
                user = User(register[0], register[1], register[2])
                usersData.append(user)
            return usersData

    @classmethod
    def insert(cls, user):
        with poolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.info(f'User a insertar {user}')
            values = (user.GetUsername(), user.GetPassword())
            cursor.execute(cls.__INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with poolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.info(f'Username to update {user}')
            values = (user.GetUsername(), user.GetPassword(), user.GetIdUser())
            cursor.execute(cls.__UPDATE, values)
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with poolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.info(f'User a eliminar {user}')
            values = (user.GetIdUser(),)
            cursor.execute(cls.__DELETE, values)
            return cursor.rowcount


#if __name__ == '__main__':
    #user1 = User(Username="Abigail", Password="121241")
    #insertaruser = DAOuser.insert(user1)
    #logger.info(f'Users insertados: {insertaruser}')

    #users = DAOuser.select()
    #for user in users:
    #    logger.debug(user)

    #user = User(idUser=1)
    #deleteduser= DAOuser.delete(user)
    #logger.debug(f'Usuarios eliminados: {deleteduser}')
