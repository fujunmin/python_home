#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入第三方库
import cx_Oracle
import os
# 导入配置文件
from global_config import DB_ADDRESS, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

# NLS_LANG设置及编码转换
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 数据库连接
def conndb(db_address=DB_ADDRESS, db_username=DB_USERNAME, db_password=DB_PASSWORD, db_name=DB_NAME, db_port=DB_PORT):
    dsn_tns = "%s:%d/%s" %(db_address, db_port, db_name)
    db = cx_Oracle.connect(db_username, db_password, dsn_tns)
    return db

# 数据库查询操作
def selectdb(db, sql):
    """
    SELECT：用于检索数据
    """
    cursor = db.cursor()
    cursor.execute(sql)
    rst=cursor.fetchall()
    cursor.close()
    return rst

# 数据库更新(插入,更新,删除数据)操作
def updatedb(db, sql, para=None):
    cursor = db.cursor()
    if para:
        cursor.execute(sql, para)
    else:
        cursor.execute(sql)
    cursor.close()
    db.commit()

def closedb(db):
    db.close()

def printResult(rs):
    for row in rs:
        print row

# db = conndb()
# sr = selectdb(db, u"select * from s_en_baseinfo where entname='汉柏科技有限公司'")
# closedb(db)
# for row in sr:
#     print row
#     print row[2]

# db = cx_Oracle.connect('NEWDAAS', 'NEWDAAS2016', '192.168.205.55:1521/orcl')
# db = cx_Oracle.connect('NEWDAAS/NEWDAAS2016@192.168.205.55:1521/orcl')
# dsn_tns = cx_Oracle.makedsn('192.168.205.55', 1521, 'orcl')
# db = cx_Oracle.connect('NEWDAAS', 'NEWDAAS2016', dsn_tns)