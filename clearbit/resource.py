import requests
import clearbit

class Resource(dict):
    endpoint = ''
    options  = {}
    valid_options = ['params', 'key', 'headers', 'stream']

    @classmethod
    def set_version(cls, value):
        cls.options['headers'] = {'API-Version': value}

    @classmethod
    def new(cls, item, response=None):
        instance_s = None
        if isinstance(item, list):
            instance_s = (cls(rec) for rec in item)
            for instance in instance_s:
                instance['response'] = response

        else:
            instance_s = cls(item)
            instance_s['response'] = response

        return instance_s

    @classmethod
    def extract_options(cls, values):
        options = {k: v for k, v in values.items() if k in cls.valid_options}
        options.update(cls.options)

        params  = {k: v for k, v in values.items() if k not in cls.valid_options}
        options.setdefault('params', {}).update(params)

        key = options.pop('key', clearbit.key)
        options['auth'] = key, ''

        return options

    @classmethod
    def get(cls, url, **values):
        options = cls.extract_options(values)

        endpoint = cls.endpoint + url

        if options.pop('stream', False):
            endpoint = endpoint.replace('.', '-stream.', 1)

        response = requests.get(endpoint, **options)

        instance = None

        if response.status_code == 200:
            instance = cls.new(response.json())
        if response.status_code == 202:
            instance = cls({ 'pending': True })
        elif response.status_code == requests.codes.not_found:
            instance = None
        else:
            response.raise_for_status()

        if instance:
            instance['response'] = response

        return instance


    @classmethod
    def post(cls, url, **values):
        options = cls.extract_options(values)
        endpoint = cls.endpoint + url

        # Always post as a JSON object
        options['json'] = options.pop('params', {})

        response = requests.post(endpoint, **options)
        response.raise_for_status()

        return response

    @classmethod
    def delete(cls, url, **values):
        options = cls.extract_options(values)
        endpoint = cls.endpoint + url

        response = requests.delete(endpoint, **options)
        response.raise_for_status()

        return response
