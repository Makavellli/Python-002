# 我的而第一个爬虫程序 获取猫眼电影按评分排名前10的电影基本信息
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


##指定访问客户端
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}

##定义按评分排列页面
myurl = 'https://maoyan.com/films?showType=3&sortId=3'

## 获取整个页面信息
response = requests.get(myurl,headers=header)

## 处理文文本信息
bs_info = bs(response.text, 'html.parser')

# 通过for循环找到指定html节点，遍历获取电影基本信息
topNo=0
filmName=''
list=[]
# 定位电影基本信息位置
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    topNo+=1
# 遍历电影基本信息节点获取
    for info in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        filmName=info.text
        list.append(filmName.replace(' ', ''))
        print(filmName.replace(' ', ''))

    print('当前序号是：'+str(topNo))
# 判断当前为第几个 第10个的时候跳出循环
    if topNo == 10:
        break
    else:
        continue
    break

movie1 = pd.DataFrame(data = list)
# 保存为csv文件
movie1.to_csv('./films.csv', encoding='GBK', index=False, header=False)
