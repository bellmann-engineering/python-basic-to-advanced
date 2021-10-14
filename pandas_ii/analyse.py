import argparse
import pandas as pd
import sqlite3 as sql
from datetime import datetime
from sklearn import linear_model

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--db', type=str, required=True)

  args = parser.parse_args()

  with sql.connect(args.db) as db:
    df = pd.read_sql('SELECT * FROM NET_USAGE', db, index_col='ID')
    df.dropna(inplace=True)

    # ('10.252.166.0', [[0.854, '2021-02-01 00:00:00'], [0.854, '2021-03-01 00:00:00'], ..])
    d = dict()
    # usage_len = dict()
    # last_month = dict()
    for v in df.values:
      id_ = v[0]
      usage_vs = v[1:].tolist()
      usage = usage_vs[0]
      month = datetime.fromisoformat(usage_vs[1]).month

      if id_ in d:
        d[id_][0].append(usage)
        d[id_][1].append(month)
      else:
        d[id_] = ([usage], [month])

      # old_usage_len = 0
      # new_usage_len = len(d[id_][0])
      # if id_ in usage_len:
      #   old_usage_len = usage_len[id_]

      # if new_usage_len > old_usage_len:
      #   usage_len[id_] = new_usage_len

      # if id_ in last_month:
      # usage_len[id_] = len(d[id_][0])
      # last_month[id_] = month

    # print(d.popitem())
    # exit()

    preds = dict()
    # x_test = [ datetime(2021, m, 1) for m in range(8,11) ]
    # x_test = [list(range(8,14))]

    for id_, data in d.items():
      # ul = usage_len[id_]
      usage_len = len(data[0])
      last_month = data[1][-1]
      x_test = [list(range(last_month + 1, last_month + 1 + usage_len))]
      # data: [0.854, 0.854, 0.85, 0.732, 0.85, 0.85], [2, 3, 4, 5, 6, 7]
      y_train = [data[0]]
      # print(usage_vs, usage_vs[0], usage_vs[1])
      x_train = [data[1]]
      # x_train = 

      # print(f'y_train {y_train}')
      # print(f'x_train {x_train}')
      regr = linear_model.LinearRegression()
      regr.fit(x_train, y_train)
      y_pred = regr.predict(x_test)
      # print(f'y_pred {y_pred}')

      preds[id_] = (x_test, y_pred)

      # break

    for i in range(0,5):
      net, ps = preds.popitem()
      us = d[net]

      # print(ps[0], ps[1])
      print(f'Usage for {net}:')
      print(list(zip(us[1], us[0])))
      print(f'Predictions for {net}:')
      print(list(zip(ps[0][0], ps[1].tolist()[0])))
