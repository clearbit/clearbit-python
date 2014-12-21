from clearbit.resource import Resource
from clearbit.error import (ParamsInvalidError)

class PersonCompany(Resource):
    endpoint = 'https://person.clearbit.com/v1/combined'

    @classmethod
    def find(cls, **options):
        if 'email' in options:
            url = '/email/' + options['email']
        else:
            raise ParamsInvalidError('Invalid values')

        options.setdefault('params', {})

        for o in ['webhook_url', 'webhook_id', 'subscribe']:
            if o in options:
                options['params'][o] = options[o]

        return cls.get(url, **options)
