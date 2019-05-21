from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode


def main():
    q = input("-->")
    data = {
        'q': q,
        'keyfrom': 'new-fanyi.smartResult'
    }
    if is_chinese(q):
        url = 'http://dict.youdao.com/search?' + urlencode(data)
        flag = True
    else:
        url = 'http://dict.youdao.com/w/eng/' + q + '/#keyfrom=dict2.index'
        flag = False


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.\
                3683.75 Safari/537.36',
    }
    html = get_html(url, headers)
    result = get_result(html,flag)
    final_result = result
    for final_result in final_result:
        if final_result is not None:
            print(final_result.string)


def get_html(url, headers):
    response = requests.get(url=url, headers=headers)
    return response.text


def get_result(html, flag):
    soup = BeautifulSoup(html, 'lxml')
    if flag:
        result = soup.select('#phrsListTab > div > ul > p > span > a')
    else:
        result = soup.select('#phrsListTab > div.trans-container > ul > li')
    return result


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        main()
