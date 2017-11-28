# coding=utf-8
import re
import pymysql
#获取所有好友的qq号

def datas(data):
    db = pymysql.connect("localhost", "root", "root",
                         "test", use_unicode=True, charset="utf8mb4")
    list = []
    cursor = db.cursor()
    i=0
    for jsons in data:
        d = (jsons[0], jsons[1])
        i=i+1
        list.append(d)
    try:
        sql = 'INSERT INTO qq(qqname,qqnum) VALUES (%s, %s)'
        # 批量插入
        cursor.executemany(sql, list)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        # cursor.executemany(sql,list)
    # 关闭数据库连接
    db.close()


data = open('data.txt')
a = data.read()
b = re.findall(
    r"<span class=\"name tf\">(.+?)</span><span class=\"email tf\">(.+?)@qq.com</span>", a)
datas(b)
# for jsons in b:
#     d = (jsons[0], jsons[1])
#     print(d)
