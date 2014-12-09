import sys
import unittest

if sys.version_info > (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from clearbit.resource import Resource

class TestResource(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_clearbit_key(self, requests):
        Resource.get('http://x.clearbit.com/test', key='mykey')
        requests.get.assert_called_with('http://x.clearbit.com/test', params={}, auth=('mykey', ''))

    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Resource.get('http://x.clearbit.com/test', webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('http://x.clearbit.com/test', params={'webhook_url': 'http://webhook.com/webhook'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Resource.get('http://x.clearbit.com/test', webhook_id='myid')
        requests.get.assert_called_with('http://x.clearbit.com/test', params={'webhook_id': 'myid'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Resource.get('http://x.clearbit.com/test', subscribe=True)
        requests.get.assert_called_with('http://x.clearbit.com/test', params={'subscribe': True}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_stream(self, requests):
        Resource.get('http://x.clearbit.com/test', stream=True)
        requests.get.assert_called_with('http://x-stream.clearbit.com/test', params={}, auth=(None, ''))
