COINS = { 1: "Penny", 5: "Nickel", 10: "Dime", 25: "Quarter"}

def makeSmallerCoins(coins, coin):
  """
  Takes a collection of coins, and one value of coin.

  Returns a list of the coins from the collection that are smaller or equal to
  the given coin
  """
  smallerCoins = []
  for maybeIncludeMe in coins:
    if maybeIncludeMe <= coin:
      smallerCoins.append(maybeIncludeMe)
  return smallerCoins

def incrementCoin(way, coin):
  if coin in way:
    way[coin] = way[coin]+1
  else:
    way[coin] = 1

def change(amount, coins):
  if amount == 0:
     return [{}]
  elif amount == 1:
     return [{"Penny": 1}]
  ways = []
  for coin in coins:
    if amount >= coin:
      smallerCoins = makeSmallerCoins(coins, coin)
      for thisWay in change(amount-coin, smallerCoins):
        thisCoin = COINS[coin]
        incrementCoin(thisWay, thisCoin)
        ways.append(thisWay)
  return ways
