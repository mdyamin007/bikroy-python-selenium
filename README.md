# Python Selenium Demo Project

### How to run

Create a virtual python environment:

> python -m venv .env

Activate the environment:

> source './.env/bin/activate'

Install all requirements from requirements.txt:

> pip install -r requirements.txt

Run using PyTest:

> pytest -v -s tests/test_cases.py

Run using Pytest with *Allure* report:

> pytest -v -s \-\-alluredir="Path of the directory" tests/test_cases.py 

Finally server allure report:

> allure serve [Path of the report directory]

