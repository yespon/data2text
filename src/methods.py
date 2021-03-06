# for the following functions
# input type: int(gvkey)

from datetime import datetime
import pandas as pd
from voluptuous import Schema, Required, MultipleInvalid
import num2words


# Currently we only cover S&P 500
company_info = pd.read_csv('../datasets/company_name_city.csv')
df = pd.read_csv('../datasets/stock_prices_info.csv')

def get_company_city(comp_id):
    """
    Example input: 'aapl', 'AAPL', 1075, 28733
    """
    res = 0
    if isinstance(comp_id, int):
        res = SP500_company_info.loc[SP500_company_info['gvkey']==comp_id, 'city']
    elif isinstance(comp_id, str):
        res = SP500_company_info.loc[SP500_company_info['tic']==comp_id.upper(), 'city']
    else:
        print('error: input must be ticker(str) or gvkey(int) of a valid company')
        return
    if res.any():
        return res.to_string(index=False)
    else:
        print('error: input must be ticker(str) or gvkey(int) of a valid company')
        return


# def get_company_name(**kwargs):
#     """
#     Example: "Murphy Oil Corporation"
#     :return: string (official full name)
#     """
#     s = Schema({
#         Required('df'): pd.DataFrame,
#         'row_id': int
#     })
#     try:
#         s(kwargs) # validate args
#         df = kwargs['df']
#         cpn_name = list(df.groupby('ticker')['Name'].head(1))
#         row_id = kwargs['row_id']
#         return cpn_name[row_id]
#     except MultipleInvalid as e:
#         print("error: {} occur while parse with required args".format(e.errors))


def get_company_name(**kwargs):
    """
    return company full name in company_info from ticker in stock_prices.csv

    :author: dyj
    :param kwargs:
    :return:
    """
    # param validation
    s = Schema({
            Required('df'): pd.DataFrame,
            Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        # ticker = df.iloc[row_id]['ticker']
        # fullname = str(company_info.loc[company_info['tic'] == ticker]['conml'])
        fullname = df.iloc[row_id, :].Name
        return fullname
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

# get_company_name(df=df, row_id=1)

def get_price_in_dollar(**kwargs):
    """
    return close price in stock_prices.csv

    :author: dyj
    :param kwargs:
    :return:
    """
    # param validation
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        close_price = df.iloc[row_id]['close']
        return close_price
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_volume_in_million(**kwargs):
    """
    return volume in million in stock_prices.csv

    :author: dyj
    :param kwargs:
    :return: str
    """
    # param validation
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        volume_num = int(df.iloc[row_id]['volume'])
        volume_str = "{0:.2f}".format(volume_num / 1000000, 2)
        return volume_str + ' million'

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_start_price(**kwargs):
    """
    return start price in stock_prices.csv

    :author: dyj
    :param kwargs:
    :return:
    """
    # param validation
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        start_price = df.iloc[row_id]['open']
        return start_price

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_close_price(**kwargs):
    """
    return close price

    :author: dyj
    :param kwargs:
    :return:
    """
    # param validation
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        close_price = df.iloc[row_id]['close']
        return close_price

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


#def get_ahead_or_behind(**kwargs):
#    """
#     return ahead or behind
#
#    :author: dyj
#    :param kwargs:
#    :return: 'ahead'/'behind'
#    """
#    # param validation
#    s = Schema({
#        Required('df'): pd.DataFrame,
#        Required('row_id'): int,
#    })
#    try:
#        s(kwargs)
#        df = kwargs['df']
#        row_id = kwargs['row_id']
#        close_price = df.iloc[row_id]['close']
#        return close_price
#
#    except MultipleInvalid as e:
#        print("error: {} occur while parse with required args".format(e.errors))

def get_company_tic(**kwargs):
    """
    Example: "MUR"
    :return: string (ticker)
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        'row_id': int
    })
    try:
        s(kwargs)  # validate args
        df = kwargs['df']
        row_id = kwargs['row_id']
        # ticker = list(df.groupby('ticker')['ticker'].head(1))
        # row_id = kwargs['row_id']
        ticker = df.iloc[row_id, :].ticker
        return ticker

    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_company_hq(**kwargs):
    """
    Example: "Cambridge, MA"
    :return: string (headquarter)
    """
    pass


def get_today_price(**kwargs):
    """
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    Note: This function can also be realized by calling get_history_price() and
    assigning today's date.
    :author: dyj
    :return: dict
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        'row_id': int,
    })
    try:
        s(kwargs)  # validate args
        df = kwargs['df']
        row_id = int(kwargs['row_id'])
        dict_ = {'open': str(df['open'][row_id]), 'high': str(df['high'][row_id]), 'low': str(df['low'][row_id]),
                 'close': str(df['close'][row_id]), 'volume': str(df['volume'][row_id])}
        return dict_
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))
    except TypeError as e:
        print("TypeError: ".format(e.errors))


