#!/usr/bin/python
# -*- coding: UTF-8 -*-

#需要安装的包
#pip install PyMySQL

import pymysql.cursors

print 'Hello World!'

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM user "
        cursor.execute(sql,)
        result = cursor.fetchall()
        for one in result:
            print one['name']
finally:
    connection.close()


