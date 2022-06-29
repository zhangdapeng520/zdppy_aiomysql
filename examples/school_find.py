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


async def find(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='test', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            sql = """select * from school;"""
            result = await cur.execute(sql)
            print(result)
            result = await cur.fetchall()
            print(result)
    pool.close()
    await pool.wait_closed()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

results = loop.run_until_complete(find(loop))
print(results)
