from random import randint

from fastapi import FastAPI

from models import Record
from services import postgres_error_wrapper

from db_connection import PostgresConnection, DBConnectionParameters

app = FastAPI()


CONNECTION = PostgresConnection(DBConnectionParameters(
    dbname='test',
    user='test_user',
    password='test_password',
    host='127.0.0.1',
    port='5432'
))

WORK_TABLE = 'records'

@postgres_error_wrapper
@app.get('/get/records', status_code=200)
async def tasks_list():
    res = await CONNECTION.run_cmd('SELECT * FROM %s;' % (WORK_TABLE))
    return {'message': res}

@postgres_error_wrapper
@app.post('/create/record', status_code=200)
async def create_task(record: Record):
    await CONNECTION.run_cmd(
        'INSERT INTO %s VALUES (\'%s\', \'%s\', \'%s\');' % 
        (WORK_TABLE, str(randint(0, 1_000_000_000)), record.name, record.value)
    )
    return {'message': 'ok'}

@postgres_error_wrapper
@app.delete('/delete/record/{id}', status_code=200)
async def delete_task(id: str):
    await CONNECTION.run_cmd(
        'DELETE FROM %s WHERE id = \'%s\';' % (WORK_TABLE, id)
    )
    return {'message': 'ok'}

@postgres_error_wrapper
@app.patch('/update/record/{id}', status_code=200)
async def update_task(id: str, record: Record):
    await CONNECTION.run_cmd(
        'UPDATE %s SET name = \'%s\', value = \'%s\' WHERE id = \'%s\';' % 
        (WORK_TABLE, record.name, record.value, id)
    )
    return {'message': 'ok'}
