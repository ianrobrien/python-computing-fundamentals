# Copyright (c) 2018-present, Ian R. O'Brien
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

import json
import requests

api_currency_converter = 'https://free.currencyconverterapi.com/api/v6'


def get_quote(base, quote):
    b = base.upper()
    q = quote.upper()
    request_url = f'{api_currency_converter}/convert?q={b}_{q}&compact=ultra'
    response = requests.get(request_url).json()
    return response[f'{b}_{q}']
