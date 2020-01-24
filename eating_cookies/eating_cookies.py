#!/usr/bin/python

import sys

# Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

# For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

#  1. He can eat 1 cookie at a time 3 times
#  2. He can eat 1 cookie, then 2 cookies 
#  3. He can eat 2 cookies, then 1 cookie
#  4. He can eat 3 cookies all at once. 

# Thus, `eating_cookies(3)` should return an answer of 4.

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
      if cache is None or type(cache) == list:
            cache = {0: 1, 1: 1, 2: 2}
      # If n is less than 0, it will return 0.
      if n < 0:
            return 0
      # Otherwise if n is not in cache, then cache[n] will breakdown the amount of cookies (like a tree with roots).
      elif n not in cache:
            cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n -3, cache)
      return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')