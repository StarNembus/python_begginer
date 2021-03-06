# -*- coding: UTF-8 -*-
from sys import argv
from utils import currency_rates


script, course = argv
print(currency_rates(course))
