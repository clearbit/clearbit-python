import requests
import logging
import clearbit

logging.basicConfig(level=logging.DEBUG)

class Resource(dict):
    @classmethod
    def get(cls, url, **options):
        params = {}

        for o in ['webook_url', 'webhook_id', 'subscribe']:
            if o in options:
                params[o] = options[o]

        response = requests.get(url, params=params, auth=(clearbit.api_key, ''))

        if response.status_code == 200:
            return response.json()
        if response.status_code == 202:
            return { 'pending': True }
        elif response.status_code == requests.codes.not_found:
            return None
        else:
            response.raise_for_status()
