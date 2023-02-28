import asyncio

from app import CONNECTION, WORK_TABLE


async def main(table_name=WORK_TABLE):
    await CONNECTION.run_cmd('DROP TRIGGER set_date on %s;' % (table_name))
    await CONNECTION.run_cmd('DROP TABLE %s;' % (table_name))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
