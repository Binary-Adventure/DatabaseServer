import asyncio
import asyncpg
import json

from aiohttp import web



pool_config_name = 'pool_config.json'



class DataBaseHandler:
    async def create_table(self, request):
        pool = request.app['pool']
        data = {
            "name": request.match_info.get('name', None),
            "json": await request.json()
        }
        print(data['name'], data['json'])

        async with pool.acquire() as conn:
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS %s (

                )
            ''', (data['name'],))

    async def delete_table(self):
        pass


    async def get_line(self):
        pass

    async def get_value(self):
        pass


    async def add_line(self):
        pass

    async def add_value(self):
        pass


    async def remove_line(self):
        pass

    async def remove_value(self):
        pass



dbh = DataBaseHandler()
async def init_db(app):
    with open(pool_config_name, encoding='utf-8') as file:
        pool_config = json.load(file)

    try:
        app['pool'] = await asyncpg.create_pool(host=pool_config['host'],
                                                port=pool_config['port'],
                                                user=pool_config['user'],
                                                password=pool_config['password'],
                                                database=pool_config['database'])

    except Exception as e:
        print(e)
    
    finally:
        print('database is connected')
        yield
        app['pool'].close()


def init_app():
    app = web.Application()
    app.cleanup_ctx.append(init_db)
    app.add_routes([
        web.post(path='/create_table/{name}', handler=dbh.create_table),
    ])

    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(app, host='0.0.0.0', port=8080)