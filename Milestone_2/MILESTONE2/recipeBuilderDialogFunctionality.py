import wx.grid
import wx

from recipeBuilderDialog import RecipeBuilder
from setAmountDialogFunctionality import SetAmount

class Recipe(RecipeBuilder):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_recipe_name = ''
        self.current_recipe_items = []
        self.right_click_row = None
        self.right_click_col = None


    def insert_data_into_grid(self):
        if self.current_recipe_items:
            self.recipebuilder_added_items_list.ClearGrid()

            for row_index, item in enumerate(self.current_recipe_items):
                for col_index, column_name in enumerate(item.keys()):
                    self.recipebuilder_added_items_list.SetCellValue(row_index, col_index, str(item[column_name]))

    def setup_grid(self):
        # populate the list with the column names
        if self.current_recipe_items:
            column_names = list(self.current_recipe_items[0].keys())
            self.recipebuilder_added_items_list.ClearGrid()

            if self.recipebuilder_added_items_list.GetNumberRows() < len(self.current_recipe_items):
                self.recipebuilder_added_items_list.AppendRows(len(self.current_recipe_items) - self.recipebuilder_added_items_list.GetNumberRows())

            self.recipebuilder_added_items_list.SetColLabelValue(0, column_names[0])
            for index, column_name in enumerate(column_names):
                self.recipebuilder_added_items_list.SetColLabelValue(index, column_name)

            self.recipebuilder_added_items_list.AutoSizeColumns()

        else:
            print("No items available")

    def recipebuilder_save( self, event ):
        self.current_recipe_name = self.recipebuilder_name.GetValue()
        self.EndModal(wx.ID_OK)

    def recipebuilder_delete( self, event ):
        self.current_recipe_name = ''
        self.current_recipe_items = []
        self.EndModal(wx.ID_OK)

    def open_cell_menu( self, event ):
        self.right_click_row = event.GetRow()
        self.right_click_col = event.GetCol()
        self.PopupMenu(self.recipebuilder_popup_menu, event.GetPosition())

    def change_amount( self, event ):
        if self.right_click_row is not None and self.right_click_row < len(self.current_recipe_items):
            amount = self.current_recipe_items[self.right_click_row]['Amount']

            change_amount_dialog = SetAmount(self)
            change_amount_dialog.current_amount = amount

            if change_amount_dialog.ShowModal() == wx.ID_OK:
                new_amount = change_amount_dialog.set_amount_value.GetValue()

                if new_amount:
                    self.current_recipe_items[self.right_click_row]['Amount'] = new_amount
                    self.recipebuilder_added_items_list.SetCellValue(self.right_click_row, 1, new_amount)
                    self.update_recipe_nutrients()

                else:
                    wx.MessageBox("Valid amount not found.", "Error", wx.OK | wx.ICON_ERROR)
            change_amount_dialog.Destroy()

    def remove_item( self, event ):
        if self.right_click_row >= 0:
            self.recipebuilder_added_items_list.DeleteRows(self.right_click_row, 1)
            del self.current_recipe_items[self.right_click_row]
            self.update_recipe_nutrients()

    def RecipeBuilderOnContextMenu( self, event ):
        self.PopupMenu( self.recipebuilder_popup_menu, event.GetPosition() )

    def calculate_nutritional_totals(self):
        nutrient_totals = {f"nutrient_{i}": 0.0 for i in range(34)}

        num_rows = self.recipebuilder_added_items_list.GetNumberRows()
        for row in range(num_rows):
            amount_value = float(self.recipebuilder_added_items_list.GetCellValue((row, 1)))

            for col in range(2, 34):
                nutrient_value = float(self.recipebuilder_added_items_list.GetCellValue(row, col))
                nutrient_key = f"nutrient_{col - 2}"
                nutrient_totals[nutrient_key] += nutrient_value * amount_value

        return nutrient_totals

    def update_nutrient_totals(self, totals):
        self.caloric_value_total.SetLabel(f"{totals['nutrient_0']:.2f}")
        self.carbs_total.SetLabel(f"{totals['nutrient_5']:.2f}")
        self.protein_total.SetLabel(f"{totals['nutrient_7']:.2f}")
        self.sugars_total.SetLabel(f"{totals['nutrient_6']:.2f}")
        self.fiber_total.SetLabel(f"{totals['nutrient_8']:.2f}")
        self.cholesterol_total.SetLabel(f"{totals['nutrient_9']:.2f}")
        self.fats_sat_total.SetLabel(f"{totals['nutrient_2']:.2f}")
        self.fats_mono_total.SetLabel(f"{totals['nutrient_3']:.2f}")
        self.fats_poly_total.SetLabel(f"{totals['nutrient_4']:.2f}")
        self.A_total.SetLabel(f"{totals['nutrient_12']:.2f}")
        self.B_total.SetLabel(f"{totals['nutrient_13']:.2f}")
        self.b_11_total.SetLabel(f"{totals['nutrient_14']:.2f}")
        self.b_12_total.SetLabel(f"{totals['nutrient_15']:.2f}")
        self.b_2_total.SetLabel(f"{totals['nutrient_16']:.2f}")
        self.b_3_total.SetLabel(f"{totals['nutrient_17']:.2f}")
        self.b_5_total.SetLabel(f"{totals['nutrient_18']:.2f}")
        self.b_6_total.SetLabel(f"{totals['nutrient_19']:.2f}")
        self.c_total.SetLabel(f"{totals['nutrient_20']:.2f}")
        self.D_total.SetLabel(f"{totals['nutrient_21']:.2f}")
        self.E_total.SetLabel(f"{totals['nutrient_22']:.2f}")
        self.K_total.SetLabel(f"{totals['nutrient_23']:.2f}")
        self.calcium_total.SetLabel(f"{totals['nutrient_24']:.2f}")
        self.copper_total.SetLabel(f"{totals['nutrient_25']:.2f}")
        self.iron_total.SetLabel(f"{totals['nutrient_26']:.2f}")
        self.magnesium_total.SetLabel(f"{totals['nutrient_27']:.2f}")
        self.manganese_total.SetLabel(f"{totals['nutrient_28']:.2f}")
        self.phosphorus_total.SetLabel(f"{totals['nutrient_29']:.2f}")
        self.potassium_total.SetLabel(f"{totals['nutrient_30']:.2f}")
        self.selenium_total.SetLabel(f"{totals['nutrient_31']:.2f}")
        self.zinc_total.SetLabel(f"{totals['nutrient_32']:.2f}")
        self.water_total.SetLabel(f"{totals['nutrient_11']:.2f}")
        self.fats_total.SetLabel(f"{totals['nutrient_1']:.2f}")
        self.sodium_label.SetLabel(f"{totals['nutrient_10']:.2f}")

    def update_recipe_nutrients(self):
        totals = self.calculate_nutritional_totals()
        self.update_nutrient_totals(totals)

