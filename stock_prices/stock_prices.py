#!/usr/bin/python

# input a list of stock prices
# return max profit between buy and sell
# it not buy at the last item on the list



import argparse
test =[100, 90, 80, 50, 20, 10]
def find_max_profit(prices):
  current_min_price = prices[0]
  current_max_price = prices[1]
  profit = 0
  max_profit = 0
 
  max_profit = current_max_price - current_min_price

  for i in range(1, len(prices)-1):
    profit = prices[i] - current_min_price
    print(prices[i])
    if profit > max_profit:
      max_profit = profit
    if prices[i] <= current_min_price:
      current_min_price = prices[i]
 
  return max_profit

print(find_max_profit(test))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))




  # first attempt

  #  for i in range(1 ,len(prices) -1):
  #   if prices[i] < current_min_price and prices[i] == len(prices) :

  #     current_min_price = prices[i-1]
  #     current_max_price = prices[i]
     
  #   elif prices[i] < current_min_price:
  #     current_min_price = prices[i]
   
  #   elif prices[i] > current_max_price and prices[i] == len(prices) -2:
  #     current_max_price = prices[i-2]
    
  #   elif prices[i] > current_max_price:
  #     current_max_price = prices[i]
  # max_profit = current_max_price - current_min_price