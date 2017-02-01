#!/usr/bin/python

import mysql.connector
import work_times_mysql_cfg as cfg

def record_time(start, end):
    cnx = mysql.connector.connect(user=cfg.MYSQL_USER, password=cfg.MYSQL_PASS,
                                  host=cfg.MYSQL_HOST,
                                  database=cfg.MYSQL_DATABASE)

    cursor = cnx.cursor()
    sql_statement = "INSERT work_times (start, end) VALUES ('{}', '{}')".format(start, end)
    cursor.execute(sql_statement)
    cnx.commit()
    cnx.close()
    
if __name__ == '__main__':
    pass