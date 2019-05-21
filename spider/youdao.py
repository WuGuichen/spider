from bs4 import BeautifulSoup
import requests


def main():
    q = '地'
    url = 'http://dict.youdao.com/search'
    payload = {
        'q': q,
        'keyfrom': 'new-fanyi.smartResult'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.\
                3683.75 Safari/537.36',
    }
    html = get_html(url, headers, payload)
    result = get_result(html)
    final_result = result
    for final_result in final_result:
        if final_result is not None:
            print(final_result.string)


def get_html(url, headers, payload):
    response = requests.get(url=url, headers=headers, params=payload)
    return response.text


def get_result(html):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('#phrsListTab > div > ul > p > span > a')
    return result


if __name__ == "__main__":
    main()
