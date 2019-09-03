#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
import os
from shutil import copyfile

# chillin imports
from koala_serializer import generate


commands_reletive_path = 'ks/commands.ks'
models_reletive_path = 'ks/models.ks'
destinations = [
    '../PythonClient',
    '../CppClient/Game',
    '../JavaClient/src'
]

for dest in destinations:
    for rel_path in [commands_reletive_path, models_reletive_path]:
        path = os.path.join(dest, rel_path)
        if not os.path.exists(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        copyfile(rel_path, path)

all_args = [
    ('python', 'ks', 'snake_case'),
    ('python', '../PythonClient/ks', 'snake_case'),
    ('cpp', '../CppClient/Game/ks', 'camelCase'),
    ('java', '../JavaClient/src', 'camelCase')
]

for args in all_args:
    generate(commands_reletive_path, *args)
    generate(models_reletive_path, *args)