# --------------------------------------------------------------------


def datestr2date(**kwargs):
    """
    two allowed format: "20170202" or "2017-02-02"
    :param datestr:
    :return: datetime object (date)
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df=s['df']
        row_id=s['row_id']
        datestr=df.iloc[row_id]['date']
        return datetime.strptime(datestr, "%Y%m%d").date()
    except:
        pass
    try:
        datestr = kwargs['datestr']
        return datetime.strptime(datestr, "%Y-%m-%d").date()

    except MultipleInvalid as e:
        print(
            "Error: input date string must be a valid date in two of the following formats: 'YYYYMMDD' or 'YYYY-MM-DD'".format(e.errors))
        return None


# --------------------------------------------------------------------
def get_trading_change_in_percent(**kwargs):
    """
    52-week low with trading change in percent
    :param kwargs:
    :return: str(percentage)
    Example: 0.2
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        res=trading_change(df,row_id)
        res=res if res>=0 else -res
        res=res*100
        return str(res)+"%"
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def trading_change(**kwargs):
    """
    return the value of trading_change
    :param kwargs:
    :return: float
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        curr_date = df['date']
        curr_low = float(df['low'])
        former_date = curr_date.datetime.now() - datetime.timedelta(days=365)
        former_low = float(df.loc[df['date'] == former_date and df['ticker'] == df.iloc[row_id]['ticker'],'low'])
        return 1-(curr_low/former_low)
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_ahead_or_behind(**kwargs):
    """
     return ahead or behind
    :param kwargs:
    :return: str
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        res = trading_change(df, row_id)
        out='ahead' if res<0 else 'behind'
        return out
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_increase_or_decrease(**kwargs):
    """
     return increase or decrease
    :param kwargs:
    :return: str
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        res = trading_change(df, row_id)
        out='increase' if res<0 else 'decrease'
        return out
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_forward_backward(**kwargs):
    """
    return increase or decrease
    :param kwargs:
    :return: str
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int,
        Required('n'):int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        n=kwargs['n']
        price=float(get_price_in_dollar(df,row_id))
        average=get_average_price(df,row_id,n)
        out = 'forward' if price>average else 'backward'
        return out
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_period_days(**kwargs):
    """
    return  #days
    :param int
    :return: str
    hzy
    """
    s = Schema({
        Required('n'): int
    })
    try:
        s(kwargs)
        n=kwargs['n']
        return str(n)
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_average_price(**kwargs):
    """
    Moving Average
    input type: pandas.DataFrame(df),int(n),int(row_id)
    return:float
    n represents # days
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('n'): int,
        Required('row_id'):int
    })
    try:
        s(kwargs)
        df=kwargs['df']
        n=kwargs['n']
        row_id=kwargs['row_id']
        df=df.iloc[row_id-n+1:row_id+1]
        summ=df['close'].sum()
        return summ*1.0/n
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))

def get_distance_percentage(**kwargs):
    """
    Distance percentage
    input type: pandas.DataFrame(df),int(n),int(row_id)
    return:float
    n represents # days
    hzy
        """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('n'): int,
        Required('row_id'): int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        n = kwargs['n']
        row_id = kwargs['row_id']
        price = float(get_price_in_dollar(df, row_id))
        average = get_average_price(df, row_id, n)
        dis=price-average if price-average>0 else average-price
        return str(dis*100.0/average)+"%"
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def get_last_trading_days(**kwargs):
    """
    return  # trading days
    :param int
    :return: str
    hzy
    """
    s = Schema({
        Required('n'): int
    })
    try:
        s(kwargs)
        n = kwargs['n']
        return str(n)
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))

def get_pulling_away_or_closer(**kwargs):
    """
    return pulling away or closer
    :param kwargs:
    :return: str
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        row_id = kwargs['row_id']
        price = float(get_price_in_dollar(df, row_id))
        average = get_30_days_average(df,row_id)
        out = 'pulling away' if price < average else 'closer'
        return out
    except MultipleInvalid as e:
        print("error: {} occur while parse with required args".format(e.errors))


