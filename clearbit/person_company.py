from clearbit.resource import Resource
from clearbit.error import (ParamsInvalidError)

class PersonCompany(Resource):
    endpoint = 'https://person.clearbit.com/v1/combined'

    @classmethod
    def find(cls, **options):
        if 'email' in options:
            url = '/email/' + options.pop('email')
        else:
            raise ParamsInvalidError('Invalid values')

        return cls.get(url, **options)
