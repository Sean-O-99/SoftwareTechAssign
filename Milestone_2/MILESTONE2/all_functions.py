def clear_filters():
    return {
        'selected_nutrient': None,
        'min_value': "",
        'max_value': "",
        'level': None
    }

def apply_filters(selected_nutrient, min_value_str, max_value_str, level):
    try:
        min_value = float(min_value_str)
    except ValueError:
        min_value = None

    try:
        max_value = float(max_value_str)
    except ValueError:
        max_value = None

    return {
        'selected_nutrient': selected_nutrient,
        'min_value': min_value,
        'max_value': max_value,
        'level': level
    }