import wx

from setAmountDialog import change_amount
class SetAmount(change_amount):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_amount = ''

    def amount_save( self, event ):
        current_amount = self.set_amount_value.GetValue()
        if current_amount:
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Please enter a valid amount.", "Error", wx.OK | wx.ICON_ERROR)
