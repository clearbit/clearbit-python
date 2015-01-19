from clearbit.resource import Resource

class Watchlist(Resource):
    endpoint = 'https://watchlist.clearbit.com/v1'

    @classmethod
    def search(cls, **options):
        if 'path' in options:
            path = options['path']
            del options['path']
        else:
            path = '/search/all'

        options.setdefault('params', {})

        for o in ['name', 'list', 'fuzzy']:
            if o in options:
                options['params'][o] = options[o]

        response = cls.post(path, **options)

        return(cls(item) for item in response.json())

class Individual(Watchlist):
    @classmethod
    def search(cls, **options):
        return super(Individual, cls).search(path='/search/individuals', **options)

class Entity(Watchlist):
    @classmethod
    def search(cls, **options):
        return super(Entity, cls).search(path='/search/entities', **options)
