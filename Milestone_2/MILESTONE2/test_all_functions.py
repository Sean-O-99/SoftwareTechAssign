import pytest
from all_functions import clear_filters, apply_filters

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
    filters = apply_filters("Caloric Value", "invalid", "100", "Low")
    assert filters['min_value'] is None
    assert filters['max_value'] == 100.0

    # Test invalid max_value (should handle gracefully)
    filters = apply_filters("Caloric Value", "50", "invalid", "Medium")
    assert filters['min_value'] == 50.0
    assert filters['max_value'] is None

    # Test invalid nutrient (empty string)
    filters = apply_filters("", "50", "100", "High")
    assert filters['selected_nutrient'] == ""
    assert filters['min_value'] == 50.0
    assert filters['max_value'] == 100.0
    assert filters['level'] == "High"

    # Test no level selected (None)
    filters = apply_filters("Protein", "30", "70", None)
    assert filters['selected_nutrient'] == "Protein"
    assert filters['min_value'] == 30.0
    assert filters['max_value'] == 70.0
    assert filters['level'] is None