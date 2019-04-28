import requests
from bs4 import BeautifulSoup


base_url = 'http://opac.suda.edu.cn/m/weixin/wsearch.action'
question = input("请输入要查找的问题的关键字：")
page_num = int(input("输入查找页数："))
paylord = {'q': question, 't': 'any'}
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.\
        3683.75 Safari/537.36',
}


def url_open(base_url,headers):

    response = requests.get(url=base_url,headers=headers,params=paylord)
    url = response.url
    #print(url)
    result = requests.get(url,headers=headers)
    return result


def get_text(result):
    html = BeautifulSoup(result,'lxml')
    text1 = html.find_all('h4')
    text2 = html.find_all('li')
    final_text = zip(list(text1),list(text2))
    final_text = {}
    for i,n in zip(text1,text2):
        i = i.string
        n = n.string
        final_text[i] = n
    count =  1
    print("=======================")
    for k,v in final_text.items():
        print(count,end='>  ')
        count += 1
        print('《{0}》'.format(k),end='  ------  ')
        print(v)
    print("========下一页=========")


if __name__ == '__main__':
    for num in range(1,page_num+1):
        paylord['page'] = num
        result = url_open(base_url,headers)
        result = result.text
        get_text(result)




