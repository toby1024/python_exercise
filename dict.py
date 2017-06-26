#!/usr/bin/env python3

import random

def person(name, age, **kw):
    kw['a'] = 456
    print('name:', name, 'age:', age, 'other:', kw)

map = {'a': 1, 'b': 2}
person('Bob',20, **map)
print(map)

