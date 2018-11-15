import clearbit

response = clearbit.Prospector.search(domain='clearbit.com', roles={'sales', 'marketing'})

for person in response['results']:
  print(person['name']['fullName'])
  print(person.email)
