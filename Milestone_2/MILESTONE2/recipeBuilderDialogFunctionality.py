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
        print(self.current_recipe_items)
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
                else:
                    wx.MessageBox("Valid amount not found.", "Error", wx.OK | wx.ICON_ERROR)
            change_amount_dialog.Destroy()

    def remove_item( self, event ):
        if self.right_click_row >= 0:
            self.recipebuilder_added_items_list.DeleteRows(self.right_click_row, 1)
            del self.current_recipe_items[self.right_click_row]

    def RecipeBuilderOnContextMenu( self, event ):
        self.PopupMenu( self.recipebuilder_popup_menu, event.GetPosition() )
