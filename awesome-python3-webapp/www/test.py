'''
import ORM
from Model import User,Blog,Comment

def test():
	yield from ORM.create_pool(user='www_data',password='www_data',databese='awesome')

	u=User(name='Test',email='123@gmail.com',passwd='0000',image='about:blank')

	yield from u.save()

for x in test():
	pass
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import orm, asyncio
from models import User, Blog, Comment


# async def test(loop):
#
#     await orm.create_pool(loop=loop, user='www-data', password='WWW-data12!@', db='awesome', charset='utf8')
#     u = User(name='LIU Shusi', email='i_love_lin@163.com', passwd='18656590', image='about:blank')
#     await u.save()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()

if __name__ == '__main__':
    import asyncio

    async def wget(host):
        print('wget %s...' % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = await connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        await writer.drain()
        while True:
            line = await reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
        writer.close()


    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
