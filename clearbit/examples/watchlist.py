import clearbit

results = clearbit.WatchlistEntity.search(name='Ferland', fuzzy=True)

for result in results:
  print(result)
