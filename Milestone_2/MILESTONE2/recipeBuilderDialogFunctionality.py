import wx.grid
import wx

from recipeBuilderDialog import RecipeBuilder

class Recipe(RecipeBuilder):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_recipe_name = ''
        self.current_recipe_items = []


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
            self.recipebuilder_added_items_list.AppendRows(len(self.current_recipe_items))

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

    def cell_menu( self, event ):
        event.Skip()

    def change_amount( self, event ):
        event.Skip()

    def remove_item( self, event ):
        event.Skip()

    def RecipeBuilderOnContextMenu( self, event ):
        self.PopupMenu( self.recipebuilder_popup_menu, event.GetPosition() )
