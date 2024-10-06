import wx
from welcomePage import MyFrame1
from mainPageFunctionality import FoodDataTable

class MainApp(wx.App):
    def OnInit(self):
        self.frame1 = MyFrame1(None)
        self.frame1.Show(True)
        return True

    def open_frame2(self):
        self.frame1.Hide()  # Hide the welcome page
        self.frame2 = FoodDataTable(None)  # Open the data table with search functionality
        self.frame2.Show(True)

    # Modify MyFrame1's on_get_started method to switch to FoodDataTable
    def on_get_started(self, event):
        wx.GetApp().open_frame2()  # Call the app method to switch frames
    MyFrame1.on_get_started = on_get_started

# Run the app
if __name__ == "__main__":
    app = MainApp(False)
    app.MainLoop()
