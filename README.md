# pre-commit-setup
----------------------------------------------------------------
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

After cloning the repo in your machine, load the conda environment
```shell
conda create --name my-env python=3.9 --file=environment.yml
```

activate conda environment
```shell
conda activate my-env
```

Install the git hook scripts
```shell
pre-commit install
```

Create a python file called `example_file.py` containing the following code:
```python
x = {  'a':37,'b':42,
'c':True}
if x['c'] is not None and \
 x['a'] > 0 or \
 x['b']  <= 214           :
 z = 'hello '+'world'
else:
 world = 'world'
 a = 'hello {}'.format(world)
 f = rf'hello {world}'
class Foo  (     object  ):
  def f    (self   ):
    return       37*-2
  def g(self, x,y=42):
      return y
# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5,
    6,  7,  8,
]
```

commit your work

```shell
git add .
git commit -m "Hello pre-commit"
```

Pre-commit will run all the hooks defined in `.pre-commit-config.yaml`.
Once pre-commit will perform all the checks, you should see in your terminal something like this

```python
# -*- coding: utf-8 -*-
x = {"a": 37, "b": 42, "c": True}
if x["c"] is not None and x["a"] > 0 or x["b"] <= 214:
    z = "hello " + "world"
else:
    world = "world"
    a = "hello {}".format(world)
    f = rf"hello {world}"


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


custom_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]
```

Commit the new changes:

```shell
git add .
git commit -m "[pre-commit] Hello pre-commit"
```

This time all the tests are passed and you can finally push your changes on github.

For more information about pre-commit check the [documentation](https://pre-commit.com).
