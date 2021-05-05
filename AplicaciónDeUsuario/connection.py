from logger import logger
from psycopg2 import pool
import sys


class Connection:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 10
    __pool = None

    @classmethod
    def poolObtain(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al conectar a la Database {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def obtainConnection(cls):
        connection = cls.poolObtain().getconn()
        logger.debug(f'Conexión obtenida {connection}')
        return connection
    @classmethod
    def freeConnection(cls, connection):
        cls.poolObtain().putconn(connection)
        logger.debug(f'Retornando conexión al pool')
        logger.debug(f'Estado {cls.__pool}')
    @classmethod
    def closeConnection(cls):
        cls.poolObtain().closeall()
        logger.debug(f'Cerrando conexiones')

if __name__ == '__main__':
    conexion1 = Connection.obtainConnection()
    Connection.closeConnection()
