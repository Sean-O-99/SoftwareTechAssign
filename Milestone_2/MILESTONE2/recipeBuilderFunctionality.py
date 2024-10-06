import wx.grid
import wx

from recipeBuilderPage import RecipeBuilder

class Recipe(RecipeBuilder):


    def recipebuilder_save(self, event):
    event.Skip()

    def recipebuilder_delete(self, event):
    event.Skip()

    def cell_menu(self, event):
    event.Skip()

    def RecipeBuilderOnContextMenu(self, event):
    self.PopupMenu(self.recipebuilder_popup_menu, event.GetPosition())


if __name__ == "__main__":
    app = wx.App()
    frame = Recipe()
    app.MainLoop()