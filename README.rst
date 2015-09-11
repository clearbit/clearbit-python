# Clearbit

A Python API client to [https://clearbit.com](https://clearbit.com).

## Installation

To install the Clearbit Python bindings, run:

    pip install clearbit

Or

    easy_install clearbit

## Usage

First authorize requests by setting the API key found on your [account's settings page](https://clearbit.com/keys).

    import clearbit

    clearbit.key = 'mykey'

You can also set the API key via the CLEARBIT_KEY environment variable.

Then you can lookup people by email address. If the email's domain is corporate we'll also return a company response.

    response = clearbit.Enrichment.find(email='alex@clearbit.com',stream=True)

    person = response['person']
    print(person['name'])

See the [documentation](https://clearbit.com/docs#person-api) for more information.

## Company lookup

You can lookup company data by domain name:

    company = clearbit.Company(domain='uber.com',stream=True)

If the company can't be found, then `None` will be returned.

See the [documentation](https://clearbit.com/docs#company-api) for more information.

## Testing

Set the `PYTHONPATH` env var to the current directory to load the library locally:

    export PYTHONPATH=.
