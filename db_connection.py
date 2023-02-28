from typing import List

import aiopg


class DBConnectionParameters():
    dbname: str
    user: str
    password: str
    host: str
    port: str

    def __init__(self, dbname: str, user: str, password: str, 
                 host: str, port: str):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port


class PostgresConnection():
    def __init__(self, connection_params: DBConnectionParameters):
        self.__connection_params = connection_params

    async def run_cmd(self, cmd: str) -> List:
        conn = await aiopg.connect(dbname=self.__connection_params.dbname,
                            user=self.__connection_params.user,
                            password=self.__connection_params.password,
                            host=self.__connection_params.host,
                            port=self.__connection_params.port,
                            )
        cursor = await conn.cursor()
        await cursor.execute(cmd)

        try:
            records = await cursor.fetchall()
        except:
            records = []

        cursor.close()
        conn.close()

        return records
