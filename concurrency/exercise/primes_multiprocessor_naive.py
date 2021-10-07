#!/bin/env python3

import argparse
import multiprocessing as mp
from datetime import datetime

def isprime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def isprime_mp(s, ps, n):
  if isprime(n):
    ps[n] = True
  s.release()

def primes(n):
  ncpus = mp.cpu_count()
  s = mp.Semaphore(ncpus)

  ps = mp.Array('b', [False for i in range(0, n)])

  for i in range(2, n):
    s.acquire()
    p = mp.Process(target=isprime_mp, args=((s, ps, i)))
    p.start()

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
