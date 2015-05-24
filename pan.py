#!/usr/bin/python3.4

import urllib.request
import psycopg2
import re

for i in range(1,90000):
    stock_id = format("%06d" %i)
    print(stock_id)
    fp = urllib.request.urlopen("http://data.eastmoney.com/report/" +stock_id+".html")

    web_bytes = fp.read()
    web_str = web_bytes.decode("gbk")
    fp.close()

    match_number = 0
    pattern = re.compile(r"强烈推荐")
    match = pattern.findall(web_str)
    if match:
        for result in match:
            for item in result:
                match_number = match_number+1
    else:
        continue

    # 数据库连接参数
    conn = psycopg2.connect(database="stock", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO stock(stock_id, raw_data,tuijian)VALUES(%s ,%s, %s)", (stock_id, web_str,match_number))

    conn.commit()
    cur.close()
    conn.close()
