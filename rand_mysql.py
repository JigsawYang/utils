#!/usr/bin/env python3
#coding:utf-8
import pymysql
import random, time
import zlib

def randstr_to_mysql(times = 10):
    ranstr = (''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 20)));
    rancrc = zlib.crc32(ranstr.encode())

    conn = pymysql.connect('localhost', 'xxx', 'xxx', 'h_perfor')
    cur = conn.cursor()
    num = 0
    while num < times:
        ran = random.randint(1, 100)
        ranstr = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 20))
        rancrc = zlib.crc32(ranstr.encode())
        cur.execute("insert into test(num, randstr, crcstr) values (%s, %s, %s)", (str(ran), ranstr, rancrc))
        num = num + 1
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    randstr_to_mysql();

