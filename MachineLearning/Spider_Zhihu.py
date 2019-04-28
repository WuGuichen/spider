import requests
from selenium import webdriver
from time import  sleep
from bs4 import BeautifulSoup
from lxml import etree


def bro_open1(new_url):

    browser = webdriver.Chrome()
    browser.get(new_url)
    for i in range(2):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(1)
    rhtml = browser.page_source
    browser.close()

    parse(rhtml)


def bro_open(rurl,dd):

    browser = webdriver.Chrome()
    browser.get(rurl)
    for i in range(2):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(1)
    rhtml = browser.page_source
    browser.close()
    get_url(rhtml,dd)


def parse(rhtml):

    element = etree.HTML(rhtml)
    text = BeautifulSoup(rhtml, "lxml")
    result1 = text.find_all('li')
    result3 = text.find_all('p')
    result2 = element.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div/div/div/div/span/text()')

    Result = []
    for result0 in result3:
        res1 = result0.string
        if res1 is not None:
            Result.append(res1)
    for result4 in result1:
        res2 = result4.string
        if res2 is not None:
            Result.append(res2)
    for result5 in result2:
        if result5 is not None:
            Result.append(result5)
    middle = [str(i) for i in Result]
    Final(middle)


def Final(middle):

    Final_Result = '\n'.join(middle)
    with open(filename+'.txt', 'w',encoding='utf-8') as f:
        f.write(Final_Result)
    print('over')

def url_open(url,headers,dd):

    response = requests.get(url,headers=headers,params=paylord)
    rurl = response.url
    sleep(1)
    bro_open(rurl,dd)


def get_url(rrr,dd):
    html = BeautifulSoup(rrr,"lxml")
    result = html.find_all('a',target='_blank',href=True)
    new = []
    for item in result:
        new.append(item['href'])
    base_url = "https://www.zhihu.com"
    count = 0
    for i in new:
        x = i.split("/")
        print(x)
        new_url = base_url + '/' + x[1] + '/' + x[2]
        count += 1
        if count < num+1:
            bro_open1(new_url)
            print(new_url)
            print("正在爬取第%d个问题回答......" % dd)
            dd += 1
            sleep(2)
        else:
            break


question = input("请输入要查找的问题的关键字：")
num = int(input("请输入要查找的问题数:"))
filename = input('请输入保存后的文件名：')
cookie = '_zap=22118b7c-43af-4ec5-9348-a6803566a841; d_c0="ABAmoOXfRQ-PTlYa3zFX2L4sysQqPlLuhMA=|1555167242"; q_c1=b16c55f1fef34b4a8401dcd3012337b5|1555173007000|1555173007000; capsion_ticket="2|1:0|10:1555173361|14:capsion_ticket|44:ZjcwNDE1ZjM0OGEyNDg4OTg4ZWJjY2JlNDViYWYxYWI=|096892e7aa32e15d0d32eab26e3f1ee01872728c4f4276e1bd93823b7bd89a67"; z_c0="2|1:0|10:1555173435|4:z_c0|92:Mi4xNS1lZEFnQUFBQUFBRUNhZzVkOUZEeVlBQUFCZ0FsVk5PMTZmWFFDQ1I2eHlnYkl2TURhdVN3MG45TWt0VXVadnpR|f8461b5410b131d758d8b365da2a7aa0ac5b0085b916592c8b3b777daba1a0a1"; tst=f; __gads=ID=44c70508f4ce1615:T=1555173595:S=ALNI_MZl8xR0Lcy7Pw0O5lLhvznvb4lWOA; __utmz=155987696.1555216555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155987696.1236189548.1555216555.1555229947.1555249098.3; _xsrf=9ygRkEqbQoe0FCWLVNmLnAB5cFYaUGTm; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d'


paylord = {'q': question, 'type': 'content'}
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.\
            3683.75 Safari/537.36',
        'cookies': cookie,
        'Origin': 'https: // www.zhihu.com',
        'Referer': 'https://www.zhihu.com/question/20190827',
    }


if __name__ == '__main__':

    dd = 1
    url = "https://www.zhihu.com/search"

    url_open(url,headers,dd)




