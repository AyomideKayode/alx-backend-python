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

1. Basic annotations - concat | [1-concat.py](./1-concat.py)

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

| Task | File |
| ---- | ---- |
| 2. Basic annotations - floor | [2-floor.py](./2-floor.py) |
| 3. Basic annotations - to string | [3-to_str.py](./3-to_str.py) |
| 4. Define variables | [4-define_variables.py](./4-define_variables.py) |
| 5. Complex types - list of floats | [5-sum_list.py](./5-sum_list.py) |
| 6. Complex types - mixed list | [6-sum_mixed_list.py](./6-sum_mixed_list.py) |
| 7. Complex types - string and int/float to tuple | [7-to_kv.py](./7-to_kv.py) |
| 8. Complex types - functions | [8-make_multiplier.py](./8-make_multiplier.py) |
| 9. Let's duck type an iterable object | [9-element_length.py](./9-element_length.py) |
