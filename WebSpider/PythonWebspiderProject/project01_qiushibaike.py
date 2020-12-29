'''
爬取糗事百科上的文字笑话
'''

import requests
from bs4 import BeautifulSoup
import bs4

#获取网页信息的基本框架
def getHTMLtext(url):
    kv = {
        'user-agent':'Mozilla/5.0'
    } #伪装成浏览器
    try:
        re = requests.get(url,timeout = 30,headers = kv)
        re.raise_for_status
        re.encoding = re.apparent_encoding
        #print(re.text)
        return re.text
    except:
        return ""



def parseHTML(html,lst):
    try:
        soup = BeautifulSoup(html,"html.parser")
        soup_content = soup.find_all('div',attrs={'class':'content'})
        for i in range(len(soup_content)):
            content = soup_content[i].find('span').text
            # content = content.repalce('\n','')
            lst.append(content)
    except:
        print("")
    

def printMessage(lst):
    fmt = '{:4}\t{:}'
    print(fmt.format('序号','内容'))
    for i in range(len(lst)):
        print(fmt.format(i + 1,lst[i]))

def main():
    url = "https://www.qiushibaike.com/text/"
    html = getHTMLtext(url)
    jokeList = []
    parseHTML(html,jokeList)
    printMessage(jokeList)

if __name__ == "__main__":
    main()