def get_30_days_average(**kwargs):
    """
    Moving Average in 30 days
    input type: pandas.DataFrame(df),int(row_id)
    return:float
    hzy
    """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        n = 30
        row_id = kwargs['row_id']
        df = df.iloc[row_id - n + 1:row_id + 1]
        summ = df['close'].sum()
        return summ * 1.0 / n
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
def get_30_days_distance(**kwargs):
    """
    30 days Distance percentage
    input type: pandas.DataFrame(df),int(row_id)
    return:float
    hzy
        """
    s = Schema({
        Required('df'): pd.DataFrame,
        Required('row_id'): int
    })
    try:
        s(kwargs)
        df = kwargs['df']
        n = 30
        row_id = kwargs['row_id']
        price = float(get_price_in_dollar(df, row_id))
        average = get_30_days_average(df,row_id)
        dis=price-average if price-average>=0 else average-price
        return str(dis*100.0/average)+"%"
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))

def get_history_price(**kwargs):
    """
    input type: int(gvkey), dateObject(defined as above)
    return type: dict
    Example: {'open': 15, 'high': 16, 'low':14, 'close':15.5, 'volume': 154640}
    hzy
    """
    s=Schema({
        Required('df'):pd.DataFrame,
        Required('gvkey'):int,
        Required('date'):datetime

    })
    try:
        s(kwargs)
        df = kwargs['df']
        gvkey=kwargs['gvkey']
        date=kwargs['date']
        df=df.loc[df['gvkey']==gvkey and df['date']==date]
        return dict(['open', df['open']],['high',df['high']],['low',df['low']],['close', df['close']],['volume', df['volume']])
    except MultipleInvalid as e:
        print("error: input data is not valid".format(e.errors))
        return None

# def EMA(**kwargs):
#     """
#     ExponentialMoving Average
#     input type: pandas.DataFrame(df),int(n)
#     n represents # days
#     hzy
#     """
#     s = Schema({
#         Required('df'): pd.DataFrame,
#         'n': int
#     })
#     try:
#         s(kwargs)
#         df=kwargs['df']
#         n=kwargs['n']
#         return df.ewma(df['close'],n)
#     except MultipleInvalid as e:
#         print("error: input data is not valid".format(e.errors))
#
#
# def ROC(**kwargs):
#     """
#     Rate of Change
#     input type: pandas.DataFrame(df),int(n)
#     n represents # days
#     hzy
#     """
#     s = Schema({
#         Required('df'): pd.DataFrame,
#         'n': int
#     })
#     try:
#         s(kwargs)
#         df=kwargs['df']
#         n=kwargs['n']
#         return df['close'].diff(n-1)/df['close'].shift(n-1)
#     except MultipleInvalid as e:
#         print("error: input data is not valid".format(e.errors))
#
#
# def get_history_tech_ind(**kwargs):
#     """
#     return 7 days moving average, 30days moving average, 52 week rate of change
#     input type: int(gvkey), dateObject(defined as above)
#     Example: {'MA':70, "EMA": ..}
#     :return: dict
#     hzy
#     """
#     s=Schema({
#         Required('df'): pd.DataFrame,
#         Required('gvkey'):int,
#         Required('date'):datetime
#     })
#     try:
#         s(kwargs)
#         df=kwargs['df']
#         date=kwargs['date']
#         gvkey=kwargs['gvkey']
#         df=df.iloc[df['gvkey']==gvkey and df['date']==date]
#         row_id=df.index
#         return dict(['MA_7days',get_average_price(df,row_id,7)],['MA_30days',get_average_price(df,row_id,30)],['ROC_52week',ROC(df[row_id+52*7-1:row_id+1],row_id,52*7)])
#     except MultipleInvalid as e:
#         print("error: input is not valid".format(e.errors))


