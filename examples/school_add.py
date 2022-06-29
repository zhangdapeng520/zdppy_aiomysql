#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 20:02
# @Author  : 张大鹏
# @Github  : https://github.com/zhangdapeng520
# @File    : hello.py
# @Software: PyCharm
# @Description: 文档描述
import asyncio

import zdppy_aiomysql as aiomysql


async def add(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='test', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            sql = """
            insert into school(name)
            values ('不知名大学1'),
                   ('不知名大学2'),
                   ('不知名大学3');
            """
            result = await cur.execute(sql)
            print(result)
    pool.close()
    await pool.wait_closed()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

results = loop.run_until_complete(add(loop))
print(results)
