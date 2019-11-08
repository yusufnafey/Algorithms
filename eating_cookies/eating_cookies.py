#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # base case, 0 cookies can be eaten 1 way
  if n == 0:
      return 1
  # base case, 1 cookie can be eaten 1 way and 2 cookies can be eaten 2 ways
  if n <= 2:
      return n
  elif cache and cache[n] > 2:
      return cache[n]
  else:
      if not cache:
        # if it's not cached, compute hard way
        cache = {i: 0 for i in range(n+1)}
      cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
      # if it is in cache, return
      return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')