This is a simple QA and Devops Practice Project.

- It is a calculator program, with two basic functions: addition and substraction.

- After creating the calculator.py file and test_calculator.py. I wrote the functions and tests.

This is how i run them
- python -m pytest -v but you can do pytest -v for a simpler version.


After I added a failing test to see what it looked like and also added a report to help with my devops integration
- python -m pytest -v --junitxml=report.xml