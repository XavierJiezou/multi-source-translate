import requests


def baidu_trans(query):
    url = 'https://fanyi.baidu.com/sug'
    data = {'kw': query}
    res = requests.post(url, data=data).json()
    print(res['data'][0]['v'])


if __name__ == "__main__":
    baidu_trans('hello')
