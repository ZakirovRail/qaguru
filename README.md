# qaguru
Repo for the online course QA GURU

# Create a new virtual env and activate:
$ pip install virtualenv
$ virtualenv qaguru_env
$ source qaguru_env/bin/activate
$ pip install -r requirements.txt
$ deactivate


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

Run tests (with printing):
- $ pytest tests/tests_web_ui.py -s


# Linter flake8
To install flake8:
- $ python -m pip install flake8

You can run lint checker for your python code using flake8 tool:
- $ flake8






# Install Allure as a test report
Documentation - https://docs.qameta.io/allure-report/#_installing_a_commandline

Github repository - 
1. Install on a Mac:
$ brew install allure
2. Add the allure-pytest into requirememts.txt file and install it in your venv
3. Add the directory with test results to .gitignore file
4. Run pytest with command $ --alluredir=allure-results, e.x.
$ pytest --alluredir=allure-results
5. Run command 
$ allure serve allure-results


# Hints
For debug in Firefox:
To make a freeze: 
$ setTimeout(function() {debugger;}, 3000);


# To avoid problems with import it's usefull to run in shell: 
$ export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"



# Arenadata repositories with different examples of hooks