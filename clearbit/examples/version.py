import clearbit

clearbit.PersonCompany.set_version('2015-05-30')

result = clearbit.PersonCompany.find(email='alex@clearbit.com',webhook_url='http://requestb.in/om0hqqom')
print(result)
