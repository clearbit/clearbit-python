from clearbit.resource import Resource

class Person(Resource):
    @classmethod
    def find(cls, **params):
        url = 'https://person.clearbit.com/v1/people'

        if 'email' in params:
            url += '/email/' + params['email']
        elif 'twitter' in params:
            url += '/twitter/' + params['twitter']
        elif 'github' in params:
            url += '/github/' + params['github']
        elif 'id' in params:
            url += params['id']
        else:
            raise ParamsInvalidError('Invalid values')

        return cls(Resource.get(url))
