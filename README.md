# Clearbit

A Python API client to [https://clearbit.com](https://clearbit.com).

## Usage

First authorize requests by setting the API key found on your [account's settings page](https://clearbit.com/keys).

    import clearbit
    import clearbit.streaming

    clearbit.api_key = 'mykey'

You can also set the API key via the CLEARBIT_KEY environment variable.

Then you can lookup people by email address:

    person = clearbit.streaming.Person.find(email='info@eribium.org')

If the person can't be found, then `None` will be returned.

See the [documentation](https://clearbit.com/docs#person-api) for more information.

## Company lookup

You can lookup company data by domain name:

    company = clearbit.streaming.Company(domain='uber.com')

If the company can't be found, then `None` will be returned.

See the [documentation](https://clearbit.com/docs#company-api) for more information.
