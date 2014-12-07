from clearbit.resource import Resource

class PersonCompany(Resource):
    @classmethod
    def find(cls, **params):
        url = 'https://person.clearbit.com/v1/combined'

        if 'email' in params:
            url += '/email/' + params['email']
        else:
            raise ParamsInvalidError('Invalid values')

        return cls(Resource.get(url))
