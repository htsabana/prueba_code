# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 19:42:48 2022

@author: groja
"""

import psycopg2 as pg

#connect to db
con = pg.connect(
    host = '152.74.29.160',
    user = 'postgres',
    password = 'somno2019',
    port = '9001',
    database = 'somno')

#cursor
# cur = con.cursor(cursor_factory=pg2.DictCursor)
cur = con.cursor()
#close cursor
cur.close()

#close connection
con.close()
