# 我的而第一个爬虫程序
import requests
from bs4 import BeautifulSoup as bs

##指定访问客户端
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}

##定义按评分排列页面
myurl = 'https://maoyan.com/films?showType=3&sortId=3'

## 获取整个页面信息
response = requests.get(myurl,headers=header)

## 处理文文本信息
bs_info = bs(response.text, 'html.parser')

##调试信息打印
##print(bs_info)

# 通过for循环找到指定html节点，遍历获取电影基本信息
topNo=0
filmUrl=''
filmId=''
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    topNo = topNo + 1
    for atag in tags.find_all('div'):
        # 获取电影名字
        atag.find_all('div', attrs={'class': 'movie-hover-title'})
        if topNo==2:
            break
        print('序号:' + str(topNo))
    else:
        continue
    break
