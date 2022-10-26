import asyncio

import orm
from models import User, Blog, Comment

u = User(name='Test0', email='test0@example.com', passwd='34567890', image='about:blank')


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')
    await u.save()


async def test_findAll(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')
    rs = await u.findAll()
    print(rs)


async def main(loop):
    await test(loop)
    await test_findAll(loop)

loop = asyncio.new_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()