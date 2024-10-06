import pytest
import pandas as pd
from all_functions import on_search, clear_filters, apply_filters, on_cell_click

def test_on_search_valid():
    df = pd.DataFrame({"food": ["cheese pizza", "steak", "apple", "orange", "pepperoni pizza"],})
    filtered_df = on_search(df, "pizza")
    expected_food = ["cheese pizza", "pepperoni pizza"]
    actual_food = filtered_df["food"].to_list()
    assert actual_food == expected_food

def test_on_cell_click_valid():
    df = pd.DataFrame({
        "food": ["cheese pizza", "steak", "apple", "orange", "pepperoni pizza"],
        "fat": [25, 20, 1, 1, 30],
        "carbs": [40, 2, 20, 25, 41],
        "protein": [15, 35, 0.5, 0.2, 20],
        "vitamin_a": [5, 8, 61, 76, 5.5],
        "vitamin_b6": [0.1, 0.2, 1, 2, 0.3],
        "vitamin_c": [2, 1, 20, 31.5, 2.5],
        "vitamin_d": [0, 0, 0, 0, 0],
        "calcium": [11, 0, 0, 0, 7],
        "iron": [3, 13.3, 0.1, 0.2, 5.5],
        "magnesium": [0.2, 0.9, 7, 1, 0.5],
        "potassium": [50, 62, 99, 75, 58],
        "zinc": [0.05, 0.01, 0.07, 0.02, 0.03]
    })
    macronutrients, micronutrients = on_cell_click(df, "pepperoni pizza")
    assert macronutrients["fat"] == 30
    assert macronutrients["carbs"] == 41
    assert macronutrients["protein"] == 20

    assert micronutrients["vitamin_a"] == 5.5
    assert micronutrients["vitamin_b6"] == 0.3
    assert micronutrients["vitamin_c"] == 2.5
    assert micronutrients["vitamin_d"] == 0.0
    assert micronutrients["calcium"] == 7
    assert micronutrients["iron"] == 5.5
    assert micronutrients["magnesium"] == 0.5
    assert micronutrients["potassium"] == 58
    assert micronutrients["zinc"] == 0.03

def test_clear_filters_valid():
    filters = clear_filters()
    assert filters['selected_nutrient'] is None
    assert filters['min_value'] == ""
    assert filters['max_value'] == ""
    assert filters['level'] is None

def test_apply_filters_valid():
    filters = apply_filters(selected_nutrient= "Caloric Value", min_value_str="50", max_value_str="100", level="Low")
    assert filters['selected_nutrient'] == "Caloric Value"
    assert filters['min_value'] == 50.0
    assert filters['max_value'] == 100.0
    assert filters['level'] == "Low"


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

    filters = apply_filters("", "50", "100", "High")
    assert filters['selected_nutrient'] == ""
    assert filters['min_value'] == 50.0
    assert filters['max_value'] == 100.0
    assert filters['level'] == "High"

    filters = apply_filters("Protein", "30", "70", None)
    assert filters['selected_nutrient'] == "Protein"
    assert filters['min_value'] == 30.0
    assert filters['max_value'] == 70.0
    assert filters['level'] is None
