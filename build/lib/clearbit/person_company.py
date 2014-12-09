from clearbit.resource import Resource

class PersonCompany(Resource):
    endpoint = 'https://person.clearbit.com/v1/combined'

    @classmethod
    def find(cls, **params):
        if 'email' in params:
            url = '/email/' + params['email']
        else:
            raise ParamsInvalidError('Invalid values')

        return cls.get(url)
