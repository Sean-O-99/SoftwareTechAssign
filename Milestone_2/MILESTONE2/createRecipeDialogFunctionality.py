
import wx
from createRecipeDialog import CreateRecipe

class NameRecipeDialog(CreateRecipe):
    def __init__(self, parent):
        super().__init__(parent)
    def save_recipe( self, event ):

        #get recipe name
        recipe_name = self.createrecipe_name_field.GetValue()

        if recipe_name:
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Please enter a name.", "Error", wx.OK | wx.ICON_ERROR)


