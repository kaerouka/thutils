def create_date(sy=1900, sm=1, sd=1, ey=2015, em=12, ed=31, cnt=50):
    """指定された範囲内の、ランダムな日次を生成して返します。
    :param sy:開始年
    :param sm:開始月
    :param sd:開始日
    :param ey:終了年
    :param em:終了月
    :param ed:終了日
    :param cnt:生成数
    :return:
    """
    import datetime
    import random
    L = []
    s = datetime.datetime(sy, sm, sd)
    e = datetime.datetime(ey, em, ed)

    d = (e - s).days

    for i in range(d):
        L.append(s + datetime.timedelta(days=i))

    L2 = []
    for i in range(cnt):
        L2.append(random.choice(L).strftime('%Y%m%d'))

    return L2


def join_tables(*arys, how='outer', keys=None):
    """2つ以上のテーブルを結合する。
    :param how: テーブルのjoin方法。left or right or outer。
    :param arys:データの2次元配列。0行目は列名扱い。
    :param keys:PKを指定したい場合、配列で指定する。
    :return: pandasのDataFrame
    """
    import pandas as pd

    t = pd.DataFrame(arys[0][1:], columns=arys[0][0])

    for i, table in enumerate(arys[1:]):
        df = pd.DataFrame(table[1:], columns=table[0])
        pk = find_pk(t.columns.tolist(), table[0], keys)

        t = pd.merge(t, df, on=pk, how=how)

    return t


def find_pk(parent_table_columns, child_table_columns, keys=None):
    """たぶんPKじゃね？って項目名を見つける。
    :param parent_table_columns:親のテーブルのカラム
    :param child_table_columns: 子のテーブルのカラム
    :param keys: PKが予めわかっている場合にリスト形式で指定する
    :return: プライマリーキーと思われる列名の配列
    """
    commons = set(parent_table_columns).intersection(child_table_columns)

    if keys is None:
        return [x for x in commons if 'id' in x.lower()]
    else:
        return [x for x in commons if x.lower() in keys]


