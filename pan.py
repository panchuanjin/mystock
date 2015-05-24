#!/usr/bin/python3.4

import urllib.request
import psycopg2
import re




# python url use:
fp = urllib.request.urlopen("http://data.eastmoney.com/report/600011.html")

mybytes = fp.read()
# note that Python3 does not read the html code as string
# but as html code bytearray, convert to string with
mystr = mybytes.decode("gbk")

fp.close()

#print(mystr)
match_number = 0
pattern = re.compile(r"强烈推荐")
match = pattern.findall(mystr)
if match:
    for result in match:
        for item in result:
            match_number = match_number+1
#            print(item,end=" ")
#            print item

print(match_number)
#print match_number

# 数据库连接参数
#conn = psycopg2.connect(database="stock", user="postgres", password="postgres", host="127.0.0.1", port="5432")
#cur = conn.cursor()
#cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
# insert one item
#cur.execute("INSERT INTO stock(stock_id, stock_name,raw_data)VALUES(%s ,%s, %s)", (1, 'aaa','asdfasf'))
#cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
#cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))

#cur.execute("SELECT * FROM stock;")
#rows = cur.fetchall()        # all rows in table
#print(rows)
#for i in rows:
#    print(i)
#conn.commit()
#cur.close()
#conn.close()
