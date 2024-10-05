import wx
from filterDialog import MyDialog1

class FilterDialog(MyDialog1):
    def __init__(self, parent):
        super().__init__(parent)
        self.initialize_dialog()

    def initialize_dialog(self):
        self.m_choice1.SetItems([
            "Caloric Value", "Fat", "Saturated Fats", "Monounsaturated Fats",
            "Polyunsaturated Fats", "Carbohydrates", "Sugars", "Protein",
            "Dietary Fiber", "Cholesterol", "Sodium", "Water", "Vitamin A",
            "Vitamin B1", "Vitamin B11", "Vitamin B12", "Vitamin B2",
            "Vitamin B3", "Vitamin B5", "Vitamin B6", "Vitamin C",
            "Vitamin D", "Vitamin E", "Vitamin K", "Calcium", "Copper",
            "Iron", "Magnesium", "Manganese", "Phosphorus", "Potassium",
            "Selenium", "Zinc", "Nutrition Density"
        ])

        self.m_button4.Bind(wx.EVT_BUTTON, self.clear_filters)

    def clear_filters(self, event):
        # Reset choice control
        self.m_choice1.SetSelection(0)

        # Clear text controls
        self.m_textCtrl2.SetValue("")  # Clear minimum value
        self.m_textCtrl3.SetValue("")  # Clear maximum value

        # Unselect all radio buttons
        self.m_radioBtn1.SetValue(False)
        self.m_radioBtn2.SetValue(False)
        self.m_radioBtn3.SetValue(False)

    def apply_filters(self, event):
        # Get the selected nutrient from the choice control
        selected_nutrient = self.m_choice1.GetString(self.m_choice1.GetSelection())

        # Get the minimum and maximum values from the text controls
        try:
            min_value = float(self.m_textCtrl2.GetValue())
        except ValueError:
            min_value = None

        try:
            max_value = float(self.m_textCtrl3.GetValue())
        except ValueError:
            max_value = None

        if self.m_radioBtn1.GetValue():
            level = "Low"
        elif self.m_radioBtn2.GetValue():
            level = "Medium"
        elif self.m_radioBtn3.GetValue():
            level = "High"
        else:
            level = None

        self.filter_text = f"Nutrient: {selected_nutrient}, Min: {min_value}, Max: {max_value}, Level: {level}"
        self.selected_nutrient = selected_nutrient
        self.min_value = min_value
        self.max_value = max_value
        self.level = level
        self.EndModal(wx.ID_OK)

if __name__ == "__main__":
    app = wx.App(False)
    dialog = FilterDialog(None)
    app.MainLoop()
