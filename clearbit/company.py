from clearbit.resource import Resource

class Company(Resource):
    endpoint = 'https://company.clearbit.com/v1/companies'

    @classmethod
    def find(cls, **params):
        if 'domain' in params:
            url = '/domain/' + params['domain']
        elif 'id' in params:
            url = '/' + params['id']
        else:
            raise ParamsInvalidError('Invalid values')

        return cls.get(url)
