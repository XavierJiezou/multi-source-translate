import requests


def youdao_trans(query):
    url = 'http://fanyi.youdao.com/translate'
    data = {
        "i": query,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16081210430989",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    res = requests.post(url, data=data).json()
    return res['translateResult'][0][0]['tgt']


if __name__ == "__main__":
    print(youdao_trans('hello'))
