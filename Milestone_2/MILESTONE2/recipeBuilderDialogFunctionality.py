import wx.grid
import wx

from recipeBuilderDialog import RecipeBuilder

class Recipe(RecipeBuilder):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_recipe_name = ''
        self.current_recipe_items = []
        self.recipebuilder_name.SetLabel(self.current_recipe_name)

    def recipebuilder_save( self, event ):
        self.current_recipe_name = self.recipebuilder_name.GetValue()
        self.EndModal(wx.ID_OK)

    def recipebuilder_delete( self, event ):
        self.current_recipe_name = ''
        self.current_recipe_items = []
        self.EndModal(wx.ID_OK)

    def cell_menu( self, event ):


    def RecipeBuilderOnContextMenu( self, event ):
        self.PopupMenu( self.recipebuilder_popup_menu, event.GetPosition() )
