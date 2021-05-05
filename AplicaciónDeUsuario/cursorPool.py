from connection import Connection
from logger import logger

class poolCursor:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def __enter__(self):
        self.__connection = Connection.obtainConnection()
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, exception_type, exc_val, exc_tb):
        if exc_val is not None:
            self.__connection.rollback()
            logger.warning('Excepción registrada')
        else:
            self.__connection.commit()
            logger.debug('Cambios guardados')

        self.__cursor.close()
        Connection.freeConnection(self.__connection)

if __name__ == '__main__':
    with poolCursor() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de personas')
        logger.debug(cursor.fetchall())