# Coverage Testing Report

### GitHub Repository URL: https://github.com/Sean-O-99/SoftwareTechAssign.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

You should perform statement coverage testing and branch coverage testing. For each type, provide a description and an analysis explaining how you evaluated the coverage.

## 1. **Test Summary**
| **Tested Functions** | **Test Functions**                                           |
|----------------------|--------------------------------------------------------------|
| `on_search`          | `test_on_search_valid()` <br> `test_on_search_valid_empty()` |
| `on_cell_click`      | `test_on_cell_click_valid()`                                 |
| `clear_filters()`    | `test_clear_filters_valid()`                                 |
| `apply_filters()`    | `apply_filters_valid()` <br> `apply_filters_invalid()`       |
| `...`                | `...`                                                        |
| `...`                | `...`                                                        |

---

## 2. **Statement Coverage Test**

### 2.1 Description

Explain how you designed the test cases (i.e., test_all_functions.py) to reach 100% statement coverage.

### 2.2 Testing Results
You can use the following command to run the statement coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![statement_coverage](./statement_coverage.png)

## 3. **Branch Coverage Test**

### 3.1 Description

Explain how you designed the test cases (i.e., test_all_functions.py) to reach 100% branch coverage.

### 3.2 Testing Results
You can use the following command to run the branch coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-branch --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![statement_coverage](./branch_coverage.png)
