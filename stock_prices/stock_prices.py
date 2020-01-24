#!/usr/bin/python

import argparse

def find_max_profit(prices):
      # Set the current_min_price to an arr[0].
      # Then we set the max_profit equal to max price - min price  
      current_min_price = prices[0]
      max_profit = prices[1] - prices[0]
      
      # Next we do a for loop of i that's in range starting at 1 and comparing it to the length of prices.
      for i in range(1, len(prices)):
            # if the index of prices is less than the current_min_price then the current_min_price is equal to the index of prices.
            if prices[i] < current_min_price:
                  current_min_price = prices[i]
            # else if index of prices - the current_min_price is greater than the max_profit, then the max_profit is equal to the index of prices - current_min_price.
            elif prices[i] - current_min_price > max_profit:
                  max_profit = prices[i] - current_min_price
  
      return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))