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


def is_even(integer):
    return integer % 2 == 0


def is_odd(integer):
    return not is_even(integer)


def factorial(integer):
    if integer < 0:
        raise ValueError("Factorial is undefined for a negative number")
    return 1 if integer <= 1 else integer * factorial(integer - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("Cannot return negatively indexed elements")
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(n):
    if n < 0:
        raise ValueError("At least one element must be returned")
    if n == 0:
        return
    f1 = 1
    f2 = 1
    x = 0
    for i in range(0, n):
        x = f1
        f1 = f2
        f2 = x + f1
        yield x
