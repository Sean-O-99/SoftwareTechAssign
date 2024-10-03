import wx

class NutritionalDialog(wx.Dialog):
    def __init__(self, parent, food_item, nutritional_info):
        super().__init__(parent, id=wx.ID_ANY, title=f"Nutrition Breakdown: {food_item}", size=(800, 600))

