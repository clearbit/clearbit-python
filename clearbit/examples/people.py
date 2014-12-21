import clearbit

person = clearbit.Person.find(email='alex@alexmaccaw.com',stream=True)
person.flag(given_name='Blah')