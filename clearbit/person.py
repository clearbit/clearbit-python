from clearbit.resource import Resource
from clearbit.error import (ParamsInvalidError)

class Person(Resource):
    endpoint = 'https://person.clearbit.com/v1/people'

    @classmethod
    def find(cls, **options):
        if 'email' in options:
            url = '/email/' + options.pop('email')
        elif 'id' in options:
            url = '/' + options.pop('id')
        else:
            raise ParamsInvalidError('Invalid values')

        return cls.get(url, **options)

    def flag(self, **attrs):
        return self.__class__.post('/%s/flag' % self['id'])
