import wx.grid
import wx

from recipeBuilderPage import RecipeBuilder

class Recipe(RecipeBuilder):
    def __init__(self, parent=None):
        super().__init__(parent)


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