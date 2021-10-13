import argparse
import pandas as pd
import sqlite3 as sql
from datetime import datetime

# reshape to ID, NET, USAGE, TIMESTAMP
def reshape(df):
  # [datetime.datetime(2021, 2, 1, 0, 0), datetime.datetime(2021, 3, 1, 0, 0), ..
  dates = []
  for m in range(2,8):
    dates.append(datetime(2021, m, 1))

  usage = []
  for d in df.values:
    # d[0]: net -> '10.252.114.0'
    # d[1::2]: usage (every 2. value):
    # ['10.252.114.0' 0.125 0 0.125 0 0.125 0 0.196 0 0.125 0 0.125 0.0]
    #   -> [0.125 0.125 0.125 0.196 0.125 0.125]
    # zip(d[1::2], dates):
    # [(0.125, datetime.datetime(2021, 2, 1, 0, 0)), (0.125, datetime.datetime(2021, 3, 1, 0, 0)), ..
    # map:
    # [(0.125, datetime.datetime(2021, 2, 1, 0, 0)), (0.125, datetime.datetime(2021, 3, 1, 0, 0)), ..
    #   -> [('10.252.114.0', 0.125, datetime.datetime(2021, 2, 1, 0, 0)), ('10.252.114.0', 0.125, datetime.datetime(2021, 3, 1, 0, 0)), ..
    for u in map(lambda u: [d[0], u[0], u[1]], zip(d[1::2], dates)):
      usage.append(u)
    # usage.append(map(lambda u: [d[0], u[0], u[1]], zip(d[1::2], dates)))

  res = pd.DataFrame(usage, columns=['NET', 'USAGE', 'TIMESTAMP'])
  res.index.name = 'ID'
  return res

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--db', type=str, required=True)
  parser.add_argument('--data', type=str, required=True)

  args = parser.parse_args()

  with sql.connect(args.db) as db:
    df = pd.read_excel(args.data)
    df.drop(0, inplace=True)

    # A (0), H (7) - S (18)
    # : selects all rows
    reshaped = reshape(df.iloc[:, [0] + list(range(7, 19))])

    reshaped.to_sql('NET_USAGE', db)
