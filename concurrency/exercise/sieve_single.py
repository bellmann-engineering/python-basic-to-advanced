#!/bin/env python3

import argparse
from datetime import datetime

def sieve(n):
  # create boolean array primes[0..n] and initialize to False
  primes = [False for i in range(n+1)]
  p = 2

  while (p * p <= n):
    # if primes[p] is unchanged then it is a prime
    if (primes[p] == False):
      # update all multiples of p
      for i in range(p**2, n+1, p):
        primes[i] = True
    p += 1

  # yield primes
  for p in range(2, n+1):
    if not primes[p]:
      yield p

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--n', type=int, default=10)
  parser.add_argument('--print', action='store_true')

  args = parser.parse_args()

  print(f'calculating up to {args.n} primes.')
  start = datetime.now()
  primes = list(sieve(args.n))
  end = datetime.now()
  print(f'done. found {len(primes)} primes in {end - start}.')
  if args.print:
    print(primes)
