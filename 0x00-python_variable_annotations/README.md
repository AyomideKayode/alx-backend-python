# Project: 0x00. Python - Variable Annotations

## Resources

### Read or watch:-

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Learning Objectives

### General

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Tasks

0. [Basic annotations - add](./0-add.py) :

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

1. [Basic annotations - concat](./1-concat.py) :

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string

```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
```

2. [Basic annotations - floor](./2-floor.py) :

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./2-main.py
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
```

3. [Basic annotations - to string](./3-to_str.py) :

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

```bash
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

bob@dylan:~$ ./3-main.py
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
```

| Task | File |
| ---- | ---- |
| 4. Define variables | [4-define_variables.py](./4-define_variables.py) |
| 5. Complex types - list of floats | [5-sum_list.py](./5-sum_list.py) |
| 6. Complex types - mixed list | [6-sum_mixed_list.py](./6-sum_mixed_list.py) |
| 7. Complex types - string and int/float to tuple | [7-to_kv.py](./7-to_kv.py) |
| 8. Complex types - functions | [8-make_multiplier.py](./8-make_multiplier.py) |
| 9. Let's duck type an iterable object | [9-element_length.py](./9-element_length.py) |
