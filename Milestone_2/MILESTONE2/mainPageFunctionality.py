import wx
import wx.grid
import pandas as pd
from wx.lib.agw.aui import right
from wx.lib.masked import value

from mainPage import MyFrame2 as MyFrame2
from breakdownDialogFunctionality import NutritionalDialog
from filterDialogFunctionality import FilterDialog
import matplotlib.pyplot as plt

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
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()

    def on_search(self, event):
        keyword = self.m_textCtrl1.GetValue().lower()
        if keyword:
            self.filtered_df = self.df[
                self.df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)
            ]
        else:
            self.filtered_df = self.df  # Reset if search is cleared

        self.table = DataTable(self.filtered_df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Layout()

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

        macro_categories = list(macronutrients.keys())
        macro_sizes = list(macronutrients.values())

        micro_categories = list(micronutrients.keys())
        micro_sizes = list(micronutrients.values())

        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        ax1, ax2 = axes
        ax1.pie(macro_sizes, labels=macro_categories, shadow=True, autopct="%1.1f%%")
        ax1.set_title("Macronutrients")

        plt.xticks(rotation=45, ha="right")
        ax2.bar(micro_categories, micro_sizes)
        ax2.set_title("Micronutrients")

        plt.tight_layout()

        dialog = NutritionalDialog(None, food_item, fig)
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

        return filtered_df

    def update_grid_with_filtered_data(self, filtered_df):
        self.table = DataTable(filtered_df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = FoodDataTable()
    app.MainLoop()
