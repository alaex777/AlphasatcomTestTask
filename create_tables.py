import asyncio

from app import CONNECTION, WORK_TABLE


async def main(table_name=WORK_TABLE):
    await CONNECTION.run_cmd(
        'CREATE TABLE %s (id serial, name varchar(128), value jsonb, date_update timestamp with time zone);' % 
        (table_name)
    )
    await CONNECTION.run_cmd(
        '''
        CREATE OR REPLACE FUNCTION update_updated_on_user_task()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.date_update = LOCALTIMESTAMP;
            RETURN NEW;
        END;
        $$ language 'plpgsql';'''
    )
    await CONNECTION.run_cmd(
        'CREATE TRIGGER set_date BEFORE UPDATE ON %s FOR EACH ROW EXECUTE PROCEDURE update_updated_on_user_task();' %
        (table_name)
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
