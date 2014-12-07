from clearbit.resource import Resource

class Company(Resource):
    @classmethod
    def find(cls, **params):
        url = 'https://company.clearbit.com/v1/company'

        if 'domain' in params:
            url += '/domain/' + params['domain']
        elif 'id' in params:
            url += params['id']
        else:
            raise ParamsInvalidError('Invalid values')

        return cls(Resource.get(url))
