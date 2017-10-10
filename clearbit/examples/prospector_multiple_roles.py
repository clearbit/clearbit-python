import clearbit

people = clearbit.Prospector.search(domain='clearbit.com', roles={'sales', 'marketing'})

for person in people:
  print(person['name']['fullName'])
  print(person.email)
