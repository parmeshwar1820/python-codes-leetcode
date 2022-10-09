max_profit=0
i=0
j=0
min_element=prices[i]
while i<=j and j<len(prices):
  if prices[j]<prices[i]:
    i=j
  elif prices[j]-prices[i]>max_profit:
    max_profit=prices[j]-prices[i]
    j+=1
return max_profit
