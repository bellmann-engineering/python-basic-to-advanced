#!/bin/env python3

import argparse
from datetime import datetime

def isprime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def primes(n):
  for i in range(2, n):
    if isprime(i):
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
