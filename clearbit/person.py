from clearbit.resource import Resource
from clearbit.error import (ParamsInvalidError)

class Person(Resource):
    endpoint = 'https://person.clearbit.com/v1/people'

    @classmethod
    def find(cls, **options):
        if 'email' in options:
            url = '/email/' + options['email']
        elif 'twitter' in options:
            url = '/twitter/' + options['twitter']
        elif 'github' in options:
            url = '/github/' + options['github']
        elif 'id' in options:
            url = '/' + options['id']
        else:
            raise ParamsInvalidError('Invalid values')

        options.setdefault('params', {})

        for o in ['webhook_url', 'webhook_id', 'subscribe']:
            if o in options:
                options['params'][o] = options[o]

        return cls.get(url, **options)

    def flag(self, **attrs):
        return self.__class__.post('/%s/flag' % self['id'])
