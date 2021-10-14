import argparse
import numpy as np
import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import linear_model

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--db', type=str, required=True)
  parser.add_argument('--plot', action='store_true')
  parser.add_argument('--print', type=int, default=0)
  parser.add_argument('--predict', type=int, required=True)

  args = parser.parse_args()

  with sql.connect(args.db) as db:
    df = pd.read_sql('SELECT * FROM NET_USAGE', db, index_col='ID')
    df.dropna(inplace=True)

    # ('10.252.166.0', [[0.854, '2021-02-01 00:00:00'], [0.854, '2021-03-01 00:00:00'], ..])
    d = dict()
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

    preds = dict()
    coefs = dict()

    for id_, data in d.items():
      last_month = data[1][-1]

      # x werte für die Vorhersage: Letzter Monat + gewünschte Anzahl an Monaten
      x_test = np.array(range(last_month + 1, last_month + 1 + args.predict)).reshape((-1, 1))

      # data: [0.854, 0.854, 0.85, 0.732, 0.85, 0.85], [2, 3, 4, 5, 6, 7]
      # x_train: months -> data[1]
      # y_train: usage -> data[0]

      # You should call .reshape() on x because this array is required to be
      # two-dimensional, or to be more precise, to have one column and as many
      # rows as necessary
      x_train = np.array(data[1]).reshape((-1, 1))
      y_train = np.array(data[0])

      regr = linear_model.LinearRegression()
      regr.fit(x_train, y_train)
      y_pred = regr.predict(x_test)

      preds[id_] = (x_test, y_pred)
      coefs[id_] = regr.coef_

    for net, ps in preds.items():
      months = ps[0].reshape((1, -1))[0]
      usage_preds = ps[1]

      for n, month in enumerate(months):
        if usage_preds[n] > 0.95:
          print(f'VERY critical usage of {net} in month {month}')
        elif usage_preds[n] > 0.9:
          print(f'Critical usage of {net} in month {month}')

    if args.print > 0:
      for i in range(0, args.print):
        net, ps = preds.popitem()
        us = d[net]
        x_test = ps[0].reshape((1, -1))[0]
        y_pred = list(map(lambda v: round(v, 3), ps[1]))

        print(f'{net}:')
        print(f'Usage:          ', list(zip(us[1], us[0])))
        print(f'Predictions:    ', list(zip(x_test, y_pred)))
        print(f'Coefficients:    {coefs[net]}')
        print()

        if args.plot:
          plt.scatter(us[1], us[0], color='black')
          plt.plot(us[1], us[0], color='black')
          plt.scatter(x_test, y_pred, color='blue')
          plt.plot(x_test, y_pred, color='blue')

      if args.plot:
        plt.xticks(())
        plt.yticks(())
        plt.show()
