import clearbit

companies = clearbit.Discovery.search(query={'tech':'marketo'}, sort='alexa_asc')

for company in companies['results']:
  print(company['name'])
