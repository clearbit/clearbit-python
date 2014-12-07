import os

from clearbit.error import (ClearbitError, ParamsInvalidError)
from clearbit.person import Person
from clearbit.company import Company
from clearbit.person_company import PersonCompany

api_key = os.getenv('CLEARBIT_KEY', None)
