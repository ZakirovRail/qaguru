# qaguru
Repo for the online course QA GURU

# Create a new virtual env and activate:
$ pip install virtualenv
$ virtualenv qaguru_env
$ source qaguru_env/bin/activate

# deactivate virtual env
$ deactivate

# Usefule link about venv
https://sourabhbajaj.com/mac-setup/Python/virtualenv.html


# Install selene:
$ pip install selene

# Install all libraries from requirements.txt
$ pip install -r requirements.txt

# Export libraries from virtual env to requirements.txt file
$ pip freeze -> requirements.txt 




# Using Pytest
If you want to check which fixtures are run before and after tests, need to run --setup-plan
- $ pytest --setup-plan <test_file_name>

Run tests:
- $ pytest tests/tests_web_ui.py -s


# Linter flake8
You can run lint checker for your python code using flake8 tool:
- $ flake8