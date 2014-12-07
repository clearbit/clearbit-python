from clearbit import Person
from clearbit import Company
from clearbit import PersonCompany

class PersonCompany(PersonCompany):
    endpoint = 'https://person-stream.clearbit.com/v1/combined'

class Person(Person):
    endpoint = 'https://person-stream.clearbit.com/v1/person'

class Company(Company):
    endpoint = 'https://company-stream.clearbit.com/v1/company'
