import wx
import wx.grid
import pandas as pd
import re

from matplotlib import pyplot as plt
from wx.lib.agw.aui import right
from wx.lib.masked import value

from mainPage import MyFrame2 as MyFrame2
from breakdownDialogFunctionality import NutritionalDialog
from filterDialogFunctionality import FilterDialog
from createRecipeDialogFunctionality import NameRecipeDialog

class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        return attr

class FoodDataTable(MyFrame2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.df = pd.read_csv("./Food_Nutrition_Dataset.csv")
        self.filtered_df = None
        self.table = DataTable(self.df)
        self.current_recipe_name = ''
        self.current_recipe_items = []
        self.current_recipe_value.SetLabel(self.current_recipe_name)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.clicked_row = None
        self.Show(True)
        self.Layout()



    def on_search(self, event):
        event.Skip()
        keywordValue = self.m_textCtrl1.GetValue()
        keyword = keywordValue.lower()
        searchFood = self.df["food"]
        index = []

        for food in searchFood:
            if re.search(keyword, food):
                index.append(True)
            else:
                index.append(False)
        dfFiltered = self.df[index]
        self.m_grid1.ClearGrid()
        self.table = DataTable(dfFiltered)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()

    def on_cell_click(self, event):
        row = event.GetRow()
        food_item = self.m_grid1.GetCellValue(row, 0)
        df_row = self.df[self.df["food"] == food_item]
        nutritional_info = df_row.iloc[0].to_dict()
        nutritional_values = {key: value for key, value in nutritional_info.items() if key !="food"}

        nutritional_items = list(nutritional_values.items())
        fat = nutritional_items[1]
        carbs = nutritional_items[5]
        protein = nutritional_items[7]
        vitamin_a = nutritional_items[12]
        vitamin_b6 = nutritional_items[19]
        vitamin_b12 = nutritional_items[15]
        vitamin_c = nutritional_items[20]
        vitamin_d = nutritional_items[21]
        calcium = nutritional_items[24]
        iron = nutritional_items[26]
        magnesium = nutritional_items[27]
        potassium = nutritional_items[30]
        zinc = nutritional_items[32]

        macronutrients = {
            fat[0] : fat[1],
            carbs[0] : carbs[1],
            protein[0] : protein[1]
        }

        micronutrients = {
            vitamin_a[0]: vitamin_a[1],
            vitamin_b6[0]: vitamin_b6[1],
            vitamin_b12[0]: vitamin_b12[1],
            vitamin_c[0]: vitamin_c[1],
            vitamin_d[0] : vitamin_d[1],
            calcium[0]: calcium[1],
            iron[0]: iron[1],
            magnesium[0]: magnesium[1],
            potassium[0]: potassium[1],
            zinc[0]: zinc[1],
        }

        macro_colors = ["red", "cyan", "yellow"]
        macro_categories = list(macronutrients.keys())
        macro_sizes = list(macronutrients.values())

        micro_colors = ["green", "orange", "purple", "brown", "pink", "gray", "olive", "cyan", "magenta", "teal",]
        micro_categories = list(micronutrients.keys())
        micro_sizes = list(micronutrients.values())

        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        ax1, ax2 = axes
        ax1.pie(macro_sizes, labels=macro_categories, shadow=True, autopct="%1.1f%%", colors=macro_colors)
        ax1.set_title("Macronutrients")

        plt.xticks(rotation=45, ha="right")
        ax2.bar(micro_categories, micro_sizes, color=micro_colors)
        ax2.set_title("Micronutrients")
        ax2.set_ylabel("Milligrams (mg)")
        ax2.set_xlabel("Type")

        plt.tight_layout()

        dialog = NutritionalDialog(None, food_item, fig,fat, carbs, protein)
        dialog.ShowModal()

        # return food_item, macronutrients

    def open_filter_dialog(self, event):
        dialog = FilterDialog(None)
        if dialog.ShowModal() == wx.ID_OK:
            selected_nutrient = dialog.selected_nutrient
            min_value = dialog.min_value
            max_value = dialog.max_value
            level = dialog.level

            filtered_df = self.apply_filters_to_dataframe(selected_nutrient, min_value, max_value, level)
            self.update_grid_with_filtered_data(filtered_df)

            applied_filters = dialog.filter_text
            self.m_staticText8.SetLabel(applied_filters)
        dialog.Destroy()

    def apply_filters_to_dataframe(self, nutrient, min_value, max_value, level):
        # Filter by selected nutrient column
        filtered_df = self.df

        # Apply minimum filter if provided
        if min_value is not None:
            filtered_df = filtered_df[filtered_df[nutrient] >= min_value]

        # Apply maximum filter if provided
        if max_value is not None:
            filtered_df = filtered_df[filtered_df[nutrient] <= max_value]

        # Apply level filter
        highest_value = self.df[nutrient].max()
        if level == "Low":
            threshold = highest_value * 0.33
            filtered_df = filtered_df[filtered_df[nutrient] < threshold]  # Example threshold for low
        elif level == "Medium":
            lower_threshold = highest_value * 0.33
            upper_threshold = highest_value * 0.66
            filtered_df = filtered_df[(filtered_df[nutrient] >= lower_threshold) & (filtered_df[nutrient] < upper_threshold)]
        elif level == "High":
            threshold = highest_value * 0.66
            filtered_df = filtered_df[filtered_df[nutrient] >= threshold]

        self.filtered_df = filtered_df
        return filtered_df

    def update_grid_with_filtered_data(self, filtered_df):
        self.table = DataTable(filtered_df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Layout()

    def create_recipe(self, event):
        dialog = NameRecipeDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            recipe_name = dialog.createrecipe_name_field.GetValue()
            self.current_recipe_name = recipe_name
            self.current_recipe_value.SetLabel(self.current_recipe_name)
            # ensure the list is clear
            self.current_recipe_items = []
        dialog.Destroy()

    def add_item_to_recipe(self, event):
        if hasattr(self, 'clicked_row') and 0 <= self.clicked_row < self.m_grid1.GetNumberRows():
            row_index = self.clicked_row
            selected_df = self.filtered_df if self.filtered_df is not None else self.df
            food_item = selected_df.iloc[row_index]

            if any(item['food'] == food_item['food'] for item in self.current_recipe_items):
                wx.MessageBox(f"{food_item['food']} is already part of the current recipe.")
                return

            food_item['amount'] = 1

            #rearrange dictionary to prep for recipe
            food_item = {
                'food': food_item['food'],
                'amount': food_item['amount'],
                **{k: v for k, v in food_item.items() if k not in ['food', 'amount']}
            }
            self.current_recipe_items.append(food_item)

            print(food_item)
            wx.MessageBox("Added item to the recipe")
        else:
            wx.MessageBox("Invalid row selected.")
    def on_cell_right_click( self, event ):
        self.clicked_row = event.GetRow()
        print(self.clicked_row)
        self.PopupMenu(self.add_menu, event.GetPosition())

if __name__ == "__main__":
    app = wx.App()
    frame = FoodDataTable()
    app.MainLoop()
