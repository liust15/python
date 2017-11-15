#获取test表中的数据存储到toutiao中
import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='utf8'
)
connect2 = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='python',
    charset='utf8'
)
# 获取游标
cursor1 = connect.cursor()
cursor2 = connect2.cursor()
# 查询数据
sql = "SELECT * FROM pytest"
cursor1.execute(sql)
c=0;
for row in cursor1.fetchall():
    sql2="INSERT INTO  students_toutiao (id,image_url,title,media_creator_id,media_name)  VALUES ('" + str(row[0])+ "','" + row[1] + "','" + row[2] + "','" + str(row[3]) + "','" + row[4] +"')"
    cursor2.execute(sql2)
    connect2.commit()
    c=c+1
    print(c)
connect.close()
