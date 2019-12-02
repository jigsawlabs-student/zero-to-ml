```python
def decision_tree(customer):
  if customer['college'] == True:
  	return 1
  elif customer['college'] == False:
  	return 0
  else:
  	if customer['under_thirty']:
      return 0
    else:
      return 1
```

