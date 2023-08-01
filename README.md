# discrete helpers

This is an example project, standing in for something like a math library.<br>
The classes and functions defined here should be imported in other projects, for which [discrete_research](https://github.com/entenschule/discrete_research) stands in.


## installation

``` 
me@my:~/learn_py/discrete_helpers$ sudo apt install python3.8-venv
me@my:~/learn_py/discrete_helpers$ python3 -m venv env
me@my:~/learn_py/discrete_helpers$ source env/bin/activate
(env) me@my:~/learn_py/discrete_helpers$ pip install -r requirements.txt
```


## create library

Tutorial: [How to create a Python library](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f) (medium.com)

``` 
pip install wheel
pip install setuptools
pip install twine
```

Create [_setup.py_](setup.py).

``` 
python setup.py bdist_wheel
```

Now the library can be installed using the path to the Wheel file.

```
pip install /home/tilman/learn_py/discrete_helpers/dist/discretehelpers-0.0.1-py3-none-any.whl
```

An effect of running _setup.py_ that seems rather pointless, is the creation of the `build` folder, which contains a copy of the whole project. But it can be safely deleted.
