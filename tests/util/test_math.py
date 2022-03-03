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

from src.util import math
from unittest import TestCase


class MathTest(TestCase):

    @classmethod
    def test_is_even(cls):
        even_number = 100
        odd_number = 3253
        assert math.is_even(even_number)
        assert not math.is_even(odd_number)

    @classmethod
    def test_is_odd(cls):
        even_number = 100
        odd_number = 3253
        assert math.is_odd(odd_number)
        assert not math.is_odd(even_number)

    @classmethod
    def test_factorial(cls):
        with cls.assertRaises(cls, ValueError):
            math.factorial(-1)
        assert math.factorial(0) == 1
        assert math.factorial(1) == 1
        assert math.factorial(2) == 2
        assert math.factorial(3) == 6
        assert math.factorial(4) == 24

    @classmethod
    def test_fibonacci(cls):
        with cls.assertRaises(cls, ValueError):
            math.fibonacci(-10)
        assert math.fibonacci(0) == 1
        assert math.fibonacci(1) == 1
        assert math.fibonacci(2) == 2
        assert math.fibonacci(3) == 3
        assert math.fibonacci(4) == 5
        assert math.fibonacci(5) == 8

    @classmethod
    def test_fibonacci_sequence(cls):
        with cls.assertRaises(cls, ValueError):
            list(math.fibonacci_sequence(-10))
        for test_size in (0, 10):
            result = list(math.fibonacci_sequence(test_size))
            assert test_size == len(result)
            for i in range(0, test_size):
                assert math.fibonacci(i) == result[i]
