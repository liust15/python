#coding=utf-8
import urllib.request  
import re
import pymysql
import json

def datas(data):
    db=pymysql.connect("localhost", "root", "root", "test" ,use_unicode=True, charset="utf8")  
    list=[]
    cursor = db.cursor()
    for jsons in data:
        j=json.loads(jsons)
        title=j["title"]
        d=(j["open_url"], j["group_id"],j["image_url"],title)
        list.append(d)
    try:  
        sql = 'INSERT INTO pytest(open_url,group_id,image_url,title) VALUES (%s, %s, %s,%s)'  
        # 批量插入  
        cursor.executemany(sql, list)  
        db.commit()  
    except Exception as e:  
        print(e)
        db.rollback()
        #cursor.executemany(sql,list)
    # 关闭数据库连接  
    db.close() 
def getHtml(url):
    #url1 = url.encode('utf-8')
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html
def getTitle(html):
    reg=r'({"open_url".*?})'
    title=re.compile(reg)
    titleList=re.findall(title,html)  
    return titleList
#jsons=getTitle(html)
#datas(jsons)
def ist(html):
    j=json.loads(html)
    data=j["data"]
    list=[]
    for j in data:
        try:
            d=(j["id"], j["title"],j["image_url"],j["media_creator_id"],j["media_name"])
            list.append(d)
        except KeyError as e:  
            print(e)
    db=pymysql.connect("localhost", "root", "root", "test" ,use_unicode=True, charset="utf8")  
    cursor = db.cursor()
    try:  
        sql = 'INSERT INTO pytest(id,title,image_url,media_creator_id,media_name) VALUES (%s, %s, %s,%s,%s)'  
        # 批量插入  
        cursor.executemany(sql, list)  
        db.commit()  
    except Exception as e:  
        print(e)
        db.rollback()
for i in range(20,40):
    j=i*20
    url="https://www.toutiao.com/search_content/?offset="+str(j)+"&format=json&keyword="+urllib.parse.quote("")+"&autoload=true&count=20&cur_tab=1"
    html = getHtml(url)
    ist(html)      
