from django.test import TestCase

from capitalize import capitalize

assert capitalize("") == ""
assert capitalize("hello") == "Hello"
