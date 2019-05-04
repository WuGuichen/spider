import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup


headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.\
            3683.75 Safari/537.36',
        'cookies': '_zap=22118b7c-43af-4ec5-9348-a6803566a841; d_c0="ABAmoOXfRQ-PTlYa3zFX2L4sysQqPlLuhMA=|1555167242"; \
            q_c1=b16c55f1fef34b4a8401dcd3012337b5|1555173007000|1555173007000; capsion_ticket="2|1:0|10:1555173361|14:\
            capsion_ticket|44:ZjcwNDE1ZjM0OGEyNDg4OTg4ZWJjY2JlNDViYWYxYWI=|096892e7aa32e15d0d32eab26e3f1ee01872728c4f42\
            76e1bd93823b7bd89a67"; z_c0="2|1:0|10:1555173435|4:z_c0|92:Mi4xNS1lZEFnQUFBQUFBRUNhZzVkOUZEeVlBQUFCZ0FsVk5P\
            MTZmWFFDQ1I2eHlnYkl2TURhdVN3MG45TWt0VXVadnpR|f8461b5410b131d758d8b365da2a7aa0ac5b0085b916592c8b3b777daba1a0\
            a1"; tst=f; __gads=ID=44c70508f4ce1615:T=1555173595:S=ALNI_MZl8xR0Lcy7Pw0O5lLhvznvb4lWOA; __utmz=155987696.\
            1555216555.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _xsrf=9ygRkEqbQoe0FCWLVNmLnAB5cFYaUGTm; __utm\
            a=155987696.1236189548.1555216555.1555249098.1556470651.4; tgw_l7_route=66cb16bc7f45da64562a077714739c11',
        'authority': 'www.zhihu.com',
        # ':path': '/search?type=content&q=df',
        'scheme': 'https',
        'referer': 'https://www.zhihu.com/topic/19550228/hot',
        'Origin': 'https://www.zhihu.com'

    }


def get_page_index(q, offset, lc_idx):
    data = {
        't': 'general',
        'q': q,
        'correction': '1',
        'offset': offset,
        'limit': '20',
        'lc_idx': lc_idx,
        'show_all_topics': '0',
        'search_hash_id': 'f3ec5407c1ee588650d5b41295c063b7',
    }
    url = 'https://www.zhihu.com/api/v4/search_v3?' + urlencode(data)
    print(url)

    try:
        response = requests.get(url, headers=headers)

        return response.text
    except RequestException:
        print('请求索引页出错')
        return None


def get_title(html):

    html = re.findall(r'<h1.*?>(.*?)</h1>.*?', html, re.M | re.S)
    return html


def get_content(html):
    text = BeautifulSoup(html, "lxml")
    text = text.find_all('span')
    for text in text:
        text = text.text
        yield text
    return text


def make_text(result):
    title = get_title(result)
    content = get_content(result)
    title = ['《' + title[0] + '》']
    content = [x for x in content]
    text = title + content
    # with open('zhi' + '.txt', 'w', encoding='utf-8') as f:
    for t in text:
            # f.write(t)
        print(t)

def main():
    page_num = 1
    for num in range(1, page_num+1):
        html = get_page_index('web', 20+num*20, 20+num*20+5)
        url_list = get_url(html)
        for i in range(1):
            try:
                result = url_open(url_list.__next__())
                text = make_text(result)
                print(text)
            except:
                print('本页结束.')


def make_file(text):
    print(text)


def get_url(text):
    res1 = r'.*?"title":"(.*?)"},"object":{"id":"(.*?)","type":"(.*?)",.*?'
    res2 = r'.*?"question":{"id":"(.*?)","type":"question","name":"(.*?)",.*?'
    text1 = re.findall(res1, text, re.S | re.M)
    text2 = re.findall(res2, text, re.S | re.M)
    for t1 in text1:
        for t2 in text2:
            if t1[0] == t2[1]:
                url = 'https://www.zhihu.com/question/' + t2[0]
                yield url


def url_open(url):
    response = requests.get(url, headers=headers)
    print(response.url)
    html = response.text
    return html


if __name__ == '__main__':
    main()
