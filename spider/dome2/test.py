#coding=utf-8
#!/usr/bin/python3
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
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html
def getTitle(html):
    reg=r'({"open_url".*?})'
    title=re.compile(reg)
    titleList=re.findall(title,html)  
    return titleList

    

   

html = getHtml("https://www.toutiao.com/ch/news_hot/")
#getTitle(html)
jsons=getTitle(html)
datas(jsons)
# j='{"open_url":"\/group\/6482643985016816142\/","group_id":"6482643985016816142","image_url":"\/\/p1.pstatp.com\/list\/240x240\/434b0000766958bcb936","title":"\u4e3b\u6301\u5e38\u52a1\u5de5\u4f5c\u4e09\u5e74\u65f6\u95f4 \u4e2d\u592e\u6587\u660e\u529e\u4e3b\u4efb\u9ec4\u5764\u660e\u51fa\u4efb\u4e2d\u5ba3\u90e8\u90e8\u957f"}'
# text = json.loads(j)
#print(jsons)


#lists(json)