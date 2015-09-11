import sys
import unittest

if sys.version_info > (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

import clearbit
from clearbit import *

clearbit.key = 'k'

class TestResource(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_clearbit_key(self, requests):
        Resource.get('http://x.clearbit.com/test', key='mykey')
        requests.get.assert_called_with('http://x.clearbit.com/test', params={}, auth=('mykey', ''))

    @patch('clearbit.resource.requests')
    def test_stream(self, requests):
        Resource.get('http://x.clearbit.com/test', stream=True)
        requests.get.assert_called_with('http://x-stream.clearbit.com/test', params={}, auth=('k', ''))

class TestPerson(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Person.find(id='123',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'webhook_url': 'http://webhook.com/webhook'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Person.find(id='123',webhook_id='myid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'webhook_id': 'myid'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Person.find(id='123',subscribe=True)
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'subscribe': True}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        Person.find(email='user@example.com')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/email/user@example.com', params={}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_find_by_id(self, requests):
        Person.find(id='theid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/theid', params={}, auth=('k', ''))

class TestCompany(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Company.find(id='123',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'webhook_url': 'http://webhook.com/webhook'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Company.find(id='123',webhook_id='myid')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'webhook_id': 'myid'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Company.find(id='123',subscribe=True)
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'subscribe': True}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        Company.find(domain='example.com')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/domain/example.com', params={}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_find_by_id(self, requests):
        Company.find(id='theid')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/theid', params={}, auth=('k', ''))

class TestEnrichment(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Enrichment.find(email='user@example.com',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'webhook_url': 'http://webhook.com/webhook'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Enrichment.find(email='user@example.com',webhook_id='myid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'webhook_id': 'myid'}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Enrichment.find(email='user@example.com',subscribe=True)
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'subscribe': True}, auth=('k', ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        Enrichment.find(email='user@example.com')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={}, auth=('k', ''))


if __name__ == '__main__':
        unittest.main()
