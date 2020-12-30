'''
爬取 https://tu.cnzol.com/ 网页的美女图片
图片会分几种类型，每种类型的下面会有10几张图片，但是点进去只显示一张，是分页的
通过观察分析每一个页面的链接，下载所有页面的图片
爬取效果：
每一种类型为一个文件夹，每个文件夹下存放该类型的图片
'''

import requests
import bs4
from bs4 import BeautifulSoup

#获取页面信息的基本框架
def getHTML(url):
    headers = {
        'user-agent' : 'Mozilla/5.0'
    }
    try:
        re = requests.get(url,headers = headers,timeout = 30)
        re.raise_for_status
        re.encoding = re.apparent_encoding
        return re.text
    except:
        return ""

#获取页面的链接和每种类型的名字
def getLinkAndName(html,lst):
    '''
    html:获取的网页信息
    lst:存储解析出来的每个页面的信息，和每种类型的名字
    '''
    soup = BeautifulSoup(html,"html.parser")
    picMessage = soup.find('div',attrs = {'class':'m-list-main'}).find_all('li') #包含每组类型的链接和名字
    for item in range(len(picMessage)):
        picLink = picMessage[item].find('h2').find('a').get('href')
        picLink = 'https://tu.cnzol.com' + picLink #html页面中的链接不全
        picName = picMessage[item].find('h2').find('a').string
        lst.append([picLink,picName])

def main():
    url = 'https://tu.cnzol.com/'
    lst = []
    html = getHTML(url)
    getLinkAndName(html,lst)
    #print(lst)
    print('{:4}\t{:30}\t{:30}'.format('序号','类型名字','链接'))
    for i in range(len(lst)):
        print('{:4}\t{:30}\t{:30}'.format(i + 1,lst[i][1],lst[i][0]))

if __name__ == "__main__":
    main()
