import sys
import unittest

if sys.version_info > (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from clearbit import *

class TestResource(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_clearbit_key(self, requests):
        Resource.get('http://x.clearbit.com/test', key='mykey')
        requests.get.assert_called_with('http://x.clearbit.com/test', params={}, auth=('mykey', ''))

    @patch('clearbit.resource.requests')
    def test_stream(self, requests):
        Resource.get('http://x.clearbit.com/test', stream=True)
        requests.get.assert_called_with('http://x-stream.clearbit.com/test', params={}, auth=(None, ''))

class TestPerson(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Person.find(id='123',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'webhook_url': 'http://webhook.com/webhook'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Person.find(id='123',webhook_id='myid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'webhook_id': 'myid'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Person.find(id='123',subscribe=True)
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/123', params={'subscribe': True}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        Person.find(email='user@example.com')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/email/user@example.com', params={}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_find_by_id(self, requests):
        Person.find(id='theid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/people/theid', params={}, auth=(None, ''))

class TestCompany(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        Company.find(id='123',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'webhook_url': 'http://webhook.com/webhook'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        Company.find(id='123',webhook_id='myid')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'webhook_id': 'myid'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        Company.find(id='123',subscribe=True)
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/123', params={'subscribe': True}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        Company.find(domain='example.com')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/domain/example.com', params={}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_find_by_id(self, requests):
        Company.find(id='theid')
        requests.get.assert_called_with('https://company.clearbit.com/v1/companies/theid', params={}, auth=(None, ''))

class TestPersonCompany(unittest.TestCase):
    @patch('clearbit.resource.requests')
    def test_webhook_url(self, requests):
        PersonCompany.find(email='user@example.com',webhook_url='http://webhook.com/webhook')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'webhook_url': 'http://webhook.com/webhook'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_webhook_id(self, requests):
        PersonCompany.find(email='user@example.com',webhook_id='myid')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'webhook_id': 'myid'}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_subscribe(self, requests):
        PersonCompany.find(email='user@example.com',subscribe=True)
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={'subscribe': True}, auth=(None, ''))

    @patch('clearbit.resource.requests')
    def test_endpoint(self, requests):
        PersonCompany.find(email='user@example.com')
        requests.get.assert_called_with('https://person.clearbit.com/v1/combined/email/user@example.com', params={}, auth=(None, ''))
