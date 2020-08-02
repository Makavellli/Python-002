# 我的第一个爬虫程序 获取猫眼电影按评分排名前10的电影基本信息
#
#2020年8月3日 修改了电影基本信息的获取方式 并对结果进行了规范格式化处理
#
#############################################################
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 指定访问客户端i
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
header = {'user-agent':user_agent}

# 定义按评分排列页面
myurl = 'https://maoyan.com/films?showType=3&sortId=3'

# 获取整个页面信息
response = requests.get(myurl,headers=header)

# 处理文文本信息
bs_info = bs(response.text, 'html.parser')

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
    sub_tags = tags.find_all('div', attrs={'class': 'movie-hover-title'})
#    print("***************tags***************")
#    print(sub_tags)
#   获取第1个div节点的中html节点是span，class属性值是name的文本内容 也就是电影名称
    film_name = sub_tags[0].find('span', attrs={'class': 'name'}).text
#   获取第2个div节点的中html节点是span，class属性值是name的文本内容 也就是电影名称
#   replace("\n", "") 替换换行
#   split(":")[1] 用‘:’分割字符串，并取第二个
#   strip() 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#    
    film_type = sub_tags[1].text.replace("\n", "").split(":")[1].strip()
#    print("***************sub_tags_1***************")
#    print(sub_tags[1])
#    print("info********"+sub_tags[1].text)
#    print("info********"+sub_tags[1].text.replace("\n", ""))
#    print("info********")
#    print(sub_tags[1].text.replace("\n", "").split(":"))
#    print("info********"+sub_tags[1].text.replace("\n", "").split(":")[1])
#    print("info********"+sub_tags[1].text.replace("\n", "").split(":")[1].strip())
   
    film_time = sub_tags[3].text.replace("\n", "").split(":")[1].strip()

#  print('电影名称：'+film_name)
#  print('电影类型：'+film_type)
#  print('上映时间：'+film_time)

#    print('当前序号是：'+str(topNo))
# 判断当前为第几个 第10个的时候跳出循环
#    if topNo == 10:
#        break
#    else:
#        continue
#    break
    film_list.append({
            "name": film_name,
            "type": film_type,
            "time": film_time,
        })

films = pd.DataFrame(data = film_list)
# 保存为csv文件
films.to_csv('./films_V2.csv', encoding='UTF-8', index=False, header=False)