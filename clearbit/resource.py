import requests
import clearbit

class Resource(dict):
    endpoint = ''

    @classmethod
    def get(cls, url, **options):
        params = {}

        for o in ['webhook_url', 'webhook_id', 'subscribe']:
            if o in options:
                params[o] = options[o]

        endpoint = cls.endpoint + url

        if 'stream' in options:
            endpoint = endpoint.replace('.', '-stream.', 1)

        key = options.get('key', clearbit.key)

        response = requests.get(endpoint, params=params, auth=(key, ''))

        if response.status_code == 200:
            return cls(response.json())
        if response.status_code == 202:
            return cls({ 'pending': True })
        elif response.status_code == requests.codes.not_found:
            return None
        else:
            response.raise_for_status()
