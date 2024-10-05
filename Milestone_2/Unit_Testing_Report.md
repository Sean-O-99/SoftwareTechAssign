# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions** | **Test Functions**                                     |
|----------------------|--------------------------------------------------------|
| `...`                | `...` <br> `...`                                       |
| `...`                | `...` <br> `...`                                       |
| `clear_filters()`    | `test_clear_filters_valid()`                           |
| `apply_filters()`    | `apply_filters_valid()` <br> `apply_filters_invalid()` |
| `...`                | `...`                                                  |
| `...`                | `...`                                                  |
---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```
### Test Case 2:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 3:
- **Test Function/Module**
  - `test_clear_filters_valid()`
- **Tested Function/Module**
  - `clear_filters()`
- **Description**
  - `clear_filters()` is responsible for resetting the filters, clearing the values that have been initially set by users. It ensures all text fields and radio buttons are reset. The function doesn't take input parameters and output should reflect all filter values cleared or set to their default states.
- **1) Valid Input and Expected Output**  

| **Valid Input**                         | **Expected Output**                                                                      |
|-----------------------------------------|------------------------------------------------------------------------------------------|
| None (Function doesn't take parameters) | Filters reset: selected nutrient: `None`, min_value: `""`, max_value: `""`, level: `None` |

- **1) Code for the Test Function**
```python
def test_clear_filters_valid():
    filters = clear_filters()
    assert filters['selected_nutrient'] is None
    assert filters['min_value'] == ""
    assert filters['max_value'] == ""
    assert filters['level'] is None
```
- **2) Invalid Input and Expected Output**

Not applicable for `clear_filters()`, as it doesn't take any input.

### Test Case 4:
- **Test Function/Module**
  - `test_apply_filters_valid()`
  - `test_apply_filters_invalid()`
- **Tested Function/Module**
  - `apply_filters(selected_nutrient, min_value_str, max_value_str, level)`
- **Description**
  - `apply_filters()` is responsible for applying the filter logic based on user input for nutrient type, minimum value, maximum value, and nutrient level (low, medium, or high). It validates and converts the input, handling invalid cases like non-numeric inputs.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                      | **Expected Output**                                          |
|------------------------------------------------------|--------------------------------------------------------------|
| `apply_filters("Caloric Value", "50", "100", "Low")` | Nutrient: `"Caloric Value"`, Min: `50.0`, Max: `100.0`, Level: `"Low"` |


- **1) Code for the Test Function**
```python
def test_apply_filters_valid():
    filters = apply_filters(selected_nutrient= "Caloric Value", min_value_str="50", max_value_str="100", level="Low")
    assert filters['selected_nutrient'] == "Caloric Value"
    assert filters['min_value'] == 50.0
    assert filters['max_value'] == 100.0
    assert filters['level'] == "Low"
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                          | **Expected Output**                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------|
| `apply_filters("Caloric Value", "invalid", "100", "Low")`  | Selected Nutrient: `"Caloric Value"`, Min: `None`, Max: `100.0`, Level: `"Low"` |
| `apply_filters("Caloric Value", "50", "invalid", "Medium"` | Selected Nutrient: `"Caloric Value"`, Min:`50`, Max: `None`, Level: `"Medium"`  |
| `apply_filters("", "50", "100", "High"`                    | Selected Nutrient: `""`, Min:`50`, Max: `100`, Level: `"High"`                  |
| `apply_filters("Protein", "30", "70", None`)               | Selected Nutrient: `"Protein"`, Min:`30`, Max: `70`, Level: `None`              |

- **2) Code for the Test Function**
```python
def test_apply_filters_invalid():
    # Test invalid min_value
  filters = apply_filters("Caloric Value", "invalid", "100", "Low")
    assert filters['selected_nutrient'] == "Caloric Value"
    assert filters['min_value'] is None
    assert filters['max_value'] == 100.0
    assert filters['level'] == "Low"

    # Test invalid max_value
    filters = apply_filters("Caloric Value", "50", "invalid", "Medium")
    assert filters['selected_nutrient'] == "Caloric Value"
    assert filters['min_value'] == 50.0
    assert filters['max_value'] is None
    assert filters['level'] == "Medium"

    # Test invalid nutrient
    filters = apply_filters("", "50", "100", "High")
    assert filters['selected_nutrient'] == ""
    assert filters['min_value'] == 50.0
    assert filters['max_value'] == 100.0
    assert filters['level'] == "High"

    # Test no level selected
    filters = apply_filters("Protein", "30", "70", None)
    assert filters['selected_nutrient'] == "Protein"
    assert filters['min_value'] == 30.0
    assert filters['max_value'] == 70.0
    assert filters['level'] is None
```


### Test Case 5:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:

add more test cases if necessary.

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
