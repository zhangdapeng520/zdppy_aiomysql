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


async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='test', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 42
    pool.close()
    await pool.wait_closed()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

results = loop.run_until_complete(test_example(loop))
print(results)
