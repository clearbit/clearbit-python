import clearbit

person = clearbit.Person.find(email='alex@clearbit.com',stream=True)
# person.flag(given_name='Blah')

print(person)
