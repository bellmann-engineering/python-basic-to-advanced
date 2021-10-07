#!/bin/env python3

import argparse
import multiprocessing as mp
from datetime import datetime

def isprime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def isprime_mp(stop, q, ps):
  while True:
    n = q.get()
    if isprime(n):
      ps[n] = True
    q.task_done()

def primes(n):
  q = mp.JoinableQueue()

  for i in range(2, n):
    q.put(i)

  ps = mp.Array('b', [False for i in range(2, n)])

  procs = []
  for i in range(0, mp.cpu_count()):
    stop = mp.Event()
    proc = mp.Process(target=isprime_mp, args=((stop, q, ps)), daemon=True)
    proc.start()
    procs.append((stop, proc))

  if q.join():
    q.close()

  for i, isprime in enumerate(ps):
    if isprime:
      yield i

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--n', type=int, default=10)
  parser.add_argument('--print', action='store_true')

  args = parser.parse_args()

  print(f'calculating up to {args.n} primes.')
  start = datetime.now()
  ps = list(primes(args.n))
  end = datetime.now()
  print(f'done. found {len(ps)} primes in {end - start}.')
  if args.print:
    print(ps)
