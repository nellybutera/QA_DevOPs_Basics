## QA & DevOps Practice Project

This is a **simple practice project** I created to strengthen my **QA and DevOps skills**. The goal was to learn how to write tests in Python and integrate them into a CI/CD workflow using GitHub Actions.  

### Project Overview

- A **basic calculator program** with two functions I wrote:  
  - **Addition** (`add`)  
  - **Subtraction** (`subtract`)  
- I created automated **tests using `pytest`** to make sure the calculator works correctly.  
- Added **CI/CD integration** with GitHub Actions, including generating a test report.

### How I Built & Tested It

1. **App code**: `calculator.py`  
   - Contains the calculator functions I implemented.  

2. **Tests**: `test_calculator.py`  
   - Contains test cases for each function.  
   - Tests are run using `pytest` to verify the functions behave as expected.

3. **Running tests locally**  
   From the project folder, I run:  

   ```bash
   python -m pytest -v 
   
   or simply:

   pytest -v

4. **Generating a test report**
   - I added a JUnit XML report for DevOps practice:

    ```bash
    python -m pytest -v --junitxml=report.xml


### Failing Test Example
- I intentionally added a failing test (test_failing_example) to see how pytest reports errors and how the workflow handles failures. This was a great learning experience on how CI/CD pipelines catch problems automatically.

###  CI/CD Integration
- I set up a GitHub Actions workflow in .github/workflows/python-tests.yml.
- It runs automatically on push or pull request.
- It also uploads the test report (report.xml) as an artifact for review.