from clearbit.resource import Resource
from clearbit.error import (ParamsInvalidError)

class Person(Resource):
    endpoint = 'https://person.clearbit.com/v2/people'

    @classmethod
    def find(cls, **options):
        if 'email' in options:
            url = '/find'
        else:
            raise ParamsInvalidError('Invalid values')

        return cls.get(url, **options)

    def flag(self, **attrs):
        return self.__class__.post('/%s/flag' % self['id'])
