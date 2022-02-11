# 正股涨停
import pandas as pd
from io import StringIO

# 从tushare抽取出来的，获取指数的代码

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

INDEX_HEADER = 'code,name,open,preclose,close,high,low,0,0,volume,amount,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,d,c,3\n'

INDEX_COLS = ['code', 'name', 'change', 'open', 'preclose', 'close', 'high', 'low', 'volume', 'amount']
FORMAT = lambda x: '%.2f' % x
FORMAT4 = lambda x: '%.4f' % x


def get_index():
    headers = {'Referer': 'http://finance.sina.com.cn/'}
    url = 'https://hq.sinajs.cn/rn=xppzh&list=sh000001,sh000002,sh000003,sh000008,sh000009,sh000010,sh000011,sh000012,sh000016,sh000017,sh000300,sh000905,sz399001,sz399002,sz399003,sz399004,sz399005,sz399006,sz399008,sz399100,sz399101,sz399106,sz399107,sz399108,sz399333,sz399606'

    request = Request(url, headers=headers)
    text = urlopen(request, timeout=10).read()

    text = text.decode('GBK')
    text = text.replace('var hq_str_sh', '').replace('var hq_str_sz', '')
    text = text.replace('";', '').replace('"', '').replace('=', ',')
    text = '%s%s' % (INDEX_HEADER, text)

    df = pd.read_csv(StringIO(text), sep=',', thousands=',')
    df['change'] = (df['close'] / df['preclose'] - 1) * 100
    df['amount'] = df['amount'] / 100000000
    df['change'] = df['change'].map(FORMAT)
    df['amount'] = df['amount'].map(FORMAT4)
    df = df[INDEX_COLS]
    df['code'] = df['code'].map(lambda x: str(x).zfill(6))
    df['change'] = df['change'].astype(float)
    df['amount'] = df['amount'].astype(float)
    return df
