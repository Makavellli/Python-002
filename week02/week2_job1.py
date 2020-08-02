# 我的第一个爬虫程序 获取猫眼电影按评分排名前10的电影基本信息
#
#2020年8月3日 修改了电影基本信息的获取方式 并对结果进行了规范格式化处理
#
#2020年8月3日 增加电影基本保存至MySQL数据库功能

#############################################################
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymysql


# 指定访问客户端i
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'

## Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
header = {'user-agent':user_agent}

# 定义按评分排列页面
myurl = 'https://maoyan.com/films?showType=3&sortId=3'

# 获取整个页面信息
response = requests.get(myurl,headers=header)
# print(response)

# 处理文文本信息
bs_info = bs(response.text, 'html.parser')
# print(bs_info)
# 通过for循环找到指定html节点，遍历获取电影基本信息
# topNo=0
film_name =''
film_name =''
film_name =''
film_list = []
sub_tags = []
# 定位电影基本信息位置
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[0:10]:
#    topNo+=1
# 遍历电影基本信息节点获取 查找到html节点是div，class属性值是‘movie-hover-title’的所有节点
#   print('targs##########################'+tags)
    sub_tags = tags.find_all('div', attrs={'class': 'movie-hover-title'})

#   获取第1个div节点的中html节点是span，class属性值是name的文本内容 也就是电影名称
    film_name = sub_tags[0].find('span', attrs={'class': 'name'}).text
#   获取第2个div节点的中html节点是span，class属性值是name的文本内容 也就是电影名称
#   replace("\n", "") 替换换行
#   split(":")[1] 用‘:’分割字符串，并取第二个
#   strip() 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#    
    film_type = sub_tags[1].text.replace("\n", "").split(":")[1].strip()   
    film_time = sub_tags[3].text.replace("\n", "").split(":")[1].strip()
#   print(film_type)
#   print(film_time)
    film_list.append((
            film_name,
            film_type,
            film_time,
    ))

# 保存至MySQL数据库

# print(film_list)

# 获取数据库连接 配置数据库连接信息
conn = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='123456',
    database='geekbang',
    charset='utf8'
)
# 获取一个游标,游标建立的时候就开启了一个隐形的事物
cursor = conn.cursor()
# print(cursor)
# 定义要执行的sql语句
sql = 'insert into MAOYAN(Name,Type,Time) values(%s,%s,%s);'

# 增加异常捕获
try:
# 拼接并执行sql语句
    cursor.executemany(sql, film_list)
    cursor.close()
    conn.commit()
except:
    conn.rollback()
# 关闭数据库连接
    conn.close()