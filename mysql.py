import random
from functools import reduce

import pymysql

connection = pymysql.connect(host='localhost',
                             port=9030,
                             user='root',
                             password='',
                             database='sys',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cur:
    range_ = ["(default,now(),'%s',%s,%s)" % (x,x, 1) for x in range(1,random.randint(2,20))]

    join = ','.join(range_)
    s='insert into mydb.hello_world values'+join
    execute = cur.execute(s)
    print(execute)
