import argparse

def find_max_profit(prices):
  # base case, buy, then sell
  profit = prices[1] - prices[0]
  for price_bought in prices[:-1]:
    # can only sell on lest element
    for price_sold in prices[prices.index(price_bought)+1:]:
      # iterates through all prices
      if (price_sold - price_bought) > profit:
        # if profit of current buy/sell is greater, then make that the new highest profit
        profit = price_sold - price_bought
  
  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))