import asyncio
import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>AWESOme</h1>', content_type='text/html')


async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(init())
loop.run_forever()
