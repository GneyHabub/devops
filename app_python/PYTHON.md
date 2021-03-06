### LIST OF THE BEST PRACTICES FOR A PYTHON APP:
1. The choice of the main framework - I picked Bottle. And that's why:
    * It is fast, simple and lightweight.
    * It easily allows using prod ready servers out of the box.
    * It is distributed as a single file module and has no dependencies other than the Python.
2. Unit testing your code is always a good practice. It lets you write more reliable code and thus sleep better at nights. I wrote a simple test for my app in `test_msctime.py` file.
3. Using `pytest` for running those tests automatically is also a good idea.
3. Linters help maintaining similar code style throughout the whole project. I used `pylint` and `autopep8` for fix some of the issues automatically.
4. `requirements.txt`. Requirements are the list of Python packages (dependencies) of your project that are used by the project while it runs. It includes the version for each package.