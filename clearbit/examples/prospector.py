import clearbit

response = clearbit.Prospector.search(domain='clearbit.com')

for person in response['results']:
  print(person['name']['fullName'])
  print(person.email)
