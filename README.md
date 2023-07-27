# discrete helpers

This is an example project, standing in for something like a math library.<br>
The classes and functions defined here should be imported in other projects, for which [discrete_research](https://github.com/entenschule/discrete_research) stands in.


## installation

``` 
me@my:~/learn_py/discrete_helpers$ sudo apt install python3.8-venv
me@my:~/learn_py/discrete_helpers$ python3 -m venv env
me@my:~/learn_py/discrete_helpers$ source env/bin/activate
(env) me@my:~/learn_py/discrete_helpers$ 
```

Select `env/bin/python` as Python interpreter for the project.

```
(env) me@my:~/learn_py/discrete_helpers$ pip install -r requirements.txt
```


# attempt to make library

`python setup.py sdist` has created the folders _dist_ and _discretehelpers.egg-info_.<br>
The former contains _discretehelpers-0.0.1.tar.gz_ and the latter contains metadata.<br>
(Both folders are git-ignored.)

The path to this library is now part of `sys.path` &mdash; also in [discrete_research](https://github.com/entenschule/discrete_research).<br>

```python
from sys import path


assert '/home/tilman/learn_py/discrete_research' in path
```
