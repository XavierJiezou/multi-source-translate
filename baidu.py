import requests


def baidu_trans(query):
    url = 'https://fanyi.baidu.com/sug'
    data = {'kw': query}
    res = requests.post(url, data=data).json()
    return res['data'][0]['v']


if __name__ == "__main__":
    print(baidu_trans('hello'))
