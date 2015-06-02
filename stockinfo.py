#!/usr/bin/python3.4

import urllib.request
import psycopg2
import re



class stock_info:
    num = -1
    zone = -1
    name = ''
    now_price = -1
    yesterday_price = -1
    today_price = -1 
    volume = -1
    outer_disc = -1
    inner_disc = -1
    buy_one = -1
    buy_one_volume = -1
    buy_two = -1
    buy_three = -1
    buy_four = -1
    buy_five = -1
    sell_one = -1
    sell_one_volume = '-1'
    sell_two = -1
    sell_three = -1
    sell_four = -1
    sell_five = -1
    transaction = ''
    transaction_time = ''
    change = -1
    change_percentage = -1
    top_price = -1
    low_price = -1
    price_and_volume = -1
    volume_price = ''
    turnover_rate = -1
    pe_rate = -1
    amplitude = -1
    circulation = -1
    total_circulation = -1
    pb = -1
    up_stop = -1
    down_stop = -1

    def store2db(cur):
        cur.execute("INERT INTO stock_info(num,zone,name,now_price,yesterday_price,today_price,volume,outer_disc,inner_disc,buy_one,buy_one_volume,buy_two,buy_three,buy_four,buy_five,sell_one,sell_one_volume,sell_two,sell_three,sell_four,sell_five,transaction,transaction_time,change,change_percentage,top_price,low_price,price_and_volume,volume_price,turnover_rate,pe_rate,amplitude,circulation,total_circulation,pb,up_stop,down_stop) VALUES()")
        

conn = psycopg2.connect(database="stock", user="postgres", password="postgres", host="127.0.0.1", port="5432")
cur = conn.cursor()

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
        print( "has data")
        for result in match:
            for item in result:
                match_number = match_number+1
    else:
        continue

    # 数据库连接参数

    cur.execute("INSERT INTO stock(stock_id, tuijian)VALUES(%s , %s)", (stock_id, match_number))
    conn.commit()

cur.close()
conn.close()

