import re

import pandas as pd


def on_search(df, input_string):
    keyword = input_string.lower()
    search_food = df["food"]
    index = []

    for food in search_food:
        if re.search(keyword, food):
            index.append(True)
        else:
            index.append(False)
    return df[index]

def on_cell_click(df, food_item):
    df_row = df[df["food"] == food_item]

    nutritional_info = df_row.iloc[0].to_dict()
    nutritional_values = {key: value for key, value in nutritional_info.items() if key != "food"}

    nutritional_items = list(nutritional_values.items())
    fat = nutritional_items[0]
    carbs = nutritional_items[1]
    protein = nutritional_items[2]
    vitamin_a = nutritional_items[3]
    vitamin_b6 = nutritional_items[4]
    vitamin_c = nutritional_items[5]
    vitamin_d = nutritional_items[6]
    calcium = nutritional_items[7]
    iron = nutritional_items[8]
    magnesium = nutritional_items[9]
    potassium = nutritional_items[10]
    zinc = nutritional_items[11]

    macronutrients = {
        fat[0]: fat[1],
        carbs[0]: carbs[1],
        protein[0]: protein[1]
    }

    micronutrients = {
        vitamin_a[0]: vitamin_a[1],
        vitamin_b6[0]: vitamin_b6[1],
        vitamin_c[0]: vitamin_c[1],
        vitamin_d[0]: vitamin_d[1],
        calcium[0]: calcium[1],
        iron[0]: iron[1],
        magnesium[0]: magnesium[1],
        potassium[0]: potassium[1],
        zinc[0]: zinc[1],
    }

    return macronutrients, micronutrients

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